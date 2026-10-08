#!/usr/bin/env python3
"""Allowlisted, audited stdio MCP access for frozen benchmark invocations.

This process has no shell or arbitrary-code tool. The harness supplies its
policy; the candidate can only read declared inputs, write the current stage's
declared project files, and (when enabled) fetch the live official ASPLOS site.
Runtime authentication and session storage are outside this candidate surface.
"""

import argparse
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request


PROTOCOL = "benchmark-allowlisted-access-v1"
OFFICIAL_HOSTS = {"www.asplos-conference.org", "asplos-conference.org"}
MAX_BYTES = 4 * 1024 * 1024


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


class AccessDenied(ValueError):
    pass


class PageText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.parts = []
        self.links = []
        self.anchor = None

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self.hidden += 1
        if self.hidden:
            return
        if tag in ("p", "br", "li", "h1", "h2", "h3", "h4", "tr", "div", "article"):
            self.parts.append("\n")
        if tag == "a":
            self.anchor = {"href": dict(attrs).get("href", ""), "parts": []}

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.hidden = max(0, self.hidden - 1)
        if tag == "a" and self.anchor is not None:
            self.links.append({"url": self.anchor["href"], "text": " ".join(self.anchor["parts"]).strip()})
            self.anchor = None
        if not self.hidden and tag in ("p", "li", "h1", "h2", "h3", "h4", "tr", "article"):
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)
            if self.anchor is not None:
                self.anchor["parts"].append(data.strip())

    def result(self, base):
        lines = [" ".join(line.split()) for line in "".join(self.parts).splitlines()]
        links = []
        seen = set()
        for item in self.links:
            url = urllib.parse.urljoin(base, item["url"])
            if urllib.parse.urlparse(url).hostname in OFFICIAL_HOSTS and url not in seen:
                links.append({"url": url, "text": item["text"]})
                seen.add(url)
        return "\n".join(line for line in lines if line), links


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        return None


class AccessServer:
    def __init__(self, policy_path):
        self.policy = json.loads(Path(policy_path).read_text(encoding="utf-8"))
        self.bundle = Path(self.policy["bundle_root"]).resolve()
        self.project = Path(self.policy["project_root"]).resolve() if self.policy.get("project_root") else None
        self.inputs = set(self.policy["bundle_files"])
        self.reads = set(self.policy.get("project_reads", []))
        self.writes = set(self.policy.get("project_writes", []))
        self.web = bool(self.policy.get("official_web"))
        self.evidence = Path(self.policy["evidence_root"])
        self.evidence.mkdir(exist_ok=True)
        (self.evidence / "blobs").mkdir(exist_ok=True)
        self.log = self.evidence / "access.jsonl"
        self.sequence = 0
        self.previous = None
        if self.log.exists():
            for line in self.log.read_text(encoding="utf-8").splitlines():
                event = json.loads(line)
                self.sequence = event["sequence"]
                self.previous = event["event_sha256"]

    def blob(self, data):
        name = sha(data)
        path = self.evidence / "blobs" / name
        if path.exists():
            if path.read_bytes() != data:
                raise RuntimeError("Evidence digest collision")
        else:
            with path.open("xb") as handle:
                handle.write(data)
        return {"sha256": name, "bytes": len(data), "artifact": "blobs/" + name}

    def record(self, operation, arguments, status, detail):
        self.sequence += 1
        event = {"protocol": PROTOCOL, "sequence": self.sequence,
                 "at": datetime.now(timezone.utc).isoformat(), "previous_sha256": self.previous,
                 "operation": operation, "arguments": arguments, "status": status, "detail": detail}
        event["event_sha256"] = sha(encoded(event))
        with self.log.open("ab") as handle:
            handle.write(encoded(event) + b"\n")
            handle.flush()
            os.fsync(handle.fileno())
        self.previous = event["event_sha256"]

    def path(self, value, write=False):
        if not isinstance(value, str) or not value or "\x00" in value:
            raise AccessDenied("A declared file path is required")
        if value.startswith("bundle:"):
            candidate = self.bundle / value[len("bundle:"):].lstrip("/")
        elif value.startswith("project:") and self.project:
            candidate = self.project / value[len("project:"):].lstrip("/")
        elif Path(value).is_absolute():
            candidate = Path(value)
        elif self.project and value in self.reads | self.writes:
            candidate = self.project / value
        else:
            candidate = self.bundle / value
        # No input symlink may grant access to an undeclared target.
        resolved = candidate.resolve()
        for root, namespace, names in ((self.bundle, "bundle", self.inputs),
                                        (self.project, "project", self.writes if write else self.reads)):
            if root is None or (write and namespace != "project"):
                continue
            try:
                relative = resolved.relative_to(root).as_posix()
            except ValueError:
                continue
            if relative in names and not candidate.is_symlink():
                return resolved, namespace + ":" + relative
        raise AccessDenied("File is outside the current invocation's declared access policy")

    def tools(self):
        tools = [
            {"name": "read_file", "description": "Read a declared frozen skill/reference or authorized project file. Use its absolute path or bundle: / project: path. Full content is returned unless a line range is requested. Every read is recorded.",
             "inputSchema": {"type": "object", "properties": {"path": {"type": "string"}, "start_line": {"type": "integer", "minimum": 1}, "max_lines": {"type": "integer", "minimum": 1}}, "required": ["path"], "additionalProperties": False}},
            {"name": "list_files", "description": "List only declared bundle input files or authorized project files. This does not inspect directories outside the declared inputs.",
             "inputSchema": {"type": "object", "properties": {"namespace": {"type": "string", "enum": ["bundle", "project"]}}, "required": ["namespace"], "additionalProperties": False}},
        ]
        if self.writes:
            tools.append({"name": "write_file", "description": "Replace the complete content of one explicitly writable project file. This performs a real persistent write and returns its digest. Read the file first when preserving existing material; use read_file for the required read-back.",
                          "inputSchema": {"type": "object", "properties": {"path": {"type": "string"}, "content": {"type": "string"}}, "required": ["path", "content"], "additionalProperties": False}})
        if self.web:
            tools += [
                {"name": "read_url", "description": "Read a live public official ASPLOS page. Only HTTPS asplos-conference.org and www.asplos-conference.org are allowed. The full response bytes, URL, headers, retrieval time, visible text and official links are retained.",
                 "inputSchema": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"], "additionalProperties": False}},
                {"name": "search_official", "description": "Search the live official ASPLOS website. This retrieves that website's own search page; it does not use an unofficial summary or a cached venue registry. Follow relevant official URLs with read_url.",
                 "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"], "additionalProperties": False}},
            ]
        return tools

    def fetch(self, url):
        responses = []
        opener = urllib.request.build_opener(NoRedirect)
        for _ in range(6):
            parsed = urllib.parse.urlparse(url)
            if (parsed.scheme != "https" or parsed.hostname not in OFFICIAL_HOSTS
                    or parsed.username or parsed.password or parsed.port not in (None, 443)):
                raise AccessDenied("Only the live official ASPLOS HTTPS hosts are allowed")
            request = urllib.request.Request(url, headers={"User-Agent": "PaperSkillsBenchmark/1.0 (+read-only official-source verification)"})
            try:
                response = opener.open(request, timeout=45)
            except urllib.error.HTTPError as response:
                body = response.read(MAX_BYTES + 1)
                response_record = {"url": url, "status": response.code, "headers": dict(response.headers), "body": self.blob(body)}
                if response.code in (301, 302, 303, 307, 308):
                    responses.append(response_record)
                    url = urllib.parse.urljoin(url, response.headers["Location"])
                    continue
                return {"url": url, "retrieved_at": datetime.now(timezone.utc).isoformat(), "available": False,
                        "response": response_record, "redirects": responses,
                        "verification_status": "Official page unavailable; no current venue rule is established by this result."}
            except (urllib.error.URLError, TimeoutError) as exc:
                return {"url": url, "retrieved_at": datetime.now(timezone.utc).isoformat(), "available": False,
                        "redirects": responses, "network_error": type(exc).__name__ + ": " + str(exc),
                        "verification_status": "Official verification unavailable; mark venue facts unresolved rather than treating cached rules as current."}
            with response:
                body = response.read(MAX_BYTES + 1)
                if len(body) > MAX_BYTES:
                    raise AccessDenied("Official response exceeds the response byte limit")
                headers = dict(response.headers)
                content_type = response.headers.get_content_type()
                charset = response.headers.get_content_charset() or "utf-8"
                if content_type not in ("text/html", "text/plain", "application/xhtml+xml"):
                    raise AccessDenied("Only public text/HTML official pages are supported")
                text = body.decode(charset, errors="replace")
                if content_type != "text/plain":
                    parser = PageText()
                    parser.feed(text)
                    text, links = parser.result(url)
                else:
                    links = []
                result = {"url": url, "retrieved_at": datetime.now(timezone.utc).isoformat(), "available": True,
                          "status": response.status, "headers": headers, "body": self.blob(body),
                          "redirects": responses, "visible_text": text, "official_links": links}
                return result
        raise AccessDenied("Official redirect limit exceeded")

    def call(self, name, args):
        try:
            tools = {tool["name"]: tool for tool in self.tools()}
            if name not in tools:
                raise AccessDenied("Tool is not enabled for this invocation")
            if not isinstance(args, dict):
                raise AccessDenied("Tool arguments must be an object")
            schema = tools[name]["inputSchema"]
            if set(args) - set(schema["properties"]) or not set(schema["required"]).issubset(args):
                raise AccessDenied("Tool arguments do not match the declared schema")
            if name == "list_files":
                if args.get("namespace") == "bundle":
                    result = {"namespace": "bundle", "files": sorted(self.inputs)}
                elif args.get("namespace") == "project" and self.project:
                    result = {"namespace": "project", "files": sorted(self.reads), "writable": sorted(self.writes)}
                else:
                    raise AccessDenied("Namespace is not enabled")
            elif name == "read_file":
                path, identity = self.path(args.get("path"))
                raw = path.read_bytes()
                if len(raw) > MAX_BYTES:
                    raise AccessDenied("File exceeds the input byte limit")
                content = raw.decode("utf-8")
                lines = content.splitlines(keepends=True)
                start, count = args.get("start_line", 1), args.get("max_lines", len(lines) or 1)
                if type(start) is not int or type(count) is not int or start < 1 or count < 1:
                    raise AccessDenied("Line ranges must be positive integers")
                selected = "".join(lines[start - 1:start - 1 + count])
                result = {"path": identity, "file": self.blob(raw), "total_lines": len(lines),
                          "start_line": start, "end_line": min(len(lines), start - 1 + count), "content": selected}
            elif name == "write_file":
                path, identity = self.path(args.get("path"), write=True)
                if not isinstance(args.get("content"), str):
                    raise AccessDenied("Content must be UTF-8 text")
                raw = args["content"].encode("utf-8")
                if len(raw) > MAX_BYTES:
                    raise AccessDenied("Write exceeds the project byte limit")
                before = self.blob(path.read_bytes()) if path.exists() else None
                with path.open("wb") as handle:
                    handle.write(raw)
                    handle.flush()
                    os.fsync(handle.fileno())
                result = {"path": identity, "before": before, "after": self.blob(path.read_bytes())}
            else:
                if name == "search_official":
                    if not isinstance(args.get("query"), str) or not args["query"].strip():
                        raise AccessDenied("A nonempty official-site query is required")
                    url = "https://www.asplos-conference.org/?" + urllib.parse.urlencode({"s": args["query"]})
                else:
                    url = args.get("url")
                    if not isinstance(url, str):
                        raise AccessDenied("A URL is required")
                result = self.fetch(url)
            self.record(name, args if name != "write_file" else {"path": args.get("path"), "content": self.blob(args["content"].encode("utf-8"))}, "allowed", {"response": self.blob(encoded(result))})
            return {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False)}], "isError": False}
        except Exception as exc:
            message = type(exc).__name__ + ": " + str(exc)
            self.record(name, args if name != "write_file" else {"path": args.get("path") if isinstance(args, dict) else None}, "denied" if isinstance(exc, AccessDenied) else "failed", {"error": message})
            return {"content": [{"type": "text", "text": message}], "isError": True}

    def serve(self):
        for line in sys.stdin.buffer:
            request = None
            try:
                request = json.loads(line)
                identifier, method = request.get("id"), request.get("method")
                if identifier is None:
                    continue
                if method == "initialize":
                    result = {"protocolVersion": request.get("params", {}).get("protocolVersion", "2024-11-05"),
                              "capabilities": {"tools": {}}, "serverInfo": {"name": "benchmark_access", "version": "1.0.0"}}
                elif method == "tools/list":
                    result = {"tools": self.tools()}
                elif method == "tools/call":
                    params = request.get("params", {})
                    result = self.call(params.get("name"), params.get("arguments", {}))
                elif method in ("resources/list", "resources/templates/list"):
                    result = {"resources" if method == "resources/list" else "resourceTemplates": []}
                elif method == "ping":
                    result = {}
                else:
                    self.record("protocol:" + str(method), request.get("params", {}), "denied", {"error": "Unknown MCP method"})
                    raise AccessDenied("Unknown MCP method")
                response = {"jsonrpc": "2.0", "id": identifier, "result": result}
            except Exception as exc:
                response = {"jsonrpc": "2.0", "id": request.get("id") if isinstance(request, dict) else None,
                            "error": {"code": -32600, "message": type(exc).__name__ + ": " + str(exc)}}
            sys.stdout.buffer.write(encoded(response) + b"\n")
            sys.stdout.buffer.flush()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, required=True)
    args = parser.parse_args()
    AccessServer(args.policy).serve()


if __name__ == "__main__":
    main()
