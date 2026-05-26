# 术语表（Glossary）

> **文档版本**：v1.0.0
> **最后更新**：2026-05-10

本项目所有模块共享此术语表。命名在代码、UI、文档中必须保持一致。

---

## A. 业务术语

### A01 · 线索（Lead）
有初步联系但尚未形成意向的潜在客户。核心字段：姓名、手机、城市、来源。
**状态**：`NEW / CONTACTED / INTENTIONAL / INVALID / CONVERTED`

### A02 · 客户（Customer）
已转化的线索。至少有过一次有效接触且有明确意向。

### A03 · 联系人（Contact）
属于某个客户的具体对接人，一个客户可有多个联系人。

### A04 · 跟进（FollowUp）
销售人员对线索/客户的一次具体互动记录。

### A05 · 公海（Lead Pool）
无特定销售归属的线索池。所有符合条件的销售可以从中"捡取"。

### A06 · 私海（Owned Pool）
被特定销售持有的线索集合。

### A07 · 品牌（Brand）
企业旗下的经营品牌，一个企业可有多个品牌。

### A08 · 招商项目（Recruitment Project）
特定品牌在特定时间、特定地区的招商计划。

### A09 · 加盟政策（Policy）
招商项目下的投资标准与条件。

### A10 · 加盟商（Merchant）
与平台签约的投资方，可以是公司或个人。
**状态**：`ACTIVE / SUSPENDED / TERMINATED`
**等级**：`GOLD / SILVER / BRONZE`

### A11 · 门店（Store）
加盟商在具体地理位置经营的实体店。
**生命周期**：`PLANNING / SIGNING / DECORATING / TRAINING / SOFT_OPENING / OPENED / CLOSED`

### A12 · 门店任务（Store Task）
针对门店的运营任务，如"达人探店"、开业检查、巡店等。

### A13 · 合同（Contract）
甲乙方签署的法律文件，关联加盟商与招商项目。
**状态**：`DRAFT / APPROVING / SIGNED / EXECUTING / EXPIRED / TERMINATED`

### A14 · 审批（Approval）
需要人工决策的流程节点，包括审批人、意见、结论。

### A15 · 应收（Receivable）
合同约定的未到账金额。

### A16 · 回款（Payment）
实际已收到的款项记录。

### A17 · 保证金（Deposit）
加盟商支付的履约担保金额，可在违约时扣除。

### A18 · 活动（Campaign）
招商路演、直播、展会等营销活动。

### A19 · Banner
小程序首页的轮播图，后台配置前台显示。

### A20 · 留资（Lead Capture）
C 端用户在小程序提交联系方式的动作。

### A21 · 投资计算器
根据用户输入的面积、城市等参数估算投资总额的工具。

---

## B. 系统角色

| 代号 | 含义 |
|------|------|
| `SUPER_ADMIN` | 集团超级管理员 |
| `OPS_MANAGER` | 运营主管 |
| `SALES` | 招商顾问 |
| `FINANCE` | 财务 |
| `REVIEWER` | 审批人 |
| `CONTENT_EDITOR` | 内容运营 |
| `MERCHANT_OWNER` | 加盟商账号 |
| `STORE_STAFF` | 门店店员 |
| `EXTERNAL_USER` | 小程序 C 端用户 |

---

## C. 权限体系

### C01 · 菜单权限（Menu Permission）
控制用户能否看到某个页面。

### C02 · 按钮权限（Action Permission）
控制用户能否执行页面内具体操作，如"删除"、"导出"按钮。

### C03 · 数据权限（Data Scope）
控制用户能看到的数据范围：
- `ALL` — 全公司
- `DEPARTMENT` — 本部门及下级
- `SELF` — 仅本人
- `CUSTOM` — 自定义授权列表

### C04 · RBAC
Role-Based Access Control，基于角色的访问控制。

### C05 · 租户（Tenant）
独立的业务空间。MVP 单租户，代码预留多租户字段。

---

## D. AI 相关

### D01 · Agent
具备自主决策能力的 AI 助手，可以调用工具完成任务。

### D02 · Tool / Function Calling
AI 调用预定义函数获取数据或执行操作的机制。

### D03 · Provider
AI 模型服务提供商，如 Moonshot Kimi、OpenAI、DeepSeek 等。

### D04 · System Prompt
每次对话开头给 AI 的"角色与规则"指令。

### D05 · RAG
Retrieval-Augmented Generation，检索增强生成。通过工具调用获取真实数据后再生成回复。

### D06 · Token
AI 模型处理的最小单位，按 token 计费。

### D07 · 操作提议（Action Proposal）
AI 生成的待用户确认的写入操作预览。

### D08 · 硬黑名单（Hard-banned Actions）
AI 永远不能执行的操作清单，代码硬编码。

### D09 · 风险等级
`LOW / MEDIUM / HIGH`，决定确认弹窗的强度和是否通知上级。

### D10 · 配额（Quota）
每日/每月 AI token 使用上限。

### D11 · OCR（Optical Character Recognition）
光学字符识别。本项目中特指基于大模型多模态能力的图像识别。

### D12 · 多模态（Multimodal）
AI 模型同时支持文字、图片、视频等多种输入形式的能力。Kimi K2.6 为多模态模型。

### D13 · M15 / AI OCR 数据录入
Irys 独立模块。通过 AI 视觉识别将图片数据转为结构化数据，经人工核对后入库。**仅 SUPER_ADMIN 可用**。

### D14 · OCRJob
一次 OCR 任务的完整生命周期记录，包含上传图片、AI 识别、人工核对、最终入库四个阶段。

### D15 · OCRScene
OCR 场景枚举。MVP 仅 `STORE_DAILY_DATA`，代码预留合同/身份证/营业执照/小票等扩展。

### D16 · 置信度（Confidence）
AI 对识别结果准确性的自评估，0-1 之间。本项目用三级阈值（0.95 / 0.80 / 0.60）分别对应不同 UI 提示。

### D17 · 修改痕迹（Edit Trail）
用户在核对页面对 AI 识别结果的修改记录，完整保留原始值、最终值、修改人、修改时间，用于审计。

### D18 · 图片 hash 去重
通过 SHA-256 为每张图片生成唯一指纹，同 hash 图片在系统中只允许存在一份，防止重复上传/伪造数据。

---

## E. 技术术语

### E01 · Monorepo
单一代码仓库包含多个互相关联的包/应用。本项目用 pnpm workspace。

### E02 · DTO
Data Transfer Object，定义 API 请求和响应的数据结构。

### E03 · Prisma Schema
Prisma ORM 的数据库定义文件。

### E04 · SSE
Server-Sent Events，服务端推送流式数据的协议（AI 流式输出使用）。

### E05 · JWT / Refresh Token
JSON Web Token，鉴权令牌。双 Token 策略：短期 Access + 长期 Refresh。

### E06 · Soft Delete（软删除）
通过 `deleted_at` 字段标记而非真删。本项目默认软删除。

### E07 · 审计日志（AuditLog）
记录谁在何时做了什么的日志。不可删除、不可修改。

### E08 · 幂等（Idempotency）
同一操作多次执行结果一致。关键写入接口要求幂等键。

---

## F. 流程术语

### F01 · 垂直切片（Vertical Slice）
一次交付覆盖数据层 + 服务层 + 接口层 + 前端的完整功能，而非按层切片。

### F02 · MVP
Minimum Viable Product，最小可行产品。

### F03 · MoSCoW
需求优先级法则：`Must / Should / Could / Won't`。

### F04 · ADR
Architecture Decision Record，架构决策记录。

---

## 维护规则

- 新增术语一律在本文件登记
- 术语变更必须同步更新所有关联文档
- 中英文对照统一：代码用英文，文档可用中英
- 枚举值一律 `UPPER_SNAKE_CASE`
