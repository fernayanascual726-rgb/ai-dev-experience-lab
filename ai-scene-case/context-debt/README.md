# Context Debt

## 概览

Context Debt 指 AI 系统在多轮交互、长期任务和复杂项目中积累的 Context 负担。它包括过期信息、冲突约束、错误摘要、无关历史和未清理的中间 State。

## 为什么重要

Context Window 变大并不会自动消除 Context 问题。Context 越多，模型越容易受到噪声、旧 State 和错误假设影响。Context Debt 会降低 AI 协作的稳定性和可解释性。

## 常见 Pattern

- Context Debt Detection：识别污染、漂移和冲突 Context
- Context Pruning Pattern：在关键节点裁剪 Context
- Context Cleanup Case：任务结束后清理临时 State
- Context Boundary：区分任务 Context、项目 Context 和组织 Context

## 典型 Case

- 多轮修复后 AI 仍沿用已废弃假设
- 长任务中旧错误覆盖新的真实 State
- Agent 误把临时调试信息当成长期约束
- 项目 Memory 中保留了已经失效的技术决策

## 相关文档

- [Context Debt Detection](context-debt-detection.md)
- [Context Pruning Pattern](context-pruning-pattern.md)
- [Context Cleanup Case](context-cleanup-case.md)
