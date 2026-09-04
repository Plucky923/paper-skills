"""Pinned, checksum-verified downloads; no upstream code is executed."""

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
from urllib.parse import urlparse
from urllib.request import Request, urlopen


class BenchmarkError(ValueError):
    pass


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def stable_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def safe_name(value):
    if not isinstance(value, str) or not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_.-]{0,99}", value):
        raise BenchmarkError("Expected a short alphanumeric name, not a path: {!r}".format(value))
    return value


def inside(root, relative):
    rel = PurePosixPath(relative)
    if rel.is_absolute() or ".." in rel.parts or "\\" in str(relative) or not rel.parts:
        raise BenchmarkError("Unsafe relative path: {!r}".format(relative))
    root = Path(root).resolve()
    target = root.joinpath(*rel.parts)
    try:
        target.resolve().relative_to(root)
    except ValueError:
        raise BenchmarkError("Path or symlink escapes its root: {}".format(target))
    return target


def read_json(path):
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path, value):
    """Publish a complete JSON record atomically without replacing evidence."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=str(path.parent),
                                         prefix=".json-", delete=False) as handle:
            partial = Path(handle.name)
            json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        # Same-directory linking is atomic and, unlike rename, never overwrites.
        os.link(str(partial), str(path))
    finally:
        if partial is not None:
            partial.unlink(missing_ok=True)


def write_jsonl(path, values):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        for value in values:
            handle.write(json.dumps(value, ensure_ascii=False, allow_nan=False) + "\n")


def read_jsonl(path):
    with Path(path).open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def load_registry(repo):
    policy = read_json(Path(repo) / "benchmarks/external/admission.json")
    if policy.get("schema_version") != 1:
        raise BenchmarkError("Unsupported admission policy")
    decisions = policy["sources"]
    sources = {}
    for path in sorted((Path(repo) / "benchmarks/external").glob("*-sources.json")):
        document = read_json(path)
        if document.get("schema_version") != 1:
            raise BenchmarkError("Unsupported registry schema: {}".format(path))
        for source in document["sources"]:
            source_id = safe_name(source["id"])
            decision = decisions.get(source_id)
            if not decision or decision.get("state") != "admitted":
                raise BenchmarkError("Unadmitted source in active registry: " + source_id)
            if source_id in sources:
                raise BenchmarkError("Duplicate source ID: " + source_id)
            paths = set()
            for item in source.get("files", []):
                inside(Path(repo) / "benchmarks/external/cache" / source_id, item["path"])
                if item["path"] in paths:
                    raise BenchmarkError("Duplicate download destination: " + item["path"])
                paths.add(item["path"])
                if not re.fullmatch(r"[0-9a-f]{64}", item.get("sha256", "")):
                    raise BenchmarkError("Missing SHA-256: {} {}".format(source_id, item["path"]))
                if not isinstance(item.get("size_bytes"), int) or item["size_bytes"] < 0:
                    raise BenchmarkError("Invalid byte length: " + item["path"])
                url = urlparse(item["url"])
                if url.scheme != "https" or not url.hostname or url.username or url.password:
                    raise BenchmarkError("Only public HTTPS downloads are supported")
            source["admission"] = dict(decision, policy_version=policy["policy_version"])
            sources[source_id] = source
    expected = {key for key, value in decisions.items() if value.get("state") == "admitted"}
    if set(sources) != expected:
        raise BenchmarkError("Active registry does not match the admission policy")
    return sources


def select_sources(sources, names):
    if not names:
        return [s for s in sources.values() if s.get("default_fetch")]
    if names == ["all"]:
        return list(sources.values())
    unknown = set(names) - set(sources)
    if unknown:
        raise BenchmarkError("Unknown sources: " + ", ".join(sorted(unknown)))
    return [sources[name] for name in dict.fromkeys(names)]


def verify_source(cache, source):
    results = []
    for item in source.get("files", []):
        path = inside(Path(cache) / source["id"], item["path"])
        state = "missing"
        if path.is_file():
            state = "verified" if path.stat().st_size == item["size_bytes"] and digest(path) == item["sha256"] else "checksum_mismatch"
        results.append({"path": item["path"], "status": state, "size_bytes": item["size_bytes"]})
    return {
        "source": source["id"], "revision": source.get("revision"),
        "status": "verified" if results and all(x["status"] == "verified" for x in results) else "incomplete",
        "adapter": source.get("adapter"), "files": results,
    }


def fetch_file(root, item, timeout=45):
    target = inside(root, item["path"])
    if target.exists():
        if target.is_file() and target.stat().st_size == item["size_bytes"] and digest(target) == item["sha256"]:
            return "cached"
        raise BenchmarkError("Existing file differs; preserved without overwriting: {}".format(target))
    target.parent.mkdir(parents=True, exist_ok=True)
    partial = None
    try:
        request = Request(item["url"], headers={"User-Agent": "PaperSkills-benchmark-fetch/1"})
        with urlopen(request, timeout=timeout) as response:
            if urlparse(response.geturl()).scheme != "https":
                raise BenchmarkError("Refusing a non-HTTPS download redirect")
            with tempfile.NamedTemporaryFile(dir=str(target.parent), prefix=".download-", delete=False) as output:
                partial = Path(output.name)
                sha, size = hashlib.sha256(), 0
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    size += len(chunk)
                    if size > item["size_bytes"]:
                        raise BenchmarkError("Download exceeds pinned byte length: " + item["path"])
                    sha.update(chunk)
                    output.write(chunk)
        if size != item["size_bytes"] or sha.hexdigest() != item["sha256"]:
            raise BenchmarkError("Checksum/length mismatch: " + item["path"])
        # Hard-link publication is atomic and refuses an existing destination.
        os.link(str(partial), str(target))
        return "downloaded"
    finally:
        if partial is not None:
            partial.unlink(missing_ok=True)


def fetch_source(cache, source, progress=print):
    if source.get("status") in ("manual", "license_review_required", "blocked"):
        raise BenchmarkError("Manual source not auto-fetched: " + source["id"])
    if not source.get("files"):
        raise BenchmarkError("No pinned downloadable files: " + source["id"])
    for item in source["files"]:
        progress("{} {}: {}".format(source["id"], item["path"], fetch_file(Path(cache) / source["id"], item)))
    return verify_source(cache, source)
