# State Management

## 概览

State Management 关注 AI Workflow 在长链路、多步骤、多 Agent 场景中的 State 设计。它包括任务 State、执行 State、恢复 State、Context State 和外部副作用 State。

## 为什么重要

真实 AI Workflow 很少只是一次生成。它可能读取代码、规划任务、修改文件、运行测试、处理失败、重试、恢复 Context 并继续执行。系统必须知道什么已经完成、什么失败、什么可以重试、什么必须人工介入。

## 常见 Pattern

- Workflow State Pattern：定义可恢复的 Workflow State Machine
- Task State Design：拆分任务 State 与执行 State
- Idempotent Step：为外部动作设计幂等边界
- Recovery Checkpoint：在关键节点建立恢复点

## 典型 Case

- 长任务中断后恢复执行
- 多步骤 AI 自动化任务避免重复副作用
- Review / Test / Fix 循环中的 State 追踪
- 多 Agent 协同时维护共享任务 State

## 相关文档

- [Workflow State Pattern](workflow-state-pattern.md)
- [Task State Design](task-state-design.md)
- [State Management Case](state-management-case.md)
