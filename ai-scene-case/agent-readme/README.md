# Agent README

## 概览

Agent README 关注如何为 AI Agent 提供稳定、可维护、可审计的工程 Context。典型载体包括 `CLAUDE.md`、`AGENTS.md`、项目级 README、团队协作规范和任务说明模板。

## 为什么重要

AI Agent 的执行质量高度依赖它能否正确理解项目边界、编码规范、测试方式和协作约束。缺少 Agent 可读文档时，团队会不断在对话中重复补充 Context，造成低效和不一致。

## 常见 Pattern

- Project Instruction File：项目级 Agent 指令文件
- Role-specific Agent README：面向不同 Agent 角色的 Context 说明
- Task Entry Template：任务入口模板
- Guardrail Section：安全边界、禁止行为和提交规则

## 典型 Case

- 为 Claude Code 维护项目级 `CLAUDE.md`
- 为多工具协作维护统一 `AGENTS.md`
- 为 Review Agent 提供架构边界说明
- 为 Test Agent 提供测试运行和验证规则

## 相关文档

- [CLAUDE.md Best Practice](claude-md-best-practice.md)
- [AGENTS.md Best Practice](agents-md-best-practice.md)
- [Agent README Template](agent-readme-template.md)
