# AI Engineering Reflection Series

AI 工程化沉思录是一组面向 AI Native Engineering 的长期文章系列，用于记录 AI 如何进入真实软件工程流程，并逐步改变上下文管理、代码 Review、Prompt 组织和工作流状态管理。

这个系列不定位为 AI 工具分享，而是关注 AI 如何重构软件工程中的协作方式、知识沉淀方式和开发者体验。

## 系列定位

- 记录 AI Coding 在真实工程环境中的变化与副作用
- 沉淀 Developer Experience / AI Workflow / Human-in-the-loop Engineering 观察
- 为后续 examples、diagrams、prompts 和 workflow 材料预留结构
- 支持 GitHub、掘金、公众号和知乎等平台的系列化发布

## 系列逻辑链

```text
Context Debt
→ Code Review
→ Prompt Architecture
→ Workflow State Management
```

## 文章概览

| Series | Topic | Article | Summary |
| --- | --- | --- | --- |
| Series 1 | Context Debt | [01 · Context Debt](series-1-context-debt/01-context-debt.md) | 当 AI Coding 进入真实工程环境后，Context 正在成为新的复杂度来源。 |
| Series 2 | Code Review | `series-2-code-review/01-ai-code-review.md` | 讨论 AI 输出增多后，Review 如何从代码检查转向风险、语义和责任边界确认。 |
| Series 3 | Prompt Architecture | `series-3-prompt-architecture/01-prompt-as-architecture.md` | 讨论 Prompt 如何逐渐承担架构约束、协作规则和上下文组织的角色。 |
| Series 4 | Workflow State | `series-4-workflow-state/01-ai-workflow-state.md` | 讨论 AI Workflow 中的状态连续性、Session 管理和长期沉淀方式。 |

## 目录结构

```text
experience-summary/
├── series-1-context-debt/
├── series-2-code-review/
├── series-3-prompt-architecture/
└── series-4-workflow-state/
```

每个 series 目录预留：

- `assets/`：图片、图表、截图等材料
- `examples/`：代码片段、Prompt 示例、最小 workflow 示例

后续可按需增加：

```text
diagrams/
prompts/
workflow/
```

## Frontmatter 规范

未来所有系列文章统一使用：

```yaml
---
title:
date:
status:
tags:
summary:
---
```

Tags 示例：

```yaml
tags:
  - AI Workflow
  - Context Engineering
  - AI Coding
  - Developer Experience
```
