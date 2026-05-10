# AI 工具注册表（Tools Registry）

> **文档版本**：v1.0.0
> **最后更新**：2026-05-10
> **适用模块**：M14 AI 智能助手
> **关联文档**：[ai-security.md](./ai-security.md) · [requirements.md](./requirements.md)

---

## 0. 工具总览

MVP 阶段共设计 **30 个工具**：15 个查询工具 + 15 个写入工具。

| 类别 | 数量 | 需确认 | 风险等级 |
|------|-----|--------|---------|
| 查询类（只读） | 15 | ❌ | — |
| 写入类（单体） | 10 | ✅ | LOW / MEDIUM |
| 写入类（批量/敏感） | 5 | ✅✅ | HIGH |

---

## 1. 工具 Schema 通用规范

每个工具必须定义：

```typescript
interface AITool {
  name: string;                    // snake_case，如 query_leads
  description: string;             // 给 AI 看的自然语言描述
  parameters: JsonSchema;          // OpenAPI JSON Schema
  requireConfirmation: boolean;    // 是否需要用户确认
  severity?: 'LOW' | 'MEDIUM' | 'HIGH';
  requiredPermissions: string[];   // 对应 RBAC 权限点
  requiredDataScope?: DataScope;   // 最低数据权限要求
  category: ToolCategory;          // 分组
}
```

### 命名约定

- 查询：`query_*` / `get_*` / `list_*`
- 创建：`create_*` / `add_*`
- 更新：`update_*` / `modify_*` / `set_*`
- 转移：`assign_*` / `transfer_*`
- 批量：`batch_*`
- 审批：`approve_*` / `reject_*`
- 导出：`export_*`

### 参数规范

- 日期一律 `YYYY-MM-DD`
- 时间一律 ISO 8601 UTC
- 金额用字符串传（避免 JS 浮点）
- 枚举必须用预定义枚举值，大写下划线
- ID 一律字符串（cuid）

---

## 2. 查询类工具（15 个，只读，无需确认）

### 2.1 CRM 相关

#### T01 · `query_leads`
```yaml
description: 查询线索列表，支持按状态、销售、时间、城市筛选
parameters:
  type: object
  properties:
    status:
      type: string
      enum: [NEW, CONTACTED, INTENTIONAL, INVALID, CONVERTED]
    assigneeId:
      type: string
      description: 负责销售的用户 ID
    city:
      type: string
    source:
      type: string
      enum: [MINI_PROGRAM, WEBSITE, PHONE, EXHIBITION, REFERRAL, MANUAL]
    startDate:
      type: string
      description: 创建时间起（YYYY-MM-DD）
    endDate:
      type: string
    page:
      type: integer
      default: 1
    pageSize:
      type: integer
      default: 20
      maximum: 100
requireConfirmation: false
requiredPermissions: [lead:read]
```

#### T02 · `query_lead_detail`
```yaml
description: 查询单条线索详情，含完整跟进时间线
parameters:
  type: object
  required: [leadId]
  properties:
    leadId:
      type: string
    includeFollowUps:
      type: boolean
      default: true
requireConfirmation: false
requiredPermissions: [lead:read]
```

#### T03 · `query_customers`
```yaml
description: 查询已转化客户列表
parameters:
  type: object
  properties:
    tag: { type: string }
    ownerId: { type: string }
    page: { type: integer, default: 1 }
    pageSize: { type: integer, default: 20 }
requireConfirmation: false
requiredPermissions: [customer:read]
```

#### T04 · `query_overdue_followups`
```yaml
description: 查询超期未跟进的线索
parameters:
  type: object
  properties:
    daysOverdue:
      type: integer
      default: 7
      description: 超过几天未跟进
    assigneeId: { type: string }
requireConfirmation: false
requiredPermissions: [lead:read]
```

### 2.2 招商相关

#### T05 · `query_recruitment_projects`
```yaml
description: 查询招商项目列表
parameters:
  type: object
  properties:
    status:
      type: string
      enum: [DRAFT, RECRUITING, PAUSED, CLOSED]
    brandId: { type: string }
    region: { type: string }
requireConfirmation: false
requiredPermissions: [project:read]
```

### 2.3 加盟商相关

#### T06 · `query_merchants`
```yaml
description: 查询加盟商列表
parameters:
  type: object
  properties:
    status:
      type: string
      enum: [ACTIVE, SUSPENDED, TERMINATED]
    level:
      type: string
      enum: [GOLD, SILVER, BRONZE]
    region: { type: string }
requireConfirmation: false
requiredPermissions: [merchant:read]
```

### 2.4 门店相关

#### T07 · `query_stores`
```yaml
description: 查询门店列表
parameters:
  type: object
  properties:
    status:
      type: string
      enum: [PLANNING, SIGNING, DECORATING, TRAINING, SOFT_OPENING, OPENED, CLOSED]
    brandId: { type: string }
    merchantId: { type: string }
    city: { type: string }
requireConfirmation: false
requiredPermissions: [store:read]
```

#### T08 · `get_store_daily_data`
```yaml
description: 查询门店每日经营数据
parameters:
  type: object
  required: [storeId]
  properties:
    storeId: { type: string }
    startDate: { type: string }
    endDate: { type: string }
    metrics:
      type: array
      items:
        type: string
        enum: [revenue, orderCount, customerCount, avgOrderValue]
requireConfirmation: false
requiredPermissions: [store:read]
```

### 2.5 合同相关

#### T09 · `query_contracts`
```yaml
description: 查询合同列表
parameters:
  type: object
  properties:
    status:
      type: string
      enum: [DRAFT, APPROVING, SIGNED, EXECUTING, EXPIRED, TERMINATED]
    merchantId: { type: string }
    expiringWithinDays:
      type: integer
      description: 即将在 N 天内到期
requireConfirmation: false
requiredPermissions: [contract:read]
```

#### T10 · `query_approvals`
```yaml
description: 查询待我审批的任务
parameters:
  type: object
  properties:
    type:
      type: string
      enum: [CONTRACT, STORE_OPENING, APPLICATION, BUDGET, OTHER]
    status:
      type: string
      enum: [PENDING, APPROVED, REJECTED]
      default: PENDING
requireConfirmation: false
requiredPermissions: [approval:read]
```

### 2.6 数据统计类

#### T11 · `get_sales_ranking`
```yaml
description: 获取销售业绩排行榜
parameters:
  type: object
  properties:
    period:
      type: string
      enum: [today, this_week, this_month, this_quarter, this_year]
      default: this_month
    metric:
      type: string
      enum: [lead_count, followup_count, signed_count, signed_amount]
      default: signed_amount
    limit:
      type: integer
      default: 10
requireConfirmation: false
requiredPermissions: [dashboard:read]
```

#### T12 · `get_revenue_summary`
```yaml
description: 获取营收汇总数据
parameters:
  type: object
  properties:
    period: { type: string, enum: [today, this_week, this_month, this_year] }
    groupBy:
      type: string
      enum: [day, week, month, region, brand]
    brandId: { type: string }
requireConfirmation: false
requiredPermissions: [finance:read]
```

#### T13 · `get_conversion_funnel`
```yaml
description: 获取招商转化漏斗数据
parameters:
  type: object
  properties:
    period: { type: string }
    brandId: { type: string }
    region: { type: string }
requireConfirmation: false
requiredPermissions: [dashboard:read]
```

### 2.7 通知/待办

#### T14 · `get_notifications`
```yaml
description: 获取我的通知列表
parameters:
  type: object
  properties:
    unreadOnly: { type: boolean, default: false }
    category:
      type: string
      enum: [APPROVAL, REMINDER, SYSTEM, ANNOUNCEMENT]
requireConfirmation: false
requiredPermissions: []
```

#### T15 · `query_users`
```yaml
description: 查询员工（用于分配、指派场景）
parameters:
  type: object
  properties:
    role:
      type: string
    departmentId:
      type: string
    keyword:
      type: string
      description: 姓名/工号模糊匹配
requireConfirmation: false
requiredPermissions: [user:read]
```

---

## 3. 写入类工具（15 个，需确认）

### 3.1 CRM 写入

#### T16 · `update_lead_status` 🟢 LOW
```yaml
description: 更新线索状态
parameters:
  type: object
  required: [leadId, newStatus]
  properties:
    leadId: { type: string }
    newStatus:
      type: string
      enum: [CONTACTED, INTENTIONAL, INVALID, CONVERTED]
    note: { type: string }
requireConfirmation: true
severity: LOW
requiredPermissions: [lead:write]
```

#### T17 · `create_followup` 🟢 LOW
```yaml
description: 新建跟进记录
parameters:
  type: object
  required: [leadId, type, content]
  properties:
    leadId: { type: string }
    type:
      type: string
      enum: [PHONE, MEETING, WECHAT, VISIT, SIGNING]
    content: { type: string, maxLength: 1000 }
    nextFollowUpAt: { type: string, description: ISO 8601 }
requireConfirmation: true
severity: LOW
requiredPermissions: [followup:create]
```

#### T18 · `assign_lead` 🟡 MEDIUM
```yaml
description: 将单条线索分配给指定销售
parameters:
  type: object
  required: [leadId, assigneeUserId]
  properties:
    leadId: { type: string }
    assigneeUserId: { type: string }
    reason: { type: string }
requireConfirmation: true
severity: MEDIUM
requiredPermissions: [lead:assign]

confirmPreview:
  title: 分配线索确认
  summary: "将线索【{leadName}】分配给【{assigneeName}】"
  fields: [leadId, currentOwner, newOwner, reason]
```

#### T19 · `transfer_lead_to_pool` 🟡 MEDIUM
```yaml
description: 将线索从私海退回公海
parameters:
  type: object
  required: [leadIds]
  properties:
    leadIds:
      type: array
      items: { type: string }
      maxItems: 20
    reason: { type: string }
requireConfirmation: true
severity: MEDIUM
requiredPermissions: [lead:transfer]
```

#### T20 · `batch_assign_leads` 🔴 HIGH
```yaml
description: 批量分配线索（> 20 条走高风险流程）
parameters:
  type: object
  required: [filter, assigneeUserId]
  properties:
    filter:
      type: object
      properties:
        status: { type: string }
        city: { type: string }
        source: { type: string }
        currentAssigneeId: { type: string }
    assigneeUserId: { type: string }
    maxCount:
      type: integer
      description: 最多分配多少条
      maximum: 500
    reason:
      type: string
      description: 必填
requireConfirmation: true
severity: HIGH
requiredPermissions: [lead:batch_assign]
notifySupervisor: true
```

### 3.2 任务相关

#### T21 · `create_task` 🟢 LOW
```yaml
description: 新建任务
parameters:
  type: object
  required: [title, assigneeUserId]
  properties:
    title: { type: string }
    description: { type: string }
    assigneeUserId: { type: string }
    dueDate: { type: string }
    priority:
      type: string
      enum: [LOW, NORMAL, HIGH, URGENT]
      default: NORMAL
    relatedEntity:
      type: object
      properties:
        type: { type: string, enum: [LEAD, STORE, MERCHANT, CONTRACT] }
        id: { type: string }
requireConfirmation: true
severity: LOW
requiredPermissions: [task:create]
```

#### T22 · `update_task_status` 🟢 LOW
```yaml
description: 更新任务状态
parameters:
  type: object
  required: [taskId, newStatus]
  properties:
    taskId: { type: string }
    newStatus:
      type: string
      enum: [NOT_STARTED, IN_PROGRESS, COMPLETED, CANCELLED]
    note: { type: string }
requireConfirmation: true
severity: LOW
requiredPermissions: [task:write]
```

### 3.3 审批相关

#### T23 · `approve_application` 🟡 MEDIUM
```yaml
description: 通过审批
parameters:
  type: object
  required: [approvalTaskId]
  properties:
    approvalTaskId: { type: string }
    comment: { type: string }
requireConfirmation: true
severity: MEDIUM
requiredPermissions: [approval:approve]
```

#### T24 · `reject_application` 🟡 MEDIUM
```yaml
description: 驳回审批
parameters:
  type: object
  required: [approvalTaskId, comment]
  properties:
    approvalTaskId: { type: string }
    comment: { type: string, description: 驳回原因必填 }
requireConfirmation: true
severity: MEDIUM
requiredPermissions: [approval:approve]
```

### 3.4 门店相关

#### T25 · `update_store_status` 🟡 MEDIUM
```yaml
description: 更新门店生命周期状态
parameters:
  type: object
  required: [storeId, newStatus]
  properties:
    storeId: { type: string }
    newStatus:
      type: string
      enum: [PLANNING, SIGNING, DECORATING, TRAINING, SOFT_OPENING, OPENED, CLOSED]
    note: { type: string }
    effectiveAt: { type: string }
requireConfirmation: true
severity: MEDIUM
requiredPermissions: [store:write]
```

#### T26 · `add_store_daily_data` 🟢 LOW
```yaml
description: 录入门店每日经营数据（支持手工或 AI 识别预填后确认）
parameters:
  type: object
  required: [storeId, businessDate, totalRevenue]
  properties:
    storeId: { type: string }
    businessDate: { type: string, description: YYYY-MM-DD }
    totalRevenue: { type: string }
    orderCount: { type: integer }
    customerCount: { type: integer }
    averageOrderValue: { type: string }
    source:
      type: string
      enum: [MANUAL, AI_OCR, EMAIL, API]
      default: MANUAL
    ocrImageUrls: { type: array, items: { type: string } }
requireConfirmation: true
severity: LOW
requiredPermissions: [store_data:create]
```

### 3.5 财务相关

#### T27 · `record_payment` 🟡 MEDIUM
```yaml
description: 登记回款
parameters:
  type: object
  required: [contractId, amount, paymentDate]
  properties:
    contractId: { type: string }
    amount: { type: string }
    paymentDate: { type: string }
    method:
      type: string
      enum: [BANK_TRANSFER, ALIPAY, WECHAT, CASH, OTHER]
    note: { type: string }
requireConfirmation: true
severity: MEDIUM
requiredPermissions: [finance:write]
```

### 3.6 通知/导出

#### T28 · `send_notification` 🟢 LOW
```yaml
description: 向指定用户发送站内通知
parameters:
  type: object
  required: [recipientUserIds, title, content]
  properties:
    recipientUserIds:
      type: array
      items: { type: string }
      maxItems: 50
    title: { type: string }
    content: { type: string }
    category:
      type: string
      enum: [REMINDER, ANNOUNCEMENT, SYSTEM]
    relatedEntity:
      type: object
requireConfirmation: true
severity: LOW
requiredPermissions: [notification:send]
```

#### T29 · `export_report` 🟢 LOW
```yaml
description: 生成报表导出任务（异步）
parameters:
  type: object
  required: [reportType]
  properties:
    reportType:
      type: string
      enum: [LEADS, CONTRACTS, STORES, SALES_RANKING, REVENUE, STORE_DAILY]
    filters:
      type: object
    format:
      type: string
      enum: [CSV, XLSX]
      default: CSV
requireConfirmation: true
severity: LOW
requiredPermissions: [export:create]

returnValue:
  exportJobId: string
  downloadUrl: string
  expiresAt: string
```

#### T30 · `export_customer_list` 🔴 HIGH
```yaml
description: 导出完整客户列表（含联系方式，高敏感）
parameters:
  type: object
  properties:
    filters:
      type: object
      properties:
        tag: { type: string }
        ownerId: { type: string }
        createdAfter: { type: string }
    includeFields:
      type: array
      items:
        type: string
        enum: [name, phone, email, company, address, followUpHistory]
requireConfirmation: true
severity: HIGH
requiredPermissions: [customer:export]
notifySupervisor: true
auditExtra:
  - flagReason: "客户个人信息导出"
```

---

## 4. Tool 调用流程完整示例

### 场景：销售小李问"帮我把上个月没跟进的线索都转成公海"

```
1. 用户输入
   ↓
2. AI 理解意图 → 决定调用 query_overdue_followups + transfer_lead_to_pool

3. 第一步：查询
   Tool: query_overdue_followups
   Params: { daysOverdue: 30, assigneeId: "user-li" }
   
   ⚠️ 数据权限拦截：
   - 小李是 SALES，dataScope=SELF
   - 自动在 WHERE 条件加 assignee_id = user-li
   
   结果：[L001, L002, L003, ..., L023]（23 条）
   
4. AI 回复用户
   "您名下有 23 条超过 30 天未跟进的线索，请确认是否转回公海？"
   
5. 用户："是的"
   ↓
6. 第二步：写入操作
   Tool: transfer_lead_to_pool
   Params: { leadIds: [L001...L023], reason: "超过 30 天未跟进" }
   
   ⚠️ 第 1 层黑名单检查：不在黑名单 ✅
   ⚠️ 第 2 层权限检查：lead:transfer ✅
   ⚠️ 数量检查：23 条 > 20，升级到 HIGH 风险 🔴
   
7. 生成操作预览 → 前端弹窗
   🚨 高风险操作
   将 23 条线索转回公海
   [展示 23 条列表]
   请输入"确认"继续：[______]
   ⚠️ 本次操作将通知您的上级
   
8. 用户输入"确认" + 点击执行
   ↓
9. 后端再次校验 → 执行 → 审计
   
10. AI 回复
    "✅ 已将 23 条线索转回公海池，已通知您的上级 @王经理"
```

---

## 5. Tool 版本管理

### 5.1 版本号规则

每个 Tool 带版本号：`name: query_leads`, `version: 1`

### 5.2 升级策略

- **非破坏性变更**（新增可选参数）→ 版本号不变
- **破坏性变更**（改参数名、改必填） → 版本号 +1，保留旧版本至少 3 个月
- **废弃** → 标记 `deprecated: true`，AI 不再加载该工具

---

## 6. Tool 加载策略

### 6.1 全量加载 vs 懒加载

**MVP 方案：全量加载**
- 所有用户有权限的 Tool 全部描述放入 system prompt
- 适合 Tool 数量 < 50 时

**二期优化：懒加载**
- 先做意图分类（使用小模型或规则）
- 根据意图只加载相关类别的 Tool
- 大幅降低 token 消耗

### 6.2 Token 预算

假设 30 个工具，每个描述平均 150 tokens：

```
单工具描述: 150 tokens
总工具描述: 150 × 30 = 4,500 tokens
System Prompt: 约 800 tokens
用户消息: 约 100 tokens
历史上下文: 约 2,000 tokens
────────────────────────
单次请求输入: ~7,400 tokens
```

按 Kimi K2 输入单价 ≈ ¥4/百万 tokens 计算，单次对话 ≈ ¥0.03。

---

## 7. Tool 测试规范

每个 Tool 必须有测试覆盖：

- [ ] 参数 schema 校验（合法/非法）
- [ ] 权限校验（有权限/无权限/越权）
- [ ] 数据范围过滤（ALL / DEPARTMENT / SELF）
- [ ] 黑名单命中（硬黑名单工具）
- [ ] 确认流程（PENDING → APPROVED → EXECUTED）
- [ ] 超时处理（EXPIRED）
- [ ] 审计日志写入
- [ ] 异常场景（数据不存在、并发修改）

---

## 附录 A：Tool 优先级排期

| Sprint | Tool 编号 | 备注 |
|--------|----------|------|
| Sprint 1（AI 底座） | 无工具 | 只做基础聊天 |
| Sprint 2（AI 查询） | T01, T02, T07, T11, T15, T14 | 最高频场景 |
| Sprint 3（AI 查询） | T03, T04, T05, T06, T08, T09, T10 | 完整查询 |
| Sprint 4（AI 操作） | T16, T17, T18, T21, T22 | LOW/MEDIUM 写入 |
| Sprint 5（AI 操作） | T23, T24, T25, T26, T27, T28, T29 | 补充写入 + 导出 |
| Sprint 6（高风险） | T12, T13, T19, T20, T30 | 高风险确认流 |

---

## 附录 B：未来扩展（v2+）

以下 Tool 在 MVP 之后考虑：

- `schedule_meeting` — 日程集成
- `generate_followup_script` — AI 生成跟进话术
- `summarize_conversation` — 对话摘要
- `detect_anomaly` — 异常数据检测
- `recommend_next_action` — 智能推荐下一步
- `voice_to_followup` — 语音转跟进记录
- `image_to_store_data` — 截图识别录入（这个也可以提前做）
- `auto_assign_by_rule` — 基于规则自动分配
