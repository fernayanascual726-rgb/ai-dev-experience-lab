# Memory Engineering

## 概览

Memory Engineering 关注 AI 系统如何组织、更新、裁剪和使用长期 Context。它不是简单地保存更多历史，而是为不同生命周期、不同可信度、不同作用域的信息建立工程边界。

## 为什么重要

当 AI Workflow 进入真实项目后，系统会持续积累需求、决策、约束、偏好和历史错误。如果没有明确的 Memory 设计，长期 Memory 会逐渐变成噪声源，影响后续判断。

## 常见 Pattern

- Memory Layer Pattern：按生命周期和作用域拆分 Memory
- Memory Pruning Strategy：定期裁剪过期、冲突和低价值信息
- Project Memory：沉淀项目级长期约束和协作偏好
- Confidence Annotation：为 Memory 标注来源、可信度和更新时间

## 典型 Case

- 为 AI Coding Agent 维护项目级 Context
- 在长期协作中清理过期团队约定
- 将一次性任务 Context 转化为稳定项目知识
- 避免旧决策污染新架构演进

## 相关文档

- [Memory Layer Pattern](memory-layer-pattern.md)
- [Memory Pruning Strategy](memory-pruning-strategy.md)
- [Project Memory Case](project-memory-case.md)
