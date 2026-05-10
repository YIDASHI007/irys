# Irys Enterprise Suite

> 媒体公司企业管理后台 · 招商小程序 · AI 智能助手一体化平台

---

## 📖 项目简介

Irys 是一个面向媒体/连锁企业的**中台管理系统**，集中管理人员、客户、招商、加盟商、门店、合同、财务、营销内容等核心业务。内置 **AI 智能助手**，支持基于真实数据的问答与后台操作协助。对外通过**招商小程序**承接流量。

### 核心特色

- 🏢 **企业中台** — 14 个模块覆盖全业务链路
- 🤖 **AI 原生** — 对接月之暗面 Kimi，数据问答 + 操作协助
- 🔒 **安全优先** — 三层权限模型 + 操作确认 + 全量审计
- 📱 **多端统一** — PC 后台 + 小程序 + 加盟商端共享后端
- 🧩 **可扩展** — 预留多租户、多品牌、电子签、支付等接口

---

## 📚 文档导航

> 当前阶段：**Phase 1 — 需求定义完成** ✅

### 必读文档（按阅读顺序）

| # | 文档 | 说明 | 状态 |
|---|------|------|------|
| 1 | [docs/requirements.md](./docs/requirements.md) | 📋 完整需求文档（主文档） | ✅ v1.0 |
| 2 | [docs/glossary.md](./docs/glossary.md) | 📖 术语表 | ✅ v1.0 |
| 3 | [docs/business-rules.md](./docs/business-rules.md) | 📏 业务规则清单（BR-编号） | ✅ v1.0 |
| 4 | [docs/user-journeys.md](./docs/user-journeys.md) | 🗺️ 用户旅程图 | ✅ v1.0 |
| 5 | [docs/out-of-scope.md](./docs/out-of-scope.md) | 🚫 本期不做清单 | ✅ v1.0 |
| 6 | [docs/open-questions.md](./docs/open-questions.md) | ❓ 待确认问题 | ✅ v1.0 |

### AI 模块专项

| 文档 | 说明 |
|------|------|
| [docs/ai-security.md](./docs/ai-security.md) | 🛡️ AI 安全规则、权限模型、黑名单、审计 |
| [docs/ai-tools-registry.md](./docs/ai-tools-registry.md) | 🔧 30 个 AI 工具定义（15 查询 + 15 写入） |

### 待产出（后续阶段）

| 文档 | 阶段 | 说明 |
|------|------|------|
| `docs/database.md` | Phase 2 | Prisma Schema 完整定义 |
| `docs/state-machines.md` | Phase 2 | 所有状态机 Mermaid 图 |
| `docs/api-contract.md` | Phase 4 | REST API 契约 |
| `docs/openapi.yaml` | Phase 4 | OpenAPI 规范 |
| `docs/deployment.md` | Phase 9 | 部署手册 |
| `docs/runbook.md` | Phase 9 | 应急手册 |
| `docs/adr/` | 持续 | 架构决策记录 |

---

## 🎯 产品范围速览

### 角色（9 类）
`SUPER_ADMIN` · `OPS_MANAGER` · `SALES` · `FINANCE` · `REVIEWER` · `CONTENT_EDITOR` · `MERCHANT_OWNER` · `STORE_STAFF` · `EXTERNAL_USER`

### 功能模块（14 个）

```
L1 基础层
├─ M1  账号与权限中心
└─ M13 系统设置

L2 通用层
├─ M2  工作台
├─ M7  合同与审批
├─ M12 消息通知
└─ M14 AI 智能助手  ⭐

L3 业务层
├─ M3  CRM 客户中心
├─ M4  招商项目
├─ M5  加盟商管理
├─ M6  门店管理
├─ M8  财务结算
├─ M9  营销与内容
└─ M11 数据看板

L4 触点层
└─ M10 小程序装修
```

### MVP 优先级（MoSCoW）

- 🟥 **Must**：M1, M2, M3, M4, M6, M13, M14
- 🟨 **Should**：M5, M7, M11, M12
- 🟩 **Could**：M8, M9, M10
- 🟦 **Won't**：详见 [out-of-scope.md](./docs/out-of-scope.md)

---

## 🛠️ 技术栈（建议）

| 层 | 选型 |
|---|------|
| 后端 | NestJS + Prisma + PostgreSQL + Redis + BullMQ |
| 后台 | Vue 3 + TypeScript + Vite + Element Plus + Pinia |
| 小程序 | uni-app（兼顾 H5/APP） |
| AI | Moonshot Kimi（OpenAI 兼容协议） |
| 存储 | MinIO（dev）/ 阿里云 OSS（prod） |
| 工程 | pnpm workspace + Turborepo |
| 部署 | Docker Compose（MVP） |
| 监控 | pino + Sentry |

> 最终技术栈在 Phase 3 正式确定。

---

## 📅 开发路线图（8 周 MVP）

```
Week 0  ████████                 Phase 0-1  想法验证 + 需求定义 ✅ 当前阶段
Week 1  ████████                 Phase 2-4  领域建模 + 技术选型 + API 契约
Week 2  ████████                 Phase 5-6  原型验证 + 骨架搭建
Week 3  ████████                 切片 1     账号权限 + 工作台
Week 4  ████████                 切片 2-3   CRM 线索 + 招商项目
Week 5  ████████                 切片 4-5   加盟商 + 门店 + 合同
Week 6  ████████                 切片 6     AI 底座 + 查询
Week 7  ████████                 切片 7     AI 操作 + 确认流
Week 8  ████████                 Phase 8-9  看板 + 导出 + 上线
```

---

## 🚀 本地启动（占位 — Phase 6 后补充）

```bash
# 1. 克隆仓库
git clone https://github.com/YIDASHI007/irys.git
cd irys

# 2. 安装依赖（待 Phase 6 后可用）
# pnpm install

# 3. 启动依赖服务
# docker compose up -d postgres redis minio

# 4. 初始化数据库
# pnpm --filter backend prisma migrate dev
# pnpm --filter backend prisma db seed

# 5. 启动后端
# pnpm --filter backend dev

# 6. 启动后台前端
# pnpm --filter admin dev
# 浏览器访问：http://localhost:5173

# 7. 启动小程序（微信开发者工具导入 apps/mini）
```

---

## 🧪 测试（Phase 7 后补充）

```bash
# 单元测试
# pnpm test

# E2E 测试
# pnpm test:e2e

# 覆盖率
# pnpm test:coverage
```

---

## 📝 关键决策记录

| # | 决策 | 日期 |
|---|------|------|
| D1 | AI Key 混合模式（全局 + 个人） | 2026-05-10 |
| D2 | AI 能力严格等于用户能力 | 2026-05-10 |
| D3 | 财务默认全可见，保留脱敏开关 | 2026-05-10 |
| D4 | MVP 单 Provider（Kimi），代码多 Provider 抽象 | 2026-05-10 |
| D5 | 审批流 MVP 代码定义，二期做可视化 | 2026-05-10 |
| D6 | 电子签 MVP 不做，预留接口 | 2026-05-10 |
| D7 | 财务 MVP 不对接支付，只记账 | 2026-05-10 |
| D8 | 达人探店作为门店子模块 | 2026-05-10 |
| D9 | 门店数据采集：邮件+AI识别+手工 三路并行 | 2026-05-10 |

---

## 🎯 下一步行动

### 需要业务方确认

- [ ] 通读 [requirements.md](./docs/requirements.md) 并反馈意见
- [ ] 回答 [open-questions.md](./docs/open-questions.md) 中的 🔴 级问题
- [ ] 确认 MVP 优先级的 MoSCoW 分级

### 即将开始（Phase 2）

- [ ] 领域建模 → `docs/database.md`
- [ ] 状态机可视化 → `docs/state-machines.md`
- [ ] ER 图绘制

### 建议线下完成

- [ ] 与真实销售、运营、财务各访谈 1 小时
- [ ] 收银系统是否有 API / 能否定时导出邮件
- [ ] 月之暗面 Kimi 开放平台注册 + API Key

---

## 📁 仓库结构（当前）

```
irys/
├── README.md                 ← 你现在看的这个
├── docs/                     ← 全部设计文档
│   ├── requirements.md       主需求文档
│   ├── business-rules.md     业务规则
│   ├── user-journeys.md      用户旅程
│   ├── glossary.md           术语表
│   ├── out-of-scope.md       本期不做
│   ├── open-questions.md     待确认问题
│   ├── ai-security.md        AI 安全规则
│   └── ai-tools-registry.md  AI 工具清单
├── .gitattributes
└── IrysGame_Linux_1.1.zip    (遗留文件，后续会清理)
```

---

## 🤝 贡献指南（后续补充）

待 Phase 6 项目骨架搭建完成后补充：
- 代码风格
- Commit 规范
- Pull Request 模板
- 分支策略

---

## 📄 许可证

待定（建议 MIT 或企业内部许可）。

---

## 📞 联系方式

- **产品负责人**：待填
- **技术负责人**：待填
- **仓库**：https://github.com/YIDASHI007/irys

---

> **当前状态**：Phase 1（需求定义）已完成，可随时进入 Phase 2（领域建模）。
> 如需开始下一阶段，请告知并提供 🔴 级问题的决策。
