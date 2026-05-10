# 📚 开发功能索引表

> 用法:当你要做某个功能时,来这里查应该看哪份文档的哪段。
> 目的:让小白不迷路,不用翻遍所有文档。

---

## 🎯 使用方法

1. 在下表中找到你要做的功能
2. 打开对应的文档,**只看**对应章节
3. 复制那段内容,用 `docs/dev-workflow.md` 里的提示词喂给 AI
4. **不要把整个文档丢给 AI**

---

## 📋 功能索引总表

### 基础设施(Phase 6 · 搭骨架)

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| Monorepo 结构 | dev-workflow.md | Step 2 |
| 数据库初始化 | dev-workflow.md + requirements.md | Step 3, "9. 核心数据实体" |
| 环境变量配置 | dev-workflow.md | Step 4 |
| Docker 开发环境 | dev-workflow.md | Step 5 |

### M1 · 账号与权限

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 登录(手机号+密码) | requirements.md, business-rules.md | M1.5, BR-103/104/105 |
| JWT 鉴权 | business-rules.md | BR-105 |
| 员工 CRUD | requirements.md, business-rules.md | M1.2, BR-101/108 |
| 组织架构树 | requirements.md | M1.1 |
| 角色管理 | requirements.md, business-rules.md | M1.3, BR-106/107 |
| 权限分配 | requirements.md | M1.3 |
| 字典管理 | requirements.md | M1.4 |
| 登录失败锁定 | business-rules.md | BR-104 |
| 密码强度校验 | business-rules.md | BR-103 |

### M2 · 工作台

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 首页布局 | requirements.md | M2 |
| 待办中心 | requirements.md, user-journeys.md | M2, 旅程 4 |
| 快捷操作 | requirements.md | M2 |
| 数据概览卡片 | requirements.md | M2 |

### M3 · CRM 客户中心

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 线索列表 | requirements.md, business-rules.md | M3.1, BR-201~209 |
| 线索详情 | requirements.md | M3.1 |
| 线索状态流转 | business-rules.md | BR-202 |
| 手机号去重 | business-rules.md | BR-201 |
| 线索分配 | business-rules.md, user-journeys.md | BR-203, 旅程 2 |
| 公海池回收 | business-rules.md | BR-204 |
| 抢单防刷 | business-rules.md | BR-206 |
| 客户管理 | requirements.md | M3.2 |
| 跟进记录 | requirements.md, business-rules.md | M3.4, BR-207/208 |

### M4 · 招商项目

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 品牌管理 | requirements.md | M4.2 |
| 项目创建 | requirements.md | M4.1 |
| 项目状态 | business-rules.md | BR-301 |
| 加盟政策 | requirements.md | M4.3 |
| 资料包管理 | requirements.md, business-rules.md | M4.4, BR-304 |
| 投资计算器 | requirements.md | M4.5 |
| 项目自动关闭 | business-rules.md | BR-303 |

### M5 · 加盟商管理

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 加盟商档案 | requirements.md, business-rules.md | M5.1, BR-401/402 |
| 加盟商账号 | requirements.md, business-rules.md | M5.2, BR-403/404 |
| 加盟商分级 | requirements.md, business-rules.md | M5.3, BR-403 |
| 资质审核 | requirements.md | M5.1 |

### M6 · 门店管理

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 门店档案 | requirements.md, business-rules.md | M6.1, BR-504 |
| 门店生命周期 | requirements.md, business-rules.md | M6.2, BR-501/502 |
| 门店审批流 | business-rules.md | BR-502 |
| 门店地图 | requirements.md | M6.4 |
| 门店任务 | requirements.md | M6.3 |
| 每日数据采集(通用) | requirements.md, business-rules.md | M6.5, BR-505/506/507 |
| **AI OCR 数据录入** | **ai-ocr-module.md** | **全文,仅 SUPER_ADMIN** |
| 异常数据检测 | business-rules.md | BR-507 |

### M7 · 合同审批

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 合同创建 | requirements.md, business-rules.md | M7.1, BR-602 |
| 合同状态流转 | business-rules.md | BR-601 |
| 审批流引擎 | requirements.md, business-rules.md | M7.2, BR-604/605 |
| 到期提醒 | business-rules.md | BR-606 |
| 合同模板 | requirements.md | M7.1 |

### M8 · 财务结算

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 应收管理 | requirements.md | M8.1 |
| 回款登记 | requirements.md, business-rules.md | M8.1, BR-701/702/703 |
| 保证金 | requirements.md, business-rules.md | M8.2, BR-704/705 |
| 对账账单 | requirements.md | M8.3 |

### M9 · 营销内容

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 活动管理 | requirements.md, business-rules.md | M9.1, BR-805 |
| 优惠券 | requirements.md | M9.2 |
| 文章管理 | requirements.md, business-rules.md | M9.3, BR-801/802 |
| Banner | requirements.md, business-rules.md | M9.4, BR-803/804 |

### M10 · 小程序装修

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 页面装修 | requirements.md | M10.1 |
| 留资表单 | requirements.md, business-rules.md | M10.2, BR-901/902/903 |
| 菜单配置 | requirements.md | M10.3 |

### M11 · 数据看板

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 招商漏斗 | requirements.md | M11.1 |
| 运营数据 | requirements.md | M11.2 |
| 财务看板 | requirements.md | M11.3 |
| 门店数据 | requirements.md | M11.4 |
| CSV 导出 | requirements.md, business-rules.md | M11.5, BR-1002/1003 |

### M12 · 消息通知

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 站内信 | requirements.md | M12.1 |
| 短信通道 | requirements.md | M12.2 |
| 通知模板 | requirements.md | M12.3 |

### M13 · 系统设置

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 参数配置 | requirements.md | M13.1 |
| 附件管理 | requirements.md, business-rules.md | M13.2, BR-1207 |
| 审计日志 | requirements.md, business-rules.md | M13.3, BR-1202 |
| 定时任务 | requirements.md | M13.4 |

### M14 · AI 智能助手 ⭐

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| AI 配置页(Key 管理) | requirements.md, business-rules.md, ai-security.md | M14.1, BR-1106/1110, §7 |
| API Key 加密 | ai-security.md, business-rules.md | §7, BR-1106 |
| 对话功能 | requirements.md | M14.2 |
| 流式输出(SSE) | requirements.md | M14.2 |
| 数据问答(RAG) | requirements.md, ai-security.md | M14.3, §1 |
| 工具调用框架 | ai-security.md, ai-tools-registry.md | §1, §1 |
| 操作确认流 | requirements.md, business-rules.md, ai-security.md | M14.4, BR-1103/1104/1108, §3/§4 |
| 黑名单拦截 | ai-security.md, business-rules.md | §2, BR-1102 |
| 配额熔断 | business-rules.md, ai-security.md | BR-1105, §10 |
| 审计日志 | business-rules.md, ai-security.md | BR-1107, §9 |
| 某个具体 Tool | ai-tools-registry.md | T01~T32 |

### M15 · AI OCR 数据录入 ⭐(仅 SUPER_ADMIN)

| 功能 | 看什么 | 章节/编号 |
|------|-------|----------|
| 入口 + 权限守卫 | ai-ocr-module.md, business-rules.md | §10, BR-1301 |
| 图片上传 | ai-ocr-module.md, business-rules.md | §4, BR-1303 |
| Kimi 多模态调用 | ai-ocr-module.md | §6 |
| Prompt 模板 | ai-ocr-module.md | §6 |
| 人工核对页 | ai-ocr-module.md, business-rules.md | §14, BR-1302 |
| 反作弊 | ai-ocr-module.md, business-rules.md | §8, BR-1303~1310 |
| 异常检测 | ai-ocr-module.md, business-rules.md | §9, BR-1315~1317 |
| 审计日志 | ai-ocr-module.md, business-rules.md | §10.4, BR-1313 |
| 成本监控 | ai-ocr-module.md, business-rules.md | §13, BR-1312 |

---

## 🔍 常用组合速查

### "我要做一个列表页"(通用)
看:
- requirements.md 对应模块(如 M3.1 线索列表)
- 无需看全,只看"字段"+"功能点"即可

### "我要做一个表单页"(通用)
看:
- requirements.md 对应模块的"字段"
- business-rules.md 对应校验规则(BR-XXX)

### "我要做状态流转"
看:
- business-rules.md 对应状态机(BR-202 / BR-601 / BR-501 等)
- user-journeys.md 对应旅程

### "我要做 AI 功能"
看:
- ai-security.md §0 核心原则(**必看**)
- ai-tools-registry.md 对应工具
- business-rules.md BR-1101~1111

### "我要对接外部服务"(短信/OSS/支付)
看:
- requirements.md 对应模块
- open-questions.md 相关问题(可能还没定)

---

## ⚠️ 常见小白疑问

### Q1: 我要查"手机号为什么要唯一"怎么办?
A: 搜 business-rules.md 里的 "BR-101"

### Q2: 我想知道线索完整流转过程?
A: 看 user-journeys.md 第 2 节 + business-rules.md BR-202

### Q3: 我忘了 M15 只能超管用了
A: 看 ai-ocr-module.md §10.1 + ai-security.md §0 第五原则

### Q4: AI 给我生成代码用了 any,怎么办?
A: 看 .cursorrules 中"禁用高级特性",贴给 AI 让它重写

### Q5: 我不知道今天该做什么
A: 打开 docs/dev-workflow.md,看你的进度到哪一步

---

## 📖 文档地图

```
docs/
├── requirements.md         主需求(4000 行,按模块查)
├── business-rules.md       业务规则(120+ 条 BR 编号)
├── user-journeys.md        用户旅程(8 个 Mermaid 图)
├── ai-security.md          AI 安全规则
├── ai-tools-registry.md    32 个 AI 工具定义
├── ai-ocr-module.md        M15 独立 PRD
├── dev-workflow.md         🎯 开发步骤(你的地图)
├── dev-index.md            🎯 功能索引(本文档)
├── page-structure.md       🎯 完整页面结构树(~92 个页面)
├── glossary.md             术语表
├── out-of-scope.md         不做清单
└── open-questions.md       待确认问题
```

---

## 💡 给小白的 5 句心得

1. **做哪个功能,查哪份文档**——不要一次看完所有文档,会崩溃
2. **看到 BR-XXX 要高亮**——这是业务规则,写代码必引用
3. **忘了也没关系**——本文档随时来查
4. **AI 给你代码时,它可能忽略某些规则**——你要对照文档检查
5. **每完成一个功能,回到 dev-workflow.md 打勾**——有进度感,不焦虑
