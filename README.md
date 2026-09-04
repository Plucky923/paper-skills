# PaperSkills

面向系统研究论文的审查与改写 skills，重点是问题驱动的论证、恰当的抽象层次、简洁且精确的表达，以及技术含义保真。

## 从哪里开始

| 要做什么 | 入口 |
| --- | --- |
| 审查论文或指定研究材料，不改写原文 | [systems-paper-review](skills/systems-paper-review/SKILL.md) |
| 根据已提供证据起草或修改论文文字 | [systems-paper-revise](skills/systems-paper-revise/SKILL.md) |
| 查看系统论文写作要求及调研依据 | [写作要求调研](research/systems-paper-writing-requirements.md) |
| 检查 skill 行为与验收条件 | [合成回归测试与验收流程](benchmarks/README.md) |
| 使用当前获准的外部 benchmark | [外部评测使用说明](benchmarks/external/README.md) |
| 查看外部 benchmark 的任务依据与适用边界 | [外部 benchmark 准入依据](research/external-benchmark-admission.md) |

## 当前评测边界

ParaRev 用于受限段落改写；新输出需要人工盲评，并先检查技术含义是否保留。ParaReval 只用于校准对固定 A/B 输出的评价，不能直接给新改写评分。

现阶段没有获准使用的外部审稿 benchmark。外部数据不替代合成回归测试，也不能单独证明达到 OSDI、SOSP、EuroSys、ATC 或 ASPLOS 的写作要求。适用范围以 [admission.json](benchmarks/external/admission.json) 及准入依据为准。

## 目录职责

```text
skills/                   两个 skills 及各自参考材料
benchmarks/
  fixtures/               原创合成回归案例
  external/               当前外部评测指南、准入策略与来源清单
    cache/                本地数据；Git 忽略
research/                 写作要求与准入依据
scripts/                  结构校验器与外部评测工具
tests/                    评测工具的确定性单元测试
```

准备和运行命令会按需创建 `benchmarks/external/work/` 与 `runs/`，两者均由 Git 忽略。

## 不调用模型的本地检查

在仓库根目录执行：

```bash
python3 -B scripts/validate_skills.py
python3 -B -m unittest discover -s tests
python3 -B scripts/external_benchmarks.py list
python3 -B scripts/external_benchmarks.py verify --source all --summary
```

前三条命令不要求下载语料；最后一条检查本地缓存，尚未下载时会报告缺失。下载、准备批次、模型调用及盲评步骤见外部评测使用说明；模型调用会消耗账户额度。

只将自有 skills、代码、合成案例、来源元数据和使用说明纳入 Git。第三方论文、人工标签、生成文本与运行日志留在被忽略的目录。
