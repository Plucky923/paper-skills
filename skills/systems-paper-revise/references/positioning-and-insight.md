# Positioning Evidence and Intellectual Moves

Use this contract when prose turns prior-work inspection into a research
position, or labels a paragraph `Observation`, `Key observation`, `Insight`,
`Design objective`, or an equivalent Chinese role. It specializes the
[writing core](writing-core.md) and the
[interface-boundary contract](interface-boundaries.md). The relations below are
quality gates, not a required sentence order.

## Distill evidence into the comparison claim

Keep three levels distinct:

```text
source evidence
  -> decision-relevant capability or limitation
    -> bounded comparison, question, or gap
```

A repository layout, build command, linked object, configuration file, or
artifact behavior is **source evidence**. It belongs in the main argumentative
line only when that concrete realization is itself the relevant mechanism or
boundary. Otherwise express the capability it establishes and retain the
provenance in the citation, evidence note, or review record. For example, a
verified host-side rebuild may establish who can introduce which code at what
stage; the comparison is about deployment control, not about the reviewer having
opened a public artifact.

For every artifact-backed comparison, recover this tuple before accepting the
sentence:

```text
actor -> changeable object -> stage -> required control or approval
      -> consequence on the paragraph's comparison axis
```

The visible prose should use the narrowest supported consequence. Do not infer
tenant-controlled deployment from source availability, or lack of deployment
control from one build fact when another supported path may exist. Review keeps
the artifact observation and the manuscript-level inference as separate evidence
states. Revise may perform an **artifact-to-capability distillation** only when
the inference is supplied and the capability statement preserves the original
fact's scope.

## Reject tuple novelty without a scientific bridge

`The inspected systems do not simultaneously provide A, B, and C` is a
**conjunctive gap**. It is a set-intersection claim, not yet an explanation of a
research problem. Before it can carry positioning or novelty, recover:

1. the searched population and why it covers the claimed scope;
2. one parallel value for every named system on A, B, and C;
3. evidence for every negative cell rather than absence from a description;
4. the shared assumption, mechanism, or constraint that makes the conjunction
   difficult or previously unavailable; and
5. the design requirement or research question that follows from that cause.

Adding `in these concrete systems`, `to our knowledge`, or `not yet together`
only narrows or hedges the set claim; it does not supply the missing scientific
bridge. When the sources support only different boundary placements, use the
interface contract's `distinct question` mode if the author intends and
authorizes it. A comparison may also stop after a useful taxonomy. Neither move
establishes novelty by itself.

Review reports three failures independently: nonparallel comparison, unsupported
negative cells or population, and missing causal bridge. Revise does not polish a
blocked conjunction into a novelty sentence. It asks whether the author intends
a descriptive map, a distinct question, or a negative gap, plus the exact
evidence needed by that choice.

## Audit the observation ladder

Keep these roles separate even when one paragraph contains a short handoff:

| Role | Question answered |
|---|---|
| Evidence observation | What concrete pattern, contrast, counterexample, or measurement is visible, under what scope? |
| Interpretation | What relation does that evidence support, at what epistemic strength? |
| Insight or design observation | What non-obvious relation changes the design or reasoning space? |
| Requirement | What property must a valid design provide because of an established constraint? |
| Objective | What outcome does the system choose to optimize or preserve? |
| Mechanism | How does the design realize the requirement or objective? |

A paragraph explicitly promised as an `Observation` or `Insight` passes only if
its controlling update is source-grounded, discriminating, and consequential:

- **anchor:** a scoped pattern, contrast, counterexample, model fact, or result;
- **relation:** a non-definitional inference beyond renaming the actors,
  unpacking a term, or restating a premise;
- **information gain:** deletion of the controlling statement loses a relation
  not mechanically recoverable from the heading or premises;
- **prediction:** the relation rules in, rules out, or makes necessary a class of
  design choices, evidence tests, or boundary conditions; and
- **boundary:** the reader can identify when the relation would fail or narrow,
  or what evidence remains needed.

Not every observation paragraph needs five sentences or five explicit slots.
The gate asks whether the inferential content is recoverable. It rejects common
substitutes:

- `the above differences show ...` when `differences` has no exact referent or
  the conclusion needs an unstated cross-system premise;
- a definitional restatement such as `the interface determines what the
  interface permits`;
- a goal restatement such as `supporting independent customization requires
  independent customization`;
- a list of desired properties or mechanisms under an observation label; and
- an ending that merely repeats the heading in positive or required form.

When the visible material supplies only a requirement or objective, classify the
delivered role honestly. A role label supplied by the author remains the promised
role; reclassifying the paragraph internally does not make it pass.

## Keep independent goals independent

A design may have several legitimate objectives. Connect them under one insight
only when every fan-out edge is source-grounded under the writing core. A phrase
such as `independently of the above requirement` is acceptable only if the paper
then presents a second objective with its own constraint, mechanism, evidence,
and contribution status. It cannot both disclaim the dependency and rely on a
single-observation story.

For path objectives, keep the progression explicit:

```text
path cost to remove -> path change -> remaining work
  -> path-level prediction -> measured end-to-end result, if available
```

In completed-paper prose, a future evaluation instruction is not the payoff for
that progression. Request the metric, baseline, conditions, result, and
uncertainty rather than manufacturing or deleting the scientific question.

## Review and revision actions

Review anchors the first broken step at both endpoints and keeps paragraph-role,
evidence-truth, and external-verification findings independent. It states whether
the visible text delivers evidence observation, interpretation, insight,
requirement, objective, mechanism, or a mixed role; it does not supply replacement
prose.

Revise first performs supported local distillation and removes genuine
metadiscourse or repetition. If no source-grounded intellectual move exists, it
does not fabricate one from a system list or requirement. It routes the exact
missing anchor or relation to `author evidence`, and the intended role or bridge
choice to `author clarification`. Renaming, repurposing, splitting, or moving a
paragraph still requires explicit structural authority. Once the author supplies
the relation and authority, Revise rebuilds the paragraph around that controlling
update while preserving its original boundary and all supported propositions.
