# Chinese Systems-Writing Calibration

Use the canonical logic in [writing-core.md](writing-core.md). This reference covers failure modes specific to Chinese drafts and Chinese-to-English revision; it does not impose a more ornate or “academic” register.

## Restore technical agency

Chinese permits an omitted subject, but a systems claim must expose who acts and what changes. Distinguish:

- an author choice: `本文比较……` or an equivalent direct formulation;
- a system action: `Nimbus 合并确认消息……`;
- a mechanism property: `页表权限阻止已验证页面被写入……`;
- an experimental observation: `实验测得……`.

> **原文：**“Nimbus 对确认消息进行合并操作，将这些确认消息合并为一个批次。”
>
> **去除重复：**“Nimbus 将确认消息合并为一个批次。”

The repair removes repeated wording; it adds no benefit or experimental plan. Restore an omitted actor only when the supplied text identifies it unambiguously. Otherwise flag the ambiguity rather than choosing an actor.

## Audit every causal arrow

Constructions such as `通过 A，从而 B，进而 C，最终 D` often hide several independent claims. For each arrow, determine whether it is:

- a mechanism relation;
- a design prediction;
- an observed result;
- or an unsupported inference.

Clarify directly dependent steps only when their relation is already established. Different evidence obligations are diagnostic findings, not permission to supply missing science.

> **过载：**“系统通过分离元数据和数据，从而避免协调并保证隔离。”
>
> **处理：**保留这句原文，在正文外指出：“分离元数据和数据 → 避免协调并保证隔离”缺少推导或支持。不能自行补入协调协议、页表权限或其他隔离机制，也不能擅自将“保证”改成“可能”。

## Replace proposal shells with technical relations

`针对……问题，提出……方法` and `为了……，设计了……` can state a paper action without explaining the advance. Check whether the supplied paragraph already establishes the concrete repeated work, failed assumption, changed boundary, or new observation. Missing technical content requires author input, not an invented explanation.

> **原文：**“对于每个请求，系统都会重新计算放置决策，即每次请求都要重复计算放置决策。”
>
> **去除重复：**“系统为每个请求重新计算放置决策。”

Prefer a direct technical predicate over stacked nominalizations such as `实现了对……的有效支持` when the underlying action is `缓存`、`隔离`、`延迟`、`验证`、`复制` or `限制`.

## Match Chinese verbs to evidence

- `观察到`、`测得` report data; they do not by themselves prove a cause.
- `表明` fits a directly supported bounded conclusion; `提示` or `可能说明` retains plausible alternatives.
- `证明` requires a valid proof or equivalently decisive argument within its model.
- `保证`、`确保` require an invariant, proof, or exhaustive enforcement under explicit assumptions.
- `支持`、`允许` describe a capability; name the user, action, and condition.
- `消除`、`避免` claim absence in a stated scope; `降低` and `移出关键路径` assert different properties, not interchangeable stylistic alternatives.

Treat `高效`、`轻量`、`灵活`、`可扩展`、`鲁棒`、`安全`、`显著`、`全面` and `普适` as claims. Check their supporting property, comparison, and boundary. If support is missing, retain the affected assertion and identify the gap separately; changing its strength requires an explicit author decision.

## Keep references and terms explicit

Resolve `该方法`、`该问题`、`其` and `这` to a unique local antecedent. A small amount of exact noun repetition is cheaper than forcing the reader to choose among several mechanisms or results.

Use one stable Chinese or English label for each technical concept. Terms such as `隔离`、`内存安全`、`故障域` and `访问控制` are not stylistic synonyms; preserve the property each one denotes.

## Translate logic, not word order

Before translating, recover the actor, dominant assertion, conditions, logical relation, evidence status, and boundary. Rebuild the English sentence around those roles rather than copying Chinese topic chains or omitted subjects.

> **中文：**“运行时跨请求缓存解析后的对象，避免稳态路径上的重复解析。”
>
> **保义翻译：**“The runtime caches parsed objects across requests, avoiding repeated parsing on the steady-state path.”

Every technical detail in the translation is present in the source. A generic source such as “通过缓存中间结果，有效提升了系统性能” does not license inventing parsed objects, cross-request reuse, or a steady-state path. Translate its assertion faithfully and flag missing scientific support separately when unresolved. Include measured results only when supplied and within the requested task; `effectively`、`obviously` and `significantly` cannot supply evidence.

## Preserve concise Chinese rhythm

Keep adequate wording and information order. When a concrete ambiguity or ordering defect requires repair, make the governing relation recoverable and use connectives only for established relations. Sentence splitting or merging must remain inside the original paragraph and preserve its meaning, emphasis, and manuscript format. A merely preferable rhythm belongs in optional wording, not the main revision.
