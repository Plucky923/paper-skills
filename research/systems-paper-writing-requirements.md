# OSDI、SOSP、EuroSys、USENIX ATC 与 ASPLOS 系统论文写作要求调研

更新日期：2026-09-03

## 结论

这些会议共同要求的不是一种“顶会腔”，而是一条可以被审稿人快速检查的科学论证：

> 一个对目标社区重要的问题，在明确条件下受到某项根本约束；已有方法因此不能满足关键需求；论文提出一个能够解释为何有效的推进；实现、分析和实验分别支撑相应主张；结论不超过证据，并说明代价与边界。

因此，系统论文的 `high-level` 不等于省略细节或使用抽象形容词。真正的高层表述压缩实现细节，但保留问题的决定性约束、方案的设计原则、由原则推导出的机制以及结论成立的边界。简洁也不等于少写：它意味着每一段只承担一个推理义务，每一句都改变读者对问题、原因、方案、证据或边界的理解。

本文使用三类标签，防止把写作经验误写成会议政策：

- **[正式要求]**：当前会议 CFP、投稿说明或官方评估指南明确陈述。
- **[语料观察]**：在本文限定的代表性录用论文中反复出现，但不是录用的必要条件。
- **[写作推导]**：由正式评审义务和语料共同推导出的可执行建议。

## 方法、语料与限制

### 正式规则语料

本文以截至 2026-09-03 可获得的最新官方材料为准：

- [OSDI 2027 preliminary CFP](https://www.usenix.org/conference/osdi27/call-for-papers)，并用已定稿的 [OSDI 2026 CFP](https://www.usenix.org/conference/osdi26/call-for-papers) 补充简洁性和 Operational Systems track 的说明；
- [SOSP 2026 CFP](https://sigops.org/s/conferences/sosp/2026/cfp.html)；
- [EuroSys 2027 CFP](https://2027.eurosys.org/cfp.html)；
- [ASPLOS 2027 CFP](https://www.asplos-conference.org/asplos2027/cfp/)；
- 最后一届 [USENIX ATC 2025 CFP](https://www.usenix.org/conference/atc25/call-for-papers) 及其更具体的 [submission instructions](https://www.usenix.org/conference/atc25/submission-instructions)。

评价实验文字时，本文还采用 ASPLOS 2027 明确引用的 [SIGPLAN Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation/) 及其 checklist，以及 systems artifact evaluation 的 [evaluator guide](https://sysartifacts.github.io/evaluator-guide.html)。关于问题、创新、现实性、经验、设计选择、假设、聚焦和表达的讨论，本文参考 SOSP 9 PC 主席基于当届投稿总结的 [How (and How Not) to Write a Good Systems Paper](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/good_paper.html)；它发表于 1983 年，是重要的历史性一手经验，而不是今天任何会议的正式规则。

### 论文语料

本文建立了一个 **50 篇录用论文的分层目的样本**：每个 venue 10 篇，覆盖 2023–2026 年可由官方 proceedings、会议页面或 DOI 审计的论文。按主标签计，样本含 18 篇 Best Paper、5 篇仅标有 artifact award 的论文和 27 篇在本文核对的官方页面上没有 paper-award 标记的论文；它还覆盖新系统/机制、测量与经验、verification/formalization、benchmark/testing infrastructure、operational system、编译器以及硬件—软件跨层设计。完整清单、来源、贡献类型、奖项状态和逐篇编码见附录。

分析分为两个不混用的层次：

- **摘要编码：50/50 篇。** 只读取论文摘要正文，编码它是否显式承担 `P/G/A/I/E/B` 六种论证动作；标题、奖项和我们对论文类型的判断不用于补全缺失动作。
- **全文级近读：13/50 篇。** 对这 13 篇读取 PDF 的完整 introduction 和段落推进；涉及 design/evaluation 组织的观察再核对相应 overview 或 evaluation 小节，而不是把摘要扩写推断为全文。子集包括 10 篇获奖论文——Ensō、VeriSMo、TreeSLS、Trio、RMMAP、Emme、zpoline、On-demand Container Loading、GIANTSAN、Isaria——以及三篇官方奖项页未列名论文：EuroSys 的 carbon-aware workload shifting、ATC 的 Pecan 和 ASPLOS 的 LLM power-management characterization。附录用“全文”标出这 13 篇。

这里的 award 与“未列名”均按所链接的官方 program/award 页面核对。“未列名”只表示论文没有出现在本文核对的会议奖项页或议程奖项标签中，不证明它没有获得其他荣誉。贡献类型是本文为分层分析所作的归类，不是会议官方 track。

### 摘要编码协议与结果

六个二元代码的单位始终是 **abstract 正文**：

- `P`：明确陈述问题、压力或新的运行环境；
- `G`：明确指出已有方法的局限或产生问题的根因；
- `A`：明确提出方法、系统、分析、抽象或 artifact；
- `I`：解释方法为何可能有效的关键观察、原理或因果桥；组件清单本身不算 insight；
- `E`：报告具体的定性或定量发现；只承诺“将评估”不算；
- `B`：明确限定适用/评估范围、成本、条件、保证范围或局限。这里的 `B` 不只表示负面的 self-criticism。

`1` 表示该动作在摘要中显式可见；`0` **只表示摘要这一固定文本单位没有显式承担该动作**，绝不表示整篇论文没有讨论它。一个句子可以承担多个动作，动作也不必按固定顺序各出现一次。

| Venue | n | P | G | A | I | E | B | 六项均显式出现 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| OSDI | 10 | 9 | 7 | 10 | 10 | 10 | 10 | 7 |
| SOSP | 10 | 10 | 9 | 10 | 8 | 9 | 10 | 7 |
| EuroSys | 10 | 10 | 7 | 10 | 8 | 10 | 10 | 6 |
| USENIX ATC | 10 | 10 | 9 | 10 | 9 | 10 | 10 | 9 |
| ASPLOS | 10 | 10 | 8 | 10 | 8 | 8 | 10 | 6 |
| **合计** | **50** | **49** | **40** | **50** | **43** | **47** | **50** | **35** |

计算规则是逐篇 presence/absence 后求和，分母始终为该行的 `n`。因此总体描述性比例为 `P 49/50`、`G 40/50`、`A 50/50`、`I 43/50`、`E 47/50`、`B 50/50`，六项全部显式出现为 `35/50`。这些数字只支持一个有限观察：在这组分层摘要中，`A`、`P`、`E` 与某种范围限定高频可见，显式 `G` 和 `I` 则并非处处出现；它们不证明某一 move 是录用条件，也不能用于给单篇摘要机械打分。测量、负结果、形式化、生产经验和 characterization 论文合理地偏离 system-building 的 `P → G → A → I → E/B` 轨迹。

### 限制

官方材料几乎不规定段落首尾句、句长、段落句数或具体词汇。本文对这些问题给出的答案属于 13 篇全文近读的定性观察和写作推导，而非 venue policy；50 篇摘要编码不能支撑全文级结论。

50 篇论文是为覆盖 venue、年份、奖项状态和贡献类型而做的目的抽样，不是随机样本；EuroSys 与 ASPLOS 子样本集中于 2024 年，全文近读子集又有意包含 10 篇获奖论文。它们可以暴露不同论证路径和反例，却不能估计录用概率、venue 间差异或“获奖写法”。摘要编码也包含人工判断，本文没有第二位独立编码者，因此不报告 inter-rater reliability；附录公开逐篇 bit vector 以便复核。

本文不报告“顶会段落平均 4.2 句”一类数字。双栏 PDF 的文本抽取会混淆换栏、项目符号、公式和图注，13 篇近读也不足以产生稳定的段落长度分布。虚假的精确阈值会违背本文主张的证据边界；更可靠的密度判断是一个段落是否完成且只完成一个推理义务。

## 五个 venue 的共同评审主线

五会使用的具体措辞不同，但可以恢复出高度相似的评审链。下表的“官方依据”列只陈述逐会可追溯的 criteria；“对文字的约束”列是 **[写作推导]**，不是 CFP 原句，也不意味着每个 venue 对每一行使用相同强度的措辞。

| 可归纳的评审义务 | 官方依据 | 对文字的约束 [写作推导] |
|---|---|---|
| 问题重要且属于目标社区 | OSDI、SOSP 直接使用 significant problem；其余 criteria 也考察 relevance、interest、impact 或 practical value | 摘要与引言应说明现状在什么条件下不能满足什么需求，以及后果为何值得目标社区关注；技术趋势本身不是问题。 |
| 推进相对既有工作可辨认 | 逐会核对的五份 criteria 都包含 originality/novelty、significance，或相对 prior work 的 identifiable advance | “我们实现了一个系统”本身不是贡献。应指出旧方法受什么约束，新工作改变了哪项能力、保证、成本或适用范围。 |
| 方案有技术根据 | OSDI/SOSP 评价 compelling solution；EuroSys 评价 interesting solution；ASPLOS 评价 practical approach that makes sense；ATC 评价 novel practical solution | Design 不能只是组件清单。每个主要机制应回指一个已陈述的需求或障碍，并解释机制为何改变结果。 |
| 实现与证据对应主张 | OSDI/SOSP 评价 practicality and benefits；EuroSys 直接要求 rigorous evaluation；ASPLOS 要求 sound empirical methods；ATC 要求 implementation 与 experimental results | 先定义需要回答的主张，再决定实验、证明或经验材料；一个性能数字不能代替正确性、因果归属、资源成本或适用范围的证据。 |
| 报告代价和边界 | EuroSys 直接列出 benefits、limitations 和相对优势；ASPLOS 与 ATC 直接列出 pros、cons、实现状态并要求避免 overclaim；其他 venue 的具体措辞不完全相同 | 高层结论仍应保留成立条件。只写收益而不交代会改变结论的资源、假设、失败模式或未实现部分，会使论证无法闭合。 |
| 论文正文独立成立 | 本文核对的投稿说明均不保证审稿人阅读 supplementary material | 贡献、关键设计理由、主要方法和决定性证据不应依赖可选附录才能成立。 |
| 清晰与简洁属于可评价质量 | Clarity 在逐会 criteria 中反复出现；OSDI 2026 要求下调 padded papers，ASPLOS 2027 说明审稿人重视 conciseness 且不必写满页数 | 没有推进问题、推理、证据、边界或必要导航的句子应删除；篇幅上限不是必须写满的目标。 |

上述共同链条直接来自 [OSDI 2027](https://www.usenix.org/conference/osdi27/call-for-papers)、[SOSP 2026](https://sigops.org/s/conferences/sosp/2026/cfp.html)、[EuroSys 2027](https://2027.eurosys.org/cfp.html)、[ASPLOS 2027](https://www.asplos-conference.org/asplos2027/cfp/) 和 [ATC 2025](https://www.usenix.org/conference/atc25/submission-instructions) 的评审标准。它不是要求所有论文采用同一章节顺序。测量论文可以采用“未知现象—方法—观察—影响”，验证论文可以采用“证明障碍—新抽象—可靠性论证—适用范围”，benchmark 论文可以采用“测量缺口—构造原则—覆盖性—用它重审既有结论”。不同类型改变论证对象，不改变主张必须可辨认且被恰当证据支持的要求。

**[写作推导]** Artifact evaluation 进一步要求论文文字与实际 artifact 对齐，但不应被外推为五会统一的录用条件：这些流程通常是 optional、发生在论文决定之后，且不同 venue/年份评估的 badge 不同。只要论文选择公开 artifact，`implemented`、`automatic`、`end-to-end`、`reproduces` 等词就应与代码覆盖范围、人工步骤、实验配置和实际复现范围一致。[Systems Research Artifacts evaluator guide](https://sysartifacts.github.io/evaluator-guide.html) [OSDI 2026 artifact call](https://www.usenix.org/conference/osdi26/call-for-artifacts)

## Venue-specific emphasis

| Venue | 当前正式重点 | 对写作的含义 |
|---|---|---|
| OSDI | 创新系统研究以及量化或有洞察力的系统经验；潜在影响未来系统研究或实践，并能引起相当部分 OSDI 读者兴趣。面向 ML 等新领域的工作还必须接入 systems prior work、与已有系统技术比较，并说明新场景产生了什么新的 systems challenge。[OSDI 2027 CFP](https://www.usenix.org/conference/osdi27/call-for-papers) | Introduction 要把应用目标翻译成系统问题，不能只报告领域指标更好。Research track 强调原创推进；Operational Systems track 可以不提出新算法，但应通过部署、反例、新规模验证或经验增加公共系统知识。 |
| SOSP | 偏好探索新领域、推进重要研究对话，或从先进实现、部署和测量中获得洞察；正式范围覆盖 design、implementation、analysis、evaluation 和 deployment。[SOSP 2026 CFP](https://sigops.org/s/conferences/sosp/2026/cfp.html) | “Principles” 不是要求每篇论文写成理论论文。更稳妥的目标是让具体系统产生可迁移的 insight，并让非狭窄子领域读者理解其重要性、机制和边界。 |
| EuroSys | 评价必须清楚展示方案的收益、限制及相对 prior work 的优势。Experience paper 的 lesson 必须可推广、有严格定量分析支持且对社区有用。[EuroSys 2027 CFP](https://2027.eurosys.org/cfp.html) | Evaluation 不是优势展示区，而是收益—成本—边界的闭合论证。部署规模不能自动转化为贡献；论文必须提炼其他系统在什么条件下能够复用的知识。 |
| ASPLOS | 必须对四类 conference pillar 至少一类作出实质贡献：architecture、operating systems、programming languages，或引入 entirely new domains；第四类仍须与前三个核心知识域中的至少一个具有实质联系。仅仅使用某一 pillar 的技术不等于推进它。官方还要求展示 pros/cons、披露已实现和未实现部分、避免 overclaim，并遵循 SIGPLAN empirical guidelines。[ASPLOS 2027 CFP](https://www.asplos-conference.org/asplos2027/cfp/) | 跨层论文应说明每一层为何不可被局部替代，以及跨层协同如何因果地产生结果。2027 rapid review 只读前两页且要求它们自包含，因此前两页必须交付问题、相对推进、核心方法和可信度预览。 |
| USENIX ATC | 2025 正式标准强调 implementation、experimental results、practical solution、pros/cons、统计方法及明确披露实现范围；short paper 与 full paper 的评审标准相同，只是 scope 更小。[ATC 2025 instructions](https://www.usenix.org/conference/atc25/submission-instructions) | ATC 的历史风格允许工程和部署贡献，但绝不降低完整性或证据标准。它适合作为 production pragmatism 的写作参照，而不是当前投稿目标。 |

USENIX 已宣布 [ATC 在 2025 年后终止](https://www.usenix.org/blog/usenix-atc-announcement)，所以本文只把它作为历史写作传统。OSDI 2027 的 CFP 目前仍是 preliminary：可能只读前几页的 early review 尚未最终确定；不能把它写成既定规则。与之不同，ASPLOS 2027 的两页 rapid review 已经明确生效。

## “High-level” 的可执行定义

### 高层不是空泛，而是保留因果骨架

**[写作推导]** 一个合格的高层表述至少回答四件事：

1. **对象与条件**：哪个系统、工作负载、故障模型或执行阶段？
2. **决定性约束**：为什么已有做法在这个条件下失败？
3. **设计原则**：论文改变了哪条边界、依赖关系或控制位置？
4. **可推导后果**：这个改变为什么带来某项能力，同时留下什么代价或假设？

可以用四个测试检查一句话是否真的 high-level：

- **推导测试**：从这句话能否预测至少一个主要设计选择？若不能，它可能只是口号。
- **区分测试**：把系统名替换成同领域任意系统后，句子是否仍成立？若成立，它没有表达本文的推进。
- **反驳测试**：什么条件或反例会使句子不成立？若无法回答，主张通常不可证伪或边界缺失。
- **证据测试**：论文中的哪项分析、证明或实验支撑这句话？若找不到，它只是愿望。

下面的英文句子均为本文自造的假想例子，不描述某篇真实论文：

> **Bad — generic:** “Nimbus provides a flexible and efficient architecture for resource management.”
>
> **Bad — low-level inventory:** “Nimbus has a monitor thread, two queues, a bitmap, and three RPC handlers.”
>
> **Better — high-level and causal:** “Nimbus moves admission control off the request path, so each request avoids a centralized scheduling decision; this reduces coordination at the cost of reacting more slowly to load changes.”

第三句没有给出函数或数据结构，却保留了机制位置、因果关系和代价。这才是系统论文所需的抽象。

### Principle、mechanism 与 implementation detail 不可混写

- **Principle** 表达决定设计空间的关系，例如“将检查移到加载阶段，可以让稳态调用省去重复验证，但前提是已验证代码之后不可变化”。
- **Mechanism** 说明系统如何实现该原则，例如“加载器验证代码页并在映射后撤销写权限”。
- **Implementation detail** 说明具体工程实现，例如数据结构、函数、批量大小和线程布局。

高层段落应先让 principle 成立，再给足够 mechanism 使读者相信它不是口号；只有会影响正确性、性能、可部署性或复现性的 implementation detail 才进入正文。历史性的 SOSP 写作总结同样强调：系统论文不应把所有组件等深描述，而应聚焦新颖或异常且支撑主线的部分；好论文不仅描述选择，还解释为什么这样选择以及实际结果是否符合原始理由。[Levin and Redell](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/good_paper.html)

## 整篇论文的论证结构

### 同时为两层读者写作

**[写作推导]** 顶级系统会议的论文同时面对两种阅读深度，而不是两类互斥读者：

- **第一层：快速做去留判断的 broad systems reader。** 这位读者首先看到 title、abstract、introduction、overview figure、主要结果和 conclusion，需要迅速恢复问题为何重要、相对推进是什么、方法为何可信以及结论有多强。
- **第二层：验证技术成立性的 domain expert。** 这位读者会追踪模型、假设、语义、invariant、corner case、baseline、实验配置与统计，检查第一层叙事是否被真正兑现。

论文不能通过“简化版叙事”和“技术版正文”讲两个不同故事。更有效的组织是逐层展开同一条 claim：段落首句和图注先给可检查的高层判断，随后提供使专家能够验证该判断的机制与证据。第一层负责可发现性，第二层负责可信度。

ASPLOS 2027 的前两页 rapid review 使第一层成为正式筛选界面；对其他 venue，把前两页当作压力测试仍然有价值，但不是它们当前全部采用的硬规则。OSDI 2027 只说明可能引入类似初筛，最终规则仍待更新。[ASPLOS 2027 CFP](https://www.asplos-conference.org/asplos2027/cfp/) [OSDI 2027 preliminary CFP](https://www.usenix.org/conference/osdi27/call-for-papers)

### 先确定贡献类型，再确定叙事

**[语料观察]** 全文近读论文并不服从一个模板。Trio 围绕 NVM userspace file system 中性能、定制和 metadata integrity 的张力推导 state separation；EuroSys 的 carbon-aware workload-shifting 论文先建立并反驳一个广泛前提，主要贡献是有边界的负结果；Isaria 从反复手工构建 DSP vectorizer 的成本推导 compiler generation；AWS Lambda 的论文则以生产规模、SLO 和长期运行事实作为 operational evidence。它们共有的是论证闭合，而不是段落数量。

建议先选择最接近的主贡献类型：

| 类型 | 必须闭合的主链 |
|---|---|
| 新系统或机制 | problem → root constraint → principle → mechanism → implementation reality → benefit/cost evidence |
| 测量或经验 | consequential blind spot → trustworthy method/data → observations → causal restraint → transferable implications |
| 形式化或分析方法 | property/analysis obstacle → new abstraction or method → soundness/precision argument → practical applicability → assumptions |
| Benchmark 或基础设施 | measurement deficit → principled construction → coverage/representativeness → reproducibility → conclusions newly enabled |
| Operational/experience | deployed condition → surprising failure or lesson → analysis → intervention/validation → scope of transfer |

若论文同时声称多种贡献，应有一个统领 thesis；否则读者会看到多个并列项目，而看不到它们为何共同回答一个问题。

### Claim—reason—evidence—boundary

**[写作推导]** 全文可以维护一张内部表，而不必把表放进论文：

| Claim | Why it should hold | Evidence required | Boundary |
|---|---|---|---|
| 核心能力/正确性 | invariant、算法或架构因果链 | proof、analysis、test、fault injection | failure model、trusted component、unsupported case |
| 性能/资源收益 | 移除了哪项工作或改变了哪条关键路径 | fair baseline、end-to-end metric、variance | workload、hardware、load region |
| 可扩展性 | 哪个共享状态或串行点不再随规模增长 | scale-out/scale-up experiment、bottleneck analysis | topology、capacity、coordination regime |
| 通用 lesson | 观察由什么稳定机制产生 | diverse cases、counterexamples、sensitivity | population and transfer assumptions |

SIGPLAN checklist 明确要求 claim 可见且适当限定、比较公平、benchmark 选择有原则、指标直接相关、统计与分布恰当、配置足以重复，并承认真正影响结论的限制。[Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation/) 因此，写作不能在实验完成后才为图表寻找故事；evaluation question 必须从 claim 推导。

## 各章节应完成什么

### Title

Title 应让目标读者识别研究对象和核心推进，而不是先解码品牌名。系统名可以建立记忆点，但副标题或其余词语应说明新的 abstraction、property、trade-off 或作用域。

> **Weak:** “Nimbus: A Novel and Efficient Framework”
>
> **Stronger:** “Nimbus: Decoupling Admission from Placement in Distributed Schedulers”

第二个 title 没有预先宣称尚未证明的性能，却明确了论文改变的技术关系。`First`、`Scalable`、`Practical`、`Secure` 等词只有在正文能够给出相应范围与证据时才应进入标题。标题不应比结论更强。

Title 还必须服从投稿 track 的正式命名要求。例如 OSDI 2027 要求 Operational Systems track 的标题以 `(Operational Systems)` 结尾；这属于 venue-specific 格式，不能推广为普通标题规则。[OSDI 2027 preliminary CFP](https://www.usenix.org/conference/osdi27/call-for-papers)

### Abstract

Abstract 应是技术论证的最小闭包，而不是章节目录。它通常需要让读者恢复以下信息，但不要求固定五句话：

1. 问题与重要性；
2. 现有方法的决定性限制；
3. 核心 insight 或相对推进；
4. 实际构建或研究的方法；
5. 最强证据及其比较对象和范围；
6. 必要时说明关键边界。

**[语料观察]** 50 篇摘要的编码表明 `A` 在 `50/50` 中显式出现，但只有 `35/50` 同时显式完成六项动作。Basilisk 先定义证明工作中的具体障碍，再给出相互支撑的 provenance 与 atomic-sharding 洞见，最后报告多种协议上的结果；carbon-aware workload shifting 则以数据和负结果挑战一个既有前提，并不需要伪造 system-building 式的“solution mechanism”。这说明 abstract 的单位是论证义务，而不是模板句位。

> **Bad:** “We present Nimbus, a novel and efficient system. Section 2 gives the design, and Section 3 evaluates it.”
>
> **Better:** “Existing schedulers serialize admission and placement, so request bursts contend on one global decision path. Nimbus separates the two decisions and admits requests from replicated local state; experiments compare the resulting latency and imbalance against the centralized baseline.”

第二个版本仍需替换为论文的真实条件和结果，但已经提供问题、原因、设计和证据关系。

### Introduction

Introduction 必须在读者进入实现细节之前完成“为什么这篇论文值得继续读”的证明。一个常见但非固定的依赖顺序是：

1. 定义实际问题和 stakes；
2. 用事实或小例子证明问题存在；
3. 找到已有方法失败的 root cause，而不仅是列出缺点；
4. 陈述关键 insight：改变哪项假设、边界或控制位置；
5. 从 insight 推导主要 design challenges 和机制；
6. 说明实现真实程度；
7. 预览证据、代价、边界与贡献。

这些步骤可以合并、重排或按论文类型替换，但因果依赖不能倒置。若读者尚不知道问题和约束，组件名称没有意义；若尚不知道主张，实验数字也没有解释对象。

ASPLOS 2027 已确定只阅读前两页的 rapid review，并明确要求前两页自包含；OSDI 2027 也在考虑类似初筛但尚未确定。[ASPLOS 2027 CFP](https://www.asplos-conference.org/asplos2027/cfp/) [OSDI 2027 preliminary CFP](https://www.usenix.org/conference/osdi27/call-for-papers) 即使不为某个 venue 投稿，这也是有用的压力测试：读者只读 title、abstract、introduction 前半部分，能否准确说出 problem、delta、insight、system reality 和 evidence plan？

Contribution list 应列知识增量，而不是工作日志：新的 insight/abstraction、由此产生的系统或方法、以及验证该推进的证据。`We implemented 12K lines of code` 可以证明投入或现实性，却通常不是独立的 scientific contribution。

### Background 与 motivation

只保留主论证依赖的背景。每个背景段应回答“读者必须知道什么，才能理解下一项限制或设计选择？”术语在首次承担推理作用前定义；不要先让读者记住一个尚无语义的名字，再承诺后文解释。历史 SOSP 写作总结明确批评无关背景、只描述解法却要求读者猜问题，以及在术语定义前大量前向引用。[Levin and Redell](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/good_paper.html)

Motivation 不能用人为弱化的 baseline 制造 gap。应先给现象，再定位原因，最后把原因转化为 design requirement：

> **Observation:** “Queueing delay rises after the eighth worker.”
>
> **Root cause:** “All workers still acquire the same admission lock.”
>
> **Requirement:** “Admission must not serialize on worker count.”

三句话分别是数据、解释和设计义务，不能互相替代。

### Design overview

Overview 的任务是让读者看到因果架构，而不是提前列完所有模块。它应说明：

- 哪些 requirements 来自前文的障碍；
- 每项 requirement 由哪个 principle/mechanism 满足；
- 数据、控制或信任边界怎样连接；
- 最重要的 invariant 或 trade-off 是什么；
- 后续小节为什么按当前顺序展开。

一个有效的 overview figure 也应表达依赖关系、边界或状态变化，而不只是方框数量。正文必须能够指出 figure 中哪条路径支撑哪项主张。

### Design/implementation subsection

每个小节聚焦一个 design question。推荐的解释次序是 `why → what → how → consequence/boundary`：

1. 首段定义局部障碍或 invariant；
2. 解释设计选择及被放弃的可行替代；
3. 描述足以验证因果链和正确性的操作；
4. 说明该机制解决了什么、没有解决什么、付出什么；
5. 仅在影响主张时给出实现参数。

> **Bad:** “The controller consists of a detector, a manager, a queue, and a cache.”
>
> **Better:** “The controller must distinguish persistent overload from transient bursts without delaying the request path. It therefore records local queue transitions on the fast path and performs classification asynchronously; the next subsection explains how stale observations bound its reaction time.”

第一句是物料清单；第二组句子给出 requirement、机制位置、原因和待解释边界。

### Evaluation

Evaluation 应被组织成对主张的审问，而不是运行实验的时间顺序。核心问题通常包括：

- **End-to-end:** 整体上是否实现 headline benefit？
- **Attribution:** 收益确实来自声称的机制吗？
- **Cost:** CPU、内存、网络、能耗、复杂度或准确性代价是什么？
- **Robustness:** 在工作负载、规模、硬件、故障和参数变化时是否仍成立？
- **Comparison:** baseline 是否当前、配置公平且比较的是同一目标？
- **Correctness/reality:** 实现了什么，如何检查安全、语义或容错主张？
- **Limit:** 在哪里不再有效，为什么？

每个 evaluation subsection 和段落应先提出问题或 claim，再交代必要控制条件，随后报告结果，最后解释结果对 claim 的支持强度和边界。不要只写 `up to` 峰值；不要把 proxy metric 当作端到端结论；不要用均值隐藏分布；不要把相关性写成机制因果。以上风险均与 SIGPLAN checklist 的明确项目一致。[checklist](https://raw.githubusercontent.com/SIGPLAN/empirical-evaluation/master/checklist/checklist.pdf)

> **Bad:** “Nimbus is 2× faster and therefore scalable.”
>
> **Better:** “At 80% offered load on the evaluated cluster, Nimbus doubles throughput relative to Baseline B while median latency remains unchanged. This result supports the throughput claim for this load range; it does not establish scale-out beyond the tested cluster.”

这是一个假想例子。改进点不在句子更长，而在比较对象、条件、指标和推论边界均可审查。

### Figures、tables 与 captions

图表是论证节点，不是版面装饰。放入任何 figure/table 前，应能补全一句话：`读者看完它以后，应相信 ______`。若只能回答“了解系统结构”或“看到实验结果”，图表的任务仍不够具体。

不同图表承担不同推理：

- **Motivating figure**：证明问题存在并标出转折区间、比较对象和条件；不能只选最有利的数据点。
- **Architecture figure**：展示 data/control/trust boundary、关键状态以及机制间依赖；避免所有方框等权，使核心 insight 消失。
- **Protocol/timeline figure**：让事件顺序、并发关系、failure point 和 invariant 可见；正文解释“为何这样排序”，而不逐箭头朗读。
- **Evaluation plot**：标明 axes、units、baseline、normalization、样本/误差和 better direction；视觉强调不能超过数据差异。
- **Comparison table**：每列使用同一语义和抽象层级；`✓` 必须有明确判定标准，不能把部分支持写成完全支持。

Caption 应使 broad reader 在不搜索正文的情况下理解三件事：图中是什么、比较/设置是什么、主要 takeaway 及必要边界是什么。caption 不能承担正文从未建立的新 claim，也不能用 `Results for experiment 3` 代替结论。

> **Weak caption:** “Performance comparison of all systems.”
>
> **Stronger caption:** “Throughput as clients increase on the evaluated 32-core server. Nimbus removes the centralized bottleneck through 24 clients; all systems saturate the same network link beyond that point.”

后者是本文自造例子，包含坐标语义、环境、主结论和饱和边界。正文仍需解释原因、配置和不确定性。

本文核对的 OSDI、SOSP 和 EuroSys 当前格式说明都要求图表无需放大即可阅读，并在灰度打印时保持可辨认；这意味着不能只依赖颜色编码，也不能通过缩小字体把次要实验塞入正文。[OSDI 2027](https://www.usenix.org/conference/osdi27/call-for-papers) [SOSP 2026](https://sigops.org/s/conferences/sosp/2026/cfp.html) [EuroSys 2027](https://2027.eurosys.org/cfp.html)

### Related work

Related work 的职责是定位 delta，而不是逐篇摘要。围绕决定性轴比较：assumption、mechanism、guarantee、deployment condition、cost 或 evidence。自己的 prior work 仍应按目标 venue 的匿名说明正常引用和比较；双盲不是删除它的理由。不同 venue/年份对第一或第三人称、自引措辞和已公开版本的处理并不完全相同，因此提交前必须读取当年规则，不能把某一会的句法要求外推成五会共同规则。

若相关工作是理解 gap 的必要前提，可在 introduction/motivation 中提前比较；若主要作用是完整定位，可集中在后部。不存在适用于所有论文的固定位置。

### Limitations 与 conclusion

Limitations 不应收集无关紧要的免责声明，而应披露最可能改变核心结论的条件：failure model、trusted base、unsupported workload、scale boundary、manual step、approximation 或 external validity。SIGPLAN 指南特别说明，真正重要的是清楚限定 claim，而不是机械加入一个标题为 threats to validity 的段落。[Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation/)

Conclusion 应重申已经由正文建立的 thesis、最可迁移的 insight 及其边界，不引入新机制、新数字或未经验证的愿景。它不是 abstract 的同义改写，也不必用 `In the future, we plan to...` 稀释最后的科学结论。

## 每一种段落应怎样写

### 段落是一个 inference unit

**[写作推导]** 一个段落应完成一个 reader obligation：读者进入段落时有一个具体问题，离开时得到一个可用于下一步推理的答案。典型内部结构是：

1. **Opening claim/question**：首句声明本段要建立的判断，而不是只宣布主题；
2. **Development**：给原因、机制、定义、证据或必要对比；
3. **Payoff/boundary**：末句交付结论、设计义务、限制或下一步逻辑前提。

这不是“每段必须三句”。两句可以完成一个简单对比，较长段落可以推导复杂 invariant。判断长度的标准是推理边界：当句子开始支撑另一个独立结论、改变抽象层级，或转向新的 evidence question 时，应另起一段；若连续的单句段落各自不能形成推理，则应合并。

**[语料观察]** 13 篇全文近读同时出现短段和长段，获奖与普通录用论文都没有稳定的句数模式。Pecan 常用段首的 `However`、研究问题或 `We have two main insights` 标出角色变化；carbon-aware workload shifting 要用数段先建立再推翻一个广泛前提，因而比 artifact-first 论文更晚交付答案；LLM power-management characterization 甚至显式使用 `Motivation`、`Our work` 和 `Summary` 引导角色。首句和末句的权重来自它们对局部推理边界的暴露，而非固定句法：成熟段落有时先用第一句承接上文，再在第二句交付局部 claim；真正的标准是读者能否迅速知道本段为何存在，并在段尾得到可继续使用的判断。

| 段落角色 | 首句应该交付 | 中部应该包含 | 末句应该交付 |
|---|---|---|---|
| Problem | 在何种条件下，现状不能满足哪项需求 | 影响、规模、可信现象 | 为什么这形成研究义务 |
| Prior limitation | 最决定性的现有局限 | 局限的因果来源及公平对比 | 尚未满足的 design requirement |
| Insight | 改变问题的关键观察或重构 | 从约束到原则的推导 | 由此必须采用的机制方向 |
| Overview | 系统如何从总体上实现 thesis | 组件间的因果链、边界、invariant | 核心保证或显式 trade-off |
| Mechanism | 本段解决的局部问题 | 操作、状态变化、替代选择 | 该机制建立的 property 与条件 |
| Evidence | 本段回答的 claim/RQ | 设置、比较、结果和不确定性 | 结果支持什么、不支持什么 |
| Limitation | 哪个条件未被覆盖 | 失败原因或实际影响 | 主结论应如何收窄 |
| Transition | 上一结论产生的下一个问题 | 仅在必要时补充桥接事实 | 下一节的具体义务，而非空导航 |

首句不应是 `This section discusses...`，因为它没有建立判断；末句不应只是 `We describe this mechanism next`，因为它没有解释为什么下一步必要。

> **Weak opening:** “There are several challenges in distributed scheduling.”
>
> **Stronger opening:** “Replicating the scheduler removes a single processing bottleneck but creates inconsistent admission decisions.”
>
> **Weak ending:** “The next section presents our admission protocol.”
>
> **Stronger ending:** “The protocol must therefore coordinate admission without restoring a per-request global decision point.”

第二个 ending 同时总结本段结论并形成下一段的技术义务。

### 段落长度与密度

不设置固定句数、词数或双栏高度。用以下信号诊断：

- **过密**：首句提出 A，但中间同时证明 A、介绍机制 B、报告实验 C，末句又转向限制 D；读者无法为段落命名一个判断。
- **过碎**：连续段落只有背景事实、单个数字或空洞转折，任何一段都没有 claim—support—payoff。
- **层级跳跃**：一句讨论架构原则，下一句突然进入结构体字段，随后又回到系统目标。
- **引用堆积**：整段主要是系统名和 citation，却没有比较轴或作者自己的推论。
- **压缩过度**：为了短而删除成立条件、因果桥或证据范围，使句子听起来有力但无法审查。

最实用的测试是给每段写一个边注：`本段使读者相信 ______，因为 ______`。若空格需要两个 `and` 才能填完，应考虑拆分；若无法填写，本段可能没有论证功能。

## 句子组织与信息结构

### 一句承载一个 dominant assertion

一句可以包含条件、原因和限定，但只能有一个主导断言。若一句同时提出问题、批评 prior work、介绍系统并宣称结果，读者无法判断哪项信息支配其余信息。

> **Bad:** “Because existing schedulers use global state and workloads are bursty, which causes contention, Nimbus uses replication and is faster and more scalable.”
>
> **Better:** “Existing schedulers serialize updates to global admission state, so bursts create a shared contention point. Nimbus replicates admission state to remove that point. The evaluation separately tests throughput and decision inconsistency as the worker count grows.”

拆分不是为了追求短句，而是让 cause、design 和 evidence 各自承担可验证责任。

### 主语应暴露技术责任

- 作者作出研究或实验选择时可以用 `we`：`We compare Nimbus with...`。
- 系统或机制执行动作时让它作主语：`Nimbus batches acknowledgments...`。
- 结果或约束比执行者更重要时可以使用被动：`Requests are dropped only after...`。

不要机械禁止 `we` 或被动语态。选择标准是读者能否立即知道“谁做了什么，作用于什么”。形式感来自责任清晰，而不是更复杂的语法。

### 先放已知锚点，再放新增信息

句首连接上一句已经建立的对象，句末承载本句希望读者保留的新信息。下一句再以前一句的新信息为锚点，形成链式推进。避免在主语和谓语之间插入长串修饰，也避免裸 `This`：写 `This serialization point`、`This invariant` 或 `This result`，明确指代对象。

> **Weaker:** “This, under workloads with skewed arrivals and when the cache is full, causes it to become inefficient.”
>
> **Stronger:** “When the cache is full, skewed arrivals repeatedly evict hot entries. This churn increases miss-handling work.”

### 并列必须处于同一抽象层级

`Our contributions are a new invariant, an implementation in Rust, and 38% lower latency` 混合了知识、工程物和结果。更精确的组织是分别说明：提出什么概念、构建什么系统来实现它、用什么证据验证什么主张。项目符号也不能替代这些关系。

### 连接词只能标记真实逻辑

`however` 是对比或让步，`therefore/thus` 是可由前提推出的结果，`because` 是原因，`while/whereas` 是受控对照。不要为了“像论文”而增加连接词；若前后句没有真实关系，`Moreover` 不能把它们变成论证。

> **Bad:** “The cache is distributed. Therefore, the implementation uses Rust.”
>
> **Better:** “The cache is distributed, so eviction decisions use stale local state. The protocol therefore bounds how long an entry can remain locally visible.”

## 用词：技术关系与证据强度必须匹配

### 动词不是同义替换

| 词 | 可以表达 | 使用前必须回答 |
|---|---|---|
| `implements` | 已构建某个设计或接口 | 哪些部分真实存在，哪些模拟或未实现？ |
| `enforces` | 机制主动使约束成立 | 约束是什么，绕过路径是否存在？ |
| `guarantees/ensures` | 在明确假设下性质必然成立 | proof、invariant 或穷尽性依据在哪里？ |
| `provides` | 对外暴露能力或性质 | 谁可以使用，具体能力是什么？ |
| `permits/allows` | 规则不再禁止某动作 | 可行不等于自动发生，条件是什么？ |
| `enables` | 移除一个原本阻止目标的必要障碍 | 被移除的障碍和新增能力分别是什么？ |
| `avoids/eliminates` | 某项操作不再发生 | 是完全为零，还是只离开 fast path/常见路径？ |
| `reduces` | 可测数量下降 | metric、baseline、条件和幅度是什么？ |
| `bounds` | 给出上界或下界 | bound 的变量、模型和证明依据是什么？ |
| `shows/demonstrates` | 证据直接支持结论 | 证据覆盖范围足以支撑多强的词？ |
| `suggests/indicates` | 有限证据支持较弱推断 | 不确定性和替代解释是什么？ |
| `observes/measures` | 报告现象或数据 | 不应悄悄升级为因果结论。 |

> **Overclaim:** “Our prototype guarantees scalable performance.”
>
> **Bounded:** “The prototype maintains throughput through 64 evaluated workers; the experiment does not test multi-machine scaling.”

> **Vague:** “Nimbus enables efficient communication.”
>
> **Precise:** “Nimbus coalesces acknowledgments before crossing the process boundary, reducing crossings per completed request.”

### 高风险形容词和量词

- `novel/first`：需要系统性的 related-work 边界；最好直接陈述具体 delta，让新颖性可检查。
- `efficient/lightweight/scalable/practical`：必须绑定 metric、baseline、规模或可接受成本。
- `significant`：若指统计显著性，给方法；若指工程意义，给 effect size 和语境；若只是强调，删除。
- `optimal`：需要明确 objective、constraint 和 proof；搜索到最优配置不等于机制普遍最优。
- `all/always/never/eliminates`：需要穷尽范围；多数实验只支持 `across the evaluated...`。
- `fundamental/inherent`：应来自模型、下界或不可避免的 trade-off，而不是当前实现的瓶颈。
- `robust/general`：列出变化维度和未覆盖总体，不以少数 workload 代替普遍性。

量词和条件应靠近被限定的 claim：`under crash-stop failures`、`for read-dominated workloads`、`on the evaluated GPUs`。不要把关键限定延迟到数页后的 limitations。

### 术语稳定比词汇变化重要

同一个技术概念应使用同一个词。`isolation`、`memory safety`、`fault containment` 和 `resource isolation` 不是为了避免重复而可轮换的近义词；它们承诺不同性质。类似地，`latency` 必须说明 end-to-end、service time、median 或 tail，`throughput` 不等于 capacity，`policy` 不等于 mechanism，`interface` 不等于 implementation。

优先使用具体动作动词：`places`、`moves`、`partitions`、`serializes`、`replicates`、`maps`、`validates`、`caches`、`defers`、`coalesces`。`supports`、`handles`、`leverages`、`addresses`、`improves` 本身通常不足以说明技术关系。

## 中文技术写作及中译英

中文草稿同样必须保存 claim、condition、cause、evidence 和 boundary，不能把这些责任推迟到英文润色阶段。中文技术写作常见问题不是“不够正式”，而是主语省略、因果链压缩和抽象名词堆叠。

### 恢复明确主语和动作

中文允许依靠语境省略主语，但论文中的技术责任不能省略。明确是作者选择、系统执行、机制保证，还是实验观察。

> **较弱：**“通过批处理减少了开销，并提高了可扩展性。”
>
> **较强：**“Nimbus 将每个请求的确认合并为批量确认，从而减少跨进程通知次数；实验进一步检查该收益是否随客户端数量保持。”

前一句没有说明谁批处理什么、开销是什么，也把机制预测和实验结论混在一起。

### 拆开过长的“通过—从而—进而”链

`通过 A，从而 B，进而 C，最终 D` 常把多个尚未证明的因果关系包装成一句。每个箭头都应单独检查：A 是否足以导致 B？B 是观察还是假设？C 是否还依赖其他机制？必要时拆成两到三句，并在 evaluation 中分别验证。

> **较弱：**“系统通过分离元数据和数据，从而避免协调并进一步保证隔离。”
>
> **较强：**“系统将共享元数据与私有数据分离。该边界使元数据更新仍可协调，而私有数据无需进入共同协议。隔离性另外依赖页表权限保持这一边界。”

改写后，性能关系和安全关系不再被同一个 `从而` 错误合并。

### 避免“针对……问题，提出……方法”的空壳句式

这类句式只有论文动作，没有技术内容：

> **较弱：**“针对现有方法效率低的问题，本文提出了一种高效、灵活的优化框架。”
>
> **较强：**“现有方法在每次请求上重新计算全局放置决策，导致调度成本随集群规模增长。Nimbus 复用局部有效的决策，仅在负载越过分区边界时重新协调。”

后者把“效率低”还原为具体重复工作，把“高效”还原为被移除的成本，并给出机制触发条件。

### 中文动词同样编码证据强度

- `观察到/测得` 报告数据，不等于 `证明` 原因；
- `表明` 适合证据直接支持的有界结论，`提示/说明可能` 适合仍有替代解释的推断；
- `保证/确保` 需要模型、invariant 或完整验证，`支持/允许` 只表示能力；
- `消除/避免` 声称目标在范围内不再出现，`降低/移出关键路径` 是更窄的关系；
- `适用于所有/始终/完全` 需要穷尽性依据，实验通常只能支持“在所评估的……中”。

### 指代宁可轻微重复，也不要歧义

少用无法唯一解析的“该方法”“该问题”“其”“这”。`这一全局锁`、`该测量结果`、`上述 crash-stop 假设` 比裸指代更可靠。同一概念保持同一名称，不要为避免中文重复而在“隔离”“安全”“保护”“封装”之间任意轮换。

### 中译英应翻译逻辑，而不是复制语序

先为中文句子标注主张类型和逻辑关系，再重组英文信息结构。中文原句若包含被省略的主语或含混的 `从而`，逐词翻译只会把歧义搬到英文。

> **中文原句：**“通过缓存中间结果，有效提升了系统性能。”
>
> **机械翻译：**“By caching intermediate results, the system performance is effectively improved.”
>
> **逻辑重写：**“The runtime caches parsed objects across requests, avoiding repeated parsing on the steady-state path.”

若有真实实验，下一句再单独报告 metric、baseline 和条件。不要用 `effectively`、`obviously` 或 `significantly` 替代它们。

## 逻辑精度

### 区分事实、解释和结论

> `Latency rises after eight workers` 是观察。
>
> `A shared lock causes the rise` 是因果解释。
>
> `Replicating the lock removes the bottleneck` 是设计预测。
>
> `The system scales` 是范围更广的结论。

四者需要不同证据。时间相关曲线不能单独证明共享锁是原因；去掉锁后的 ablation 可以增强因果归属，但仍不能证明所有规模和工作负载下都可扩展。

### 区分 necessary 与 sufficient

`X requires Y` 声称 Y 是必要条件；`Y guarantees X` 声称 Y 在相应条件下足够；`Y helps X` 只表达弱关系。系统论文常见逻辑错误是从“我们的机制具有 Y 且观察到 X”跳到“Y 足以产生 X”，却没有隔离其他机制。

### 比较必须保持问题等价

公平比较不仅要求相同硬件，还要求目标、语义、容错、准确性、资源预算和调优机会相称。若系统通过放宽一致性提高性能，句子应把语义差异写进结果，而不是只写速度优势。EuroSys 和 ASPLOS 的正式要求尤其明确要求 pros/cons、limitations 和公平的相对推进；SIGPLAN checklist 也把合适 baseline 和公平配置列为独立项目。

### 结果不能越过测量对象

- Microbenchmark 支持某个操作成本，不自动支持应用端到端收益。
- Simulation 支持模型内行为，不自动支持真实硬件可部署性。
- Mean 支持中心趋势，不描述 tail 或双峰分布。
- 单次部署说明可行性，不自动说明通用性。
- Artifact 能运行说明 functionality，不自动证明所有论文结论已 reproduced。

最后一条也符合 systems artifact evaluator guide 的明确边界：产生相似输出仍不足够，评估者还应确认 artifact 的行为确实对应论文描述。[evaluator guide](https://sysartifacts.github.io/evaluator-guide.html)

## 简洁性的操作方法

简洁应按信息价值删减，而不是平均缩短所有句子。保留顺序是：

1. 核心 claim 及其边界；
2. claim 成立的必要前提；
3. 决定性的因果或推导关系；
4. 能改变可信度的证据；
5. 为理解上述内容必需的定义。

优先删除或压缩：与 thesis 无关的背景、实现过程流水账、同层组件清单、重复数字、无后续作用的例子、重复的 contribution、只宣布章节内容的 metadiscourse，以及 `It is worth noting that`、`As is well known`、`In order to` 一类不改变命题的铺垫。

同一 claim 可以在不同层级重复，但每次必须增加功能：abstract 给结论，introduction 给因果故事，design 给实现方式，evaluation 给证据，conclusion 给可迁移意义和边界。逐字或同义重复不增加信息。

## 常见失败模式

1. **先讲机制，后让读者猜问题。** 组件没有 reader obligation，细节无法排序。
2. **把 feature list 当 contribution。** 功能数量不能说明知识增量或为何有效。
3. **把 generic abstraction 当 high-level。** `flexible architecture`、`efficient framework` 没有约束、因果和边界。
4. **把工程投入当 novelty。** 代码量、开发年数和部署规模可以证明现实性，但不自动构成新思想。
5. **只列 prior-work 缺点，不解释共同 root cause。** 这会产生补丁式设计，而非原则驱动设计。
6. **用 straw-man baseline 扩大 gap。** 不公平比较破坏整个结果链。
7. **一段跨越多个推理义务。** 背景、机制、实验和限制混在一起，使首尾句无法对齐。
8. **用连接词伪造逻辑。** `therefore` 不能把相关性变成因果，`however` 不能制造不存在的对比。
9. **用形容词替代证据。** `scalable`、`robust`、`lightweight` 没有测量维度和范围。
10. **评价只展示最好结果。** 忽略 overhead、失效区间、variance、tail 或语义差异。
11. **把关键证据放入 optional supplement。** 正文因此不能独立支持录用判断。
12. **贡献、实验和结论使用不同量词。** Introduction 声称普遍保证，evaluation 只覆盖一个场景，conclusion 再次扩大。
13. **Related work 是 citation laundry list。** 没有比较轴，读者无法定位 delta。
14. **Conclusion 引入新主张或愿景。** 最后留下未经论证的最强句子。

## 一份可执行的写作审计

### 全文

- 能否用一句有条件、可反驳的话陈述 thesis？
- Title 是否准确暴露对象和推进，且没有强于正文结论？
- Problem、root constraint、principle、mechanism 和 evidence 是否形成依赖链？
- 每项 headline claim 是否有对应证据和边界？
- 贡献类型是否清楚，还是把系统、工具、数据和数字平铺成多个故事？
- Abstract、Introduction 前两页能否独立恢复 problem、delta、insight、reality 和 evidence plan？
- 术语、量词、故障模型、baseline 和实现范围是否前后一致？

### 每一段

- 首句是否提出本段将建立的判断，而非只宣布主题？
- 中间每句是否直接支持该判断？
- 是否混入第二个独立 reader obligation 或突然改变抽象层级？
- 末句是否交付 conclusion、requirement、boundary 或下一步的逻辑前提？
- 删除任何一句后，是否不损失定义、推理、证据、边界或必要过渡？若是，应删。

### 每一句

- 谁做什么是否尽早出现？
- 是否只有一个 dominant assertion？
- cause、contrast、condition、inference 是否真实且显式？
- 技术动词是否准确表达 mechanism 或 evidence strength？
- 数字是否带 metric、baseline、workload、scale 和必要不确定性？
- `all/never/guarantees/optimal/fundamental/scalable` 是否有足够范围和证据？
- 指代、术语和并列层级是否唯一明确？

### Evaluation

- 实验问题是否从 claim 推导，而非从现有图表倒推？
- baseline 是否强、当前、公平并实现相同语义？
- 是否同时检查 end-to-end、attribution、cost、robustness 和 boundary？
- 结论是否只到达证据允许的位置？

### Figures、tables 与 captions

- 每个图表是否服务一个可命名的 claim 或 reader question？
- Caption 是否独立说明对象、比较/设置、takeaway 和关键边界？
- 坐标、单位、normalization、误差、baseline 和 better direction 是否明确？
- 灰度打印和正常缩放下是否仍可辨认？
- Architecture figure 是否显示真正决定论证的边界和依赖，而不仅是组件？

### 中文草稿

- 省略的主语能否唯一恢复？
- 每个“从而/进而/因此”是否对应可成立的因果或推论？
- “高效、灵活、可扩展、安全”是否已还原为具体 property、metric 和范围？
- “保证、证明、表明、提示、观察到”是否匹配证据强度？
- 中译英前是否已消除“该/其/这”的指代歧义并拆开多重断言？

## 最终原则

面向这些 venue 写作时，应把每一页理解成审稿人更新判断的过程，而不是内容容器。段落的工作是完成一个局部推理；句子的工作是以最低歧义编码 claim、condition、cause、evidence 或 boundary；词语的工作是准确表明机制关系与证据强度。真正的顶会级简洁，不是删去技术条件后让句子更响亮，而是在保留可验证因果链的前提下，删除所有不改变科学判断的信息。

## 附录：50 篇可审计论文语料

表中论文标题链接到官方会议页面或 DOI。`摘要动作` 是按前述协议在摘要正文中显式出现的代码组合；例如 `PAEB` 只表示该摘要未显式承担 `G` 与 `I`，不评价全文。`全文` 表示属于 13 篇 introduction/段落近读子集。奖项核验入口包括 [SOSP 2023 program](https://sosp2023.mpi-sws.org/program.html)、[SOSP 2024 conference/awards](https://sigops.org/s/conferences/sosp/2024/)、[SOSP 2025 schedule](https://sigops.org/s/conferences/sosp/2025/schedule.html)、[EuroSys 2024 awards](https://2024.eurosys.org/awards.html)、[ASPLOS 2024 Best Paper awards](https://www.asplos-conference.org/asplos2024/best-paper-awards/index.html) 和 [ASPLOS 2024 artifact awards](https://www.asplos-conference.org/asplos2024/distinguished-artifact-evaluation-awards/index.html)；USENIX 的论文 landing page 直接显示 paper/artifact award 标签。

### OSDI（10 篇）

| 年份 | 论文与官方来源 | 主要贡献类型 | 奖项状态 | 摘要动作 | 近读 |
|---:|---|---|---|---|---|
| 2023 | [Ensō: A Streaming Interface for NIC-Application Communication](https://www.usenix.org/conference/osdi23/presentation/sadok) | 新抽象；NIC/软件跨层机制 | Best Paper | `PGAIEB` | 全文 |
| 2023 | [Triangulating Python Performance Issues with SCALENE](https://www.usenix.org/conference/osdi23/presentation/berger) | 测量/诊断基础设施 | Best Paper | `AIEB` | — |
| 2023 | [An Extensible Orchestration and Protection Framework for Confidential Cloud Computing](https://www.usenix.org/conference/osdi23/presentation/ahmad) | 安全系统；hypervisor/enclave 跨层 | 官方页面无奖项标记 | `PGAIEB` | — |
| 2024 | [VeriSMo: A Verified Security Module for Confidential VMs](https://www.usenix.org/conference/osdi24/presentation/zhou) | Verified system | Best Paper | `PGAIEB` | 全文 |
| 2025 | [Basilisk: Using Provenance Invariants to Automate Proofs of Undecidable Protocols](https://www.usenix.org/conference/osdi25/presentation/zhang-tony) | Verification/analysis | Best Paper | `PGAIEB` | — |
| 2025 | [Principles and Methodologies for Serial Performance Optimization](https://www.usenix.org/conference/osdi25/presentation/park-sujin) | 方法论/文献综合 | 官方页面无奖项标记 | `PGAIEB` | — |
| 2025 | [PoWER Never Corrupts: Tool-Agnostic Verification of Crash Consistency and Corruption Detection](https://www.usenix.org/conference/osdi25/presentation/leblanc) | Verification + storage system | Distinguished Artifact | `PGAIEB` | — |
| 2026 | [Controlling Opaque-Component Effects with Semisolates and Try](https://www.usenix.org/conference/osdi26/presentation/lamprou) | 新抽象；组合/运行时系统 | Best Paper；Distinguished Artifact | `PAIEB` | — |
| 2026 | [PIMS: Fleet-Wide Datacenter Maintenance with Minimal Capacity Buffer and Predictable Latency](https://www.usenix.org/conference/osdi26/presentation/leonhardi) | Operational/experience | 官方页面无奖项标记；Operational Systems | `PAIEB` | — |
| 2026 | [Mimesys: Generating Realistic Executable Testing Environments from Resource Usage Traces](https://www.usenix.org/conference/osdi26/presentation/kim-donghyun) | Testing/benchmark infrastructure | 官方页面无奖项标记 | `PGAIEB` | — |

### SOSP（10 篇）

| 年份 | 论文与官方来源 | 主要贡献类型 | 奖项状态 | 摘要动作 | 近读 |
|---:|---|---|---|---|---|
| 2023 | [TreeSLS: A Whole-system Persistent Microkernel with Tree-structured State Checkpoint on NVM](https://doi.org/10.1145/3600006.3613160) | 新系统/持久化机制 | Best Paper | `PGAIEB` | 全文 |
| 2023 | [Enabling High-Performance and Secure Userspace NVM File Systems with the Trio Architecture](https://doi.org/10.1145/3600006.3613171) | 新抽象/文件系统 | Best Paper | `PGAIEB` | 全文 |
| 2023 | [Project Silica: Towards Sustainable Cloud Archival Storage in Glass](https://doi.org/10.1145/3600006.3613208) | 硬件—软件—服务跨层系统 | 官方奖项页未列名 | `PGAIB` | — |
| 2023 | [A Cloud-Scale Characterization of Remote Procedure Calls](https://doi.org/10.1145/3600006.3613156) | Measurement/experience | 官方奖项页未列名 | `PGAIEB` | — |
| 2024 | [Efficient Reproduction of Fault-Induced Failures in Distributed Systems with Feedback-Driven Fault Injection](https://doi.org/10.1145/3694715.3695979) | Debugging/testing infrastructure | 官方奖项页未列名 | `PGAIEB` | — |
| 2024 | [LazyLog: A New Shared Log Abstraction for Low-Latency Applications](https://doi.org/10.1145/3694715.3695983) | 新抽象/存储系统 | Best Paper | `PGAIEB` | — |
| 2024 | [Verus: A Practical Foundation for Systems Verification](https://doi.org/10.1145/3694715.3695952) | Verification infrastructure | Distinguished Artifact | `PGAEB` | — |
| 2024 | [FBDetect: Catching Tiny Performance Regressions at Hyperscale through In-Production Monitoring](https://doi.org/10.1145/3694715.3695977) | Operational measurement | Best Paper | `PAEB` | — |
| 2025 | [Prove It to the Kernel: Precise Extension Analysis via Proof-Guided Abstraction Refinement](https://doi.org/10.1145/3731569.3764796) | Verification/analysis | Best Paper | `PGAIEB` | — |
| 2025 | [Fast End-to-End Performance Simulation of Accelerated Hardware-Software Stacks](https://doi.org/10.1145/3731569.3764825) | Simulation/benchmark infrastructure；跨层 | 官方奖项页未列名 | `PGAIEB` | — |

### EuroSys（10 篇）

| 年份 | 论文与官方来源 | 主要贡献类型 | 奖项状态 | 摘要动作 | 近读 |
|---:|---|---|---|---|---|
| 2024 | [Serialization/Deserialization-free State Transfer in Serverless Workflows](https://doi.org/10.1145/3627703.3629568) | Serverless runtime / OS primitive | Best Paper | `PGAIEB` | 全文 |
| 2024 | [Validating Database System Isolation Level Implementations with Version Certificate Recovery](https://doi.org/10.1145/3627703.3650080) | 数据库正确性检查 | Best Paper | `PGAIEB` | 全文 |
| 2024 | [Enoki: High Velocity Linux Kernel Scheduler Development](https://doi.org/10.1145/3627703.3629569) | 内核扩展框架 | 官方奖项页未列名 | `PAEB` | — |
| 2024 | [SplitFT: Fault Tolerance for Disaggregated Datacenters via Remote Memory Logging](https://doi.org/10.1145/3627703.3629561) | 解耦数据中心容错 | 官方奖项页未列名 | `PAIEB` | — |
| 2024 | [Minuet: Accelerating 3D Sparse Convolutions on GPUs](https://doi.org/10.1145/3627703.3629560) | GPU/ML 算子优化 | 官方奖项页未列名 | `PAIEB` | — |
| 2024 | [TTLs Matter: Efficient Cache Sizing with TTL-Aware Miss Ratio Curves and Working Set Sizes](https://doi.org/10.1145/3627703.3650066) | 缓存测量与算法 | Gilles Muller Best Artifact Award | `PGAIEB` | — |
| 2024 | [SmartNIC Security Isolation in the Cloud with S-NIC](https://doi.org/10.1145/3627703.3650071) | 安全软硬件协同设计 | 官方奖项页未列名 | `PGAIEB` | — |
| 2024 | [SandTable: Scalable Distributed System Model Checking with Specification-Level State Exploration](https://doi.org/10.1145/3627703.3650077) | 分布式系统模型检查 | 官方奖项页未列名 | `PGAIEB` | — |
| 2024 | [On the Limitations of Carbon-Aware Temporal and Spatial Workload Shifting in the Cloud](https://doi.org/10.1145/3627703.3650079) | 大规模测量/负结果 | 官方奖项页未列名 | `PGAEB` | 全文 |
| 2024 | [Occam: A Programming System for Reliable Network Management](https://doi.org/10.1145/3627703.3650086) | 生产网络管理系统 | 官方奖项页未列名 | `PGAIEB` | — |

### USENIX ATC（10 篇）

| 年份 | 论文与官方来源 | 主要贡献类型 | 奖项状态 | 摘要动作 | 近读 |
|---:|---|---|---|---|---|
| 2023 | [zpoline: a system call hook mechanism based on binary rewriting](https://www.usenix.org/conference/atc23/presentation/yasukata) | 二进制重写/系统调用机制 | Best Paper | `PGAIEB` | 全文 |
| 2023 | [On-demand Container Loading in AWS Lambda](https://www.usenix.org/conference/atc23/presentation/brooker) | Operational cloud/storage system | Best Paper | `PAEB` | 全文 |
| 2024 | [Harmonizing Efficiency and Practicability: Optimizing Resource Utilization in Serverless Computing with Jiagu](https://www.usenix.org/conference/atc24/presentation/liu-qingyuan) | Serverless 资源管理 | 官方议程无奖项标签 | `PGAIEB` | — |
| 2024 | [Starburst: A Cost-aware Scheduler for Hybrid Cloud](https://www.usenix.org/conference/atc24/presentation/luo) | 混合云调度 | Distinguished Artifact | `PGAIEB` | — |
| 2024 | [FastCommit: Resource-Efficient, Performant, and Cost-Effective File System Journaling](https://www.usenix.org/conference/atc24/presentation/shirwadkar) | 生产存储/内核机制 | Best Paper | `PGAIEB` | — |
| 2024 | [Telescope: Telemetry for Gargantuan Memory Footprint Applications](https://www.usenix.org/conference/atc24/presentation/nair) | 内存遥测与分层 | 官方议程无奖项标签 | `PGAIEB` | — |
| 2024 | [mmTLS: Scaling the Performance of Encrypted Network Traffic Inspection](https://www.usenix.org/conference/atc24/presentation/yoon) | 安全网络编程框架 | 官方议程无奖项标签 | `PGAIEB` | — |
| 2024 | [Pecan: Cost-Efficient ML Data Preprocessing with Automatic Transformation Ordering and Hybrid Placement](https://www.usenix.org/conference/atc24/presentation/graur) | ML 数据流水线优化 | 官方议程无奖项标签 | `PGAIEB` | 全文 |
| 2024 | [Removing Obstacles before Breaking Through the Memory Wall: A Close Look at HBM Errors in the Field](https://www.usenix.org/conference/atc24/presentation/wu-ronglong) | 现场测量与故障预测 | 官方议程无奖项标签 | `PGAIEB` | — |
| 2024 | [Data Caching for Enterprise-Grade Petabyte-Scale OLAP](https://www.usenix.org/conference/atc24/presentation/tang) | 生产经验/存储 | 官方议程无奖项标签 | `PGAIEB` | — |

### ASPLOS（10 篇）

| 年份 | 论文与官方来源 | 主要贡献类型 | 奖项状态 | 摘要动作 | 近读 |
|---:|---|---|---|---|---|
| 2024 | [Centauri: Enabling Efficient Scheduling for Communication-Computation Overlap in Large Model Training via Communication Partitioning](https://doi.org/10.1145/3620666.3651379) | 大模型通信调度 | Best Paper | `PGAIEB` | — |
| 2024 | [GIANTSAN: Efficient Memory Sanitization with Segment Folding](https://doi.org/10.1145/3620665.3640391) | 内存安全检测 | Best Paper | `PGAIEB` | 全文 |
| 2024 | [Automatic Generation of Vectorizing Compilers for Customizable Digital Signal Processors](https://doi.org/10.1145/3617232.3624873) | 编译器生成 | Best Paper | `PGAIEB` | 全文 |
| 2024 | [Characterizing Power Management Opportunities for LLMs in the Cloud](https://doi.org/10.1145/3620666.3651329) | Characterization + system case study | 官方奖项页未列名 | `PGAIEB` | 全文 |
| 2024 | [Going Green for Less Green: Optimizing the Cost of Reducing Cloud Carbon Emissions](https://doi.org/10.1145/3620666.3651374) | 碳感知多目标调度 | 官方奖项页未列名 | `PGAEB` | — |
| 2024 | [Formal Mechanised Semantics of CHERI C: Capabilities, Undefined Behaviour, and Provenance](https://doi.org/10.1145/3617232.3624859) | 形式化语义 | 官方奖项页未列名 | `PGAIB` | — |
| 2024 | [SUIT: Secure Undervolting with Instruction Traps](https://doi.org/10.1145/3620665.3640373) | 安全与能耗软硬件协同 | 官方奖项页未列名 | `PGAIEB` | — |
| 2024 | [BypassD: Enabling Fast Userspace Access to Shared SSDs](https://doi.org/10.1145/3617232.3624854) | 存储架构 | Distinguished Artifact Evaluation Award | `PGAIEB` | — |
| 2024 | [LightRidge: An End-to-End Agile Design Framework for Diffractive Optical Neural Networks](https://doi.org/10.1145/3623278.3624757) | 新型硬件与编译协同 | 官方奖项页未列名 | `PAIEB` | — |
| 2024 | [A Quantitative Analysis and Guidelines of Data Streaming Accelerator in Modern Intel Xeon Scalable Processors](https://doi.org/10.1145/3620665.3640401) | 案例研究/经验指南 | 官方奖项页未列名 | `PAB` | — |
