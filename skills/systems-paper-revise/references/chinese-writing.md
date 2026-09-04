# Chinese Systems-Writing Calibration

Use the canonical logic in [writing-core.md](writing-core.md). This reference covers failure modes specific to Chinese drafts and Chinese-to-English revision; it does not impose a more ornate or “academic” register.

## Restore technical agency

Chinese permits an omitted subject, but a systems claim must expose who acts and what changes. Distinguish:

- an author choice: `本文比较……` or an equivalent direct formulation;
- a system action: `Nimbus 合并确认消息……`;
- a mechanism property: `页表权限阻止已验证页面被写入……`;
- an experimental observation: `实验测得……`.

> **含混：**“通过批处理降低了开销，并提升了可扩展性。”
>
> **明确：**“Nimbus 将逐请求确认合并为批量确认，从而减少跨进程通知；实验另行检验该收益能否随客户端数量保持。”

The stronger version separates a mechanism prediction from an empirical conclusion.

## Audit every causal arrow

Constructions such as `通过 A，从而 B，进而 C，最终 D` often hide several independent claims. For each arrow, determine whether it is:

- a mechanism relation;
- a design prediction;
- an observed result;
- or an unsupported inference.

Keep directly dependent steps together and separate claims that require different evidence.

> **过载：**“系统通过分离元数据和数据，从而避免协调并保证隔离。”
>
> **精确：**“系统将共享元数据与私有数据分离。共享元数据仍通过协议协调，而私有数据无需进入该协议。隔离性另外依赖页表权限维持这一边界。”

## Replace proposal shells with technical relations

`针对……问题，提出……方法` and `为了……，设计了……` can state a paper action without explaining the advance. Recover the concrete repeated work, failed assumption, changed boundary, or new observation.

> **空壳：**“针对现有方法效率低的问题，本文提出一种高效、灵活的优化框架。”
>
> **具体：**“现有方法为每个请求重新计算全局放置决策，使调度成本随集群规模增长。Nimbus 复用局部仍有效的决策，仅在负载越过分区边界时重新协调。”

Prefer a direct technical predicate over stacked nominalizations such as `实现了对……的有效支持` when the underlying action is `缓存`、`隔离`、`延迟`、`验证`、`复制` or `限制`.

## Match Chinese verbs to evidence

- `观察到`、`测得` report data; they do not by themselves prove a cause.
- `表明` fits a directly supported bounded conclusion; `提示` or `可能说明` retains plausible alternatives.
- `证明` requires a valid proof or equivalently decisive argument within its model.
- `保证`、`确保` require an invariant, proof, or exhaustive enforcement under explicit assumptions.
- `支持`、`允许` describe a capability; name the user, action, and condition.
- `消除`、`避免` claim absence in a stated scope; `降低` or `移出关键路径` is often the exact narrower relation.

Treat `高效`、`轻量`、`灵活`、`可扩展`、`鲁棒`、`安全`、`显著`、`全面` and `普适` as claims. Replace them with the measured property, mechanism, dimension of variation, comparison, or boundary that gives them content.

## Keep references and terms explicit

Resolve `该方法`、`该问题`、`其` and `这` to a unique local antecedent. A small amount of exact noun repetition is cheaper than forcing the reader to choose among several mechanisms or results.

Use one stable Chinese or English label for each technical concept. Terms such as `隔离`、`内存安全`、`故障域` and `访问控制` are not stylistic synonyms; preserve the property each one denotes.

## Translate logic, not word order

Before translating, recover the actor, dominant assertion, conditions, logical relation, evidence status, and boundary. Rebuild the English sentence around those roles rather than copying Chinese topic chains or omitted subjects.

> **中文：**“通过缓存中间结果，有效提升了系统性能。”
>
> **机械翻译：**“By caching intermediate results, the system performance is effectively improved.”
>
> **逻辑重写：**“The runtime caches parsed objects across requests, avoiding repeated parsing on the steady-state path.”

Report a measured performance result in a separate sentence with its metric, baseline, workload, and condition. `effectively`、`obviously` and `significantly` cannot supply that evidence.

## Preserve concise Chinese rhythm

Place the governing technical relation early. Use short connective phrases only when they encode a real cause, contrast, condition, or conclusion. Split a sentence at an evidence boundary or independent assertion, not at every comma; merge fragments when they jointly discharge one paragraph obligation.
