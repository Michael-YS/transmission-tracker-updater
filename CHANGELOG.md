# 更新日志

所有重要的项目变更都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [1.0.0] - 2026-01-30

### 新增
- 初始版本发布
- 支持从多个 URL 源获取 tracker 列表
- 批量更新所有活跃种子的 tracker
- 自动触发种子重新宣告功能
- 完整的日志记录系统
- systemd timer 支持（Linux）
- 灵活的配置文件系统

### 功能
- 支持 Transmission RPC 连接（HTTP/HTTPS）
- 自动合并去重 tracker 列表
- 保留原有 tracker，仅添加新 tracker
- 可配置的超时和日志级别
