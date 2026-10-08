# Chinese Systems-Writing Calibration

Use the shared logic in [writing-core.md](writing-core.md).
This reference covers Chinese drafts and Chinese-to-English revision.
Do not use a more ornate or “academic” style only because the source is Chinese.
The English skill instructions use STE rules.
Chinese manuscript examples keep their initial language and scientific meaning.

## Restore technical agency

A Chinese sentence can have no written subject.
A systems claim must make clear who acts and what changes.
Keep these different categories:

- An author choice: `本文比较……` or an equivalent direct expression
- A system action: `Nimbus 合并确认消息……`
- A mechanism property: `页表权限阻止已验证页面被写入……`
- An experimental observation: `实验测得……`.

> **原文：**“Nimbus 对确认消息进行合并操作，将这些确认消息合并为一个批次。”
>
> **去除重复：**“Nimbus 将确认消息合并为一个批次。”

The repair removes repeated words.
It adds no benefit or experiment plan.
Add an omitted actor only when the supplied text identifies that actor without ambiguity.
If that condition does not hold, give the ambiguity in a different issue note.

## Audit each causal arrow

`通过 A，从而 B，进而 C，最终 D` can hide several independent claims.
For each arrow, find its category:

- A mechanism relation
- A design prediction
- An observed result
- An inference without support.

Make dependent steps clear only when the source shows their relation.
Different evidence requirements are findings.
They do not give permission for you to supply missing science.

> **过载：**“系统通过分离元数据和数据，从而避免协调并保证隔离。”
>
> **处理：**保留这句原文，在正文外指出：“分离元数据和数据 → 避免协调并保证隔离”缺少推导或支持。不能自行补入协调协议、页表权限或其他隔离机制，也不能擅自将“保证”改成“可能”。

## Replace proposal shells with technical relations

`针对……问题，提出……方法` and `为了……，设计了……` can name a paper action without explaining the advance.
Examine if the supplied paragraph gives the related technical content:

- Repeated work
- A failed assumption
- A changed boundary
- A new observation.

If that content is missing, give the author a question for that content.
Do not invent an explanation.

> **原文：**“对于每个请求，系统都会重新计算放置决策，即每次请求都要重复计算放置决策。”
>
> **去除重复：**“系统为每个请求重新计算放置决策。”

Prefer a direct technical predicate to stacked nominalizations such as `实现了对……的有效支持`.
Use this repair when the source action is `缓存`、`隔离`、`延迟`、`验证`、`复制` or `限制`.

## Match Chinese verbs to evidence

| Source term | Scientific requirement |
|---|---|
| `观察到`、`测得` | These terms report data. They do not prove a cause by themselves. |
| `表明` | The evidence directly supports a conclusion in its stated scope. |
| `提示`、`可能说明` | The inference keeps plausible alternatives open. |
| `证明` | A valid proof or equally decisive argument exists in the stated model. |
| `保证`、`确保` | An invariant, proof, or exhaustive enforcement exists with clear assumptions. |
| `支持`、`允许` | The capability has a named user, action, and condition. |
| `消除`、`避免` | The claimed absence has a clear scope. |
| `降低`、`移出关键路径` | These terms state different properties. They are not style alternatives. |

Treat these words as claims:

- `高效`、`轻量`、`灵活`
- `可扩展`、`鲁棒`、`安全`
- `显著`、`全面`、`普适`.

Do a check of the supporting property, comparison, and boundary.
If support is missing, keep the affected assertion.
Give the gap independently.
For a claim-strength change, get a clear author decision.

## Keep references and terms clear

Give `该方法`、`该问题`、`其` and `这` one clear local antecedent.
Repetition of the same noun can prevent ambiguity between mechanisms or results.

Use one stable Chinese or English name for each technical concept.
`隔离`、`内存安全`、`故障域` and `访问控制` name different properties.
Keep each term's meaning.

## Translate logic, not word order

Before translation, find these source elements:

- Actor and dominant assertion
- Conditions and logical relation
- Evidence status and boundary.

Write the English sentence around those elements.
Do not copy Chinese topic chains or omitted subjects.

> **中文：**“运行时跨请求缓存解析后的对象，避免稳态路径上的重复解析。”
>
> **保义翻译：**“The runtime caches parsed objects across requests, avoiding repeated parsing on the steady-state path.”

Each technical detail in this translation exists in the source.
A generic source such as “通过缓存中间结果，有效提升了系统性能” does not give permission for new technical details.
Do not add parsed objects, cross-request reuse, or a steady-state path.
Translate the assertion with its initial meaning.
If scientific support stays missing, give a different issue note.

Include measured results only when the author supplies them and the task includes them.
`effectively`、`obviously` and `significantly` cannot supply evidence.

## Keep concise Chinese rhythm

Keep sufficient wording and information order.
If ambiguity or an order defect prevents comprehension, make the controlling relation clear.
Use connectives only for shown relations.
Split or combine sentences only in the initial paragraph.
Keep meaning, emphasis, and manuscript format.
Put a merely preferable rhythm in optional wording.
