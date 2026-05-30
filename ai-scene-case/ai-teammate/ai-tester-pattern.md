# AI Tester Pattern

## Problem

AI 常被用于生成测试，但单纯生成测试并不是核心工程价值。更有用的角色是帮助团队思考验证策略、缺失场景、回归风险和可观测性缺口。

如果缺少清晰 Pattern，AI 生成的测试可能很浅、重复，或者与真实风险脱节。

## Solution

将 AI Tester 作为验证设计助手。它的职责是识别应该测试什么、为什么重要，以及哪种验证层级合适。

Testing 层级：

- unit test：验证本地逻辑
- integration test：验证组件边界
- contract test：验证 API 期望
- regression test：覆盖已知失败模式
- manual 或 staged validation：验证外部副作用

## Architecture

```mermaid
flowchart LR
    Change[拟议变更] --> Risk[风险分析]
    Risk --> Strategy[测试策略]
    Strategy --> Cases[测试用例]
    Cases --> Human[Human Review]
    Human --> Implementation[测试实现]
```

## Example

一个变更修改 Memory Pruning 行为。AI Tester 不应只生成 unit tests，而应提出场景：

- 过期 Memory 会被移除
- 持久 Project Rules 会被保留
- 重复 Memory 条目会被合并
- 冲突 Memory 需要 Human Review
- 外部引用不会被复制到长期 Memory 中

然后由人类工程师选择哪些测试进入自动化套件。

## Trade-offs

收益：

- 提升测试场景覆盖
- 早期暴露边界情况
- 帮助识别不明显风险
- 分离策略与实现

成本：

- 可能产生过多测试想法
- 可能推荐维护成本高的测试
- 需要项目 Context 才能选择正确验证层级
- 需要人工排序优先级

## Best Practices

- 先要求测试策略，再要求测试代码。
- 每个测试建议都应绑定到一个风险。
- 优先选择少量高信号测试，而不是大范围生成覆盖。
- 包含负向场景和恢复场景。
- 由人类决定哪些测试进入长期套件。
- Review AI 生成测试的脆弱性和虚假信心。
