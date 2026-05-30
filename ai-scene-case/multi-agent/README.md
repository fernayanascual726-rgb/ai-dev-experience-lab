# Multi-Agent

## 概览

Multi-Agent 关注多个 AI Agent 在同一工程任务中的角色划分、协调机制、State 共享和冲突处理。目标不是增加 Agent 数量，而是通过明确分工降低复杂任务的认知负担。

## 为什么重要

当任务跨越需求分析、代码修改、测试验证、Review 和文档更新时，单一 Agent 容易混合职责、丢失 Context 或忽略局部风险。Multi-Agent 模式需要工程化编排，避免角色混乱和 State 冲突。

## 常见 Pattern

- Coordinator Pattern：由 Coordinator 维护任务目标和阶段 State
- Reviewer Agent Pattern：独立 Review 设计和实现风险
- Specialist Agent：按领域拆分检索、Testing、文档等职责
- Shared State Contract：约定 Agent 之间共享什么 State

## 典型 Case

- 一个 Agent 实现，另一个 Agent Review 变更
- Coordinator 拆分大型重构任务
- Tester Agent 独立验证实现结果
- 多 Agent 协作处理跨模块变更

## 相关文档

- [Coordinator Pattern](coordinator-pattern.md)
- [Reviewer Agent Pattern](reviewer-agent-pattern.md)
- [Multi-Agent Case](multi-agent-case.md)
