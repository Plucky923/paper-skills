# Positioning Evidence and Intellectual Moves

Use this contract when prose uses prior-work evidence to position research.
Also use it for `Observation`, `Key observation`, `Insight`, `Design objective`, or equivalent Chinese paragraph labels.
It adds checks to the [writing core](writing-core.md) and [interface-boundary contract](interface-boundaries.md).
These checks do not specify a required sentence order.

## Distill evidence into the comparison claim

Keep these three different levels:

```text
source evidence
  -> decision-relevant capability or limitation
    -> bounded comparison, question, or gap
```

A repository layout, build command, linked object, configuration file, or artifact behavior is **source evidence**.
Put it in the primary argument only when that realization is the related mechanism or boundary.
If that condition does not hold, give the capability that it shows.
Keep its provenance in the citation, evidence note, or review record.

For example, a verified host-side rebuild can show who introduces code and at what stage.
The comparison concerns deployment control.
The reviewer's artifact inspection is evidence for that comparison, not its subject.

Before acceptance of an artifact-backed comparison, find this tuple:

```text
actor -> changeable object -> stage -> required control or approval
      -> consequence on the paragraph's comparison axis
```

Use the narrowest consequence that the evidence supports.
Source availability alone does not show tenant-controlled deployment.
One build fact does not prove absence of deployment control when another supported path can exist.
Review keeps artifact observation and manuscript-level inference in different evidence states.

Revise can do **artifact-to-capability distillation** only with a supplied inference.
The capability statement must keep the initial fact's scope.

## Reject tuple novelty without a scientific bridge

`The inspected systems do not simultaneously provide A, B, and C` is a **conjunctive gap**.
It is a set-intersection claim.
It does not give an explanation for a research problem.
Before use for positioning or novelty, find these items:

1. The searched population and the reason it covers the claimed scope
2. One parallel value for each named system on A, B, and C
3. Evidence for each negative cell
4. The shared assumption, mechanism, or constraint that makes the conjunction difficult or previously unavailable
5. The resulting design requirement or research question.

An absent description does not prove a negative cell.
`in these concrete systems`, `to our knowledge`, and `not yet together` can narrow or hedge the set claim.
They do not supply the missing scientific bridge.

If sources show only different boundary placements, consider the interface contract's `distinct question` mode.
Use it only when the author intends that mode and gives permission for it.
A comparison can also end after a taxonomy that helps the comparison.
Neither action shows novelty by itself.

Review gives three failures independently:

- A comparison whose dimensions do not match
- Negative cells or population claims without support
- A missing causal bridge.

Revise does not turn a blocked conjunction into a novelty sentence through word changes.
Give the author the choice between a descriptive map, distinct question, and negative gap.
Request the specified evidence necessary for that choice.

## Audit the observation ladder

Keep these different roles, even in one paragraph's short handoff:

| Role | Question answered |
|---|---|
| Evidence observation | What pattern, contrast, counterexample, or measurement is visible, and in what scope? |
| Interpretation | What relation does the evidence support, and with what epistemic strength? |
| Insight or design observation | What non-obvious relation changes the design or reasoning space? |
| Requirement | What property must a correct design supply because of a shown constraint? |
| Objective | What outcome does the system select for optimization or preservation? |
| Mechanism | How does the design complete the requirement or objective? |

A clear `Observation` or `Insight` paragraph passes only with a controlling update grounded in source evidence.
That update must distinguish the work and have a consequence.
Do these checks:

- **Anchor:** Find the scoped pattern, contrast, counterexample, model fact, or result.
- **Relation:** Find an inference beyond actor renaming, term explanation, or premise repetition.
- **Information gain:** Delete the controlling statement as an internal test.
  Make sure that deletion loses a relation not mechanically available from the heading or premises.
- **Prediction:** Find the choices, tests, or conditions that the relation makes possible, impossible, or necessary.
- **Boundary:** Find where the relation fails or narrows, or what evidence stays missing.

Five sentences or five clear slots are not necessary.
The checks concern its available inferential content.
Reject these substitutes:

- `the above differences show ...`, when `differences` has no specified referent or an unstated cross-system premise is necessary for the conclusion
- A definition repeated as an insight, such as `the interface determines what the interface permits`
- A repeated goal, such as `supporting independent customization requires independent customization`
- Desired properties or mechanisms listed with an observation label
- An ending that only repeats the heading as a positive statement or requirement.

If the material gives only a requirement or objective, record that delivered role.
An author's role label stays the promised role.
An internal role change does not make the paragraph pass.

## Keep independent goals independent

A design can select several objectives.
Connect them below one insight only with source evidence for each fan-out edge in the writing core.
Use `independently of the above requirement` only with a different objective and its own scientific account.
Give that account's constraint, mechanism, evidence, and contribution status.
The passage cannot reject the dependency and also rely on a single-observation account.

For path objectives, keep this progression clear:

```text
path cost to remove -> path change -> remaining work
  -> path-level prediction -> measured end-to-end result, if available
```

In completed-paper prose, a future evaluation instruction is not the payoff for this progression.
Request its metric, baseline, conditions, result, and uncertainty.
Do not invent or delete the scientific question.

## Review and revision actions

Review locates the first broken step at the two endpoints.
It keeps paragraph-role, evidence-truth, and external-verification findings independent.
It records the delivered role: evidence observation, interpretation, insight, requirement, objective, mechanism, or a mixed role.
It does not supply replacement prose.

Revise first does local distillation when evidence supports it.
For identified repetition, use the compression rule in [writing-core.md](writing-core.md).
When a supplied principle has a local organization defect, repair its detail hierarchy within the permitted paragraph:

1. Put the supplied principle above its retained details in an internal outline.
2. Assign every detail its stated role: operating duty, property definition, claimed consequence, or evidence boundary.
3. Group all operating duties in one realization account with the design as their shared referent.
   Preserve each duty's actor, action, object, and condition.
   Use subordinate clauses or explicitly linked short sentences; grouping only a subset leaves this step incomplete.
4. Attach the property definitions, claimed consequences, and evidence boundaries to the same design account in distinct roles.
   A definition specifies the property; it does not establish that the design achieves it.
5. Compare the result with the outline.
   Every retained detail must have a visible place below the governing principle.
   A principle followed by an unchanged list does not complete the repair.
   A shared frame covering only some details is also incomplete.

The supplied principle and stated design membership license this information hierarchy.
Grouping the design's duties does not assert that each duty is necessary or that their conjunction proves a claimed outcome.
Keep each claimed consequence at its initial strength and evidence status.
Leave unknown causal contribution, necessity, and sufficiency in their applicable author-input classes.
Complete the organization repair before requesting those missing scientific links.
If there is no source-grounded intellectual move, do not invent one from a system list or requirement.
Put the missing anchor or relation in `author evidence`.
Put the intended role or bridge choice in `author clarification`.

Get clear structural permission for paragraph renaming, repurposing, splitting, or movement.
For those structural operations, rebuild after the author supplies the necessary relation and permission.
Keep the initial paragraph boundary and each proposition that the evidence supports.
