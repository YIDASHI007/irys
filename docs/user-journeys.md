# 用户旅程（User Journeys）

> **文档版本**：v1.0.0
> **最后更新**：2026-05-10
>
> 用 Mermaid 流程图描述每个角色的关键旅程。
> 这是**业务流程的可视化源头**，状态机、API 设计都以此为依据。

---

## 目录

1. [C 端用户：浏览到留资](#1-c-端用户浏览到留资)
2. [招商顾问：线索跟进全流程](#2-招商顾问线索跟进全流程)
3. [运营主管：项目与门店管理](#3-运营主管项目与门店管理)
4. [审批人：合同审批](#4-审批人合同审批)
5. [加盟商：自助门店管理](#5-加盟商自助门店管理)
6. [财务：回款登记](#6-财务回款登记)
7. [用户与 AI 助手交互](#7-用户与-ai-助手交互)
8. [门店数据录入（多渠道）](#8-门店数据录入多渠道)

---

## 1. C 端用户：浏览到留资

### 路径：公众发现品牌 → 小程序浏览 → 留资 → 后台跟进

```mermaid
flowchart TD
    Start([用户通过广告/朋友介绍/搜索]) --> Open[打开招商小程序]
    Open --> Home[首页浏览 Banner + 推荐项目]
    Home --> Choose{感兴趣？}
    Choose -->|否| Leave([退出])
    Choose -->|是| Detail[查看品牌详情 / 项目详情]
    Detail --> Calc{想估算投资？}
    Calc -->|是| Calculator[使用投资计算器]
    Calc -->|否| Form
    Calculator --> Form[进入留资表单]
    Form --> Fill[填写姓名/手机/城市]
    Fill --> Verify{频率检查 BR-901}
    Verify -->|超限| ShowCaptcha[弹出滑动验证]
    ShowCaptcha --> Fill
    Verify -->|通过| Submit[提交表单]
    Submit --> Dedupe{手机号去重 BR-201}
    Dedupe -->|重复| UpdateExisting[更新已有线索]
    Dedupe -->|新线索| CreateLead[创建 Lead, status=NEW]
    CreateLead --> Assign{自动分配规则 BR-203}
    Assign -->|匹配| NotifySales[推送销售: 新线索]
    Assign -->|无匹配| Pool[进入公海池]
    UpdateExisting --> Done
    NotifySales --> Done
    Pool --> Done([用户看到: 提交成功])
```

### 异常流
- 网络异常 → 表单自动本地缓存，恢复后自动重试
- 手机号已是客户 → 提示"您已是我们的客户，是否联系负责的 @XX"
- 位置获取失败 → 降级为手动选择城市

---

## 2. 招商顾问：线索跟进全流程

### 路径：接收线索 → 跟进 → 意向确认 → 转客户 → 推合同

```mermaid
flowchart TD
    Start([开始上班]) --> Login[登录后台]
    Login --> Home[进入工作台]
    Home --> CheckTodo[查看今日待办]
    CheckTodo --> NewLeads{有新分配线索？}
    NewLeads -->|是| ContactLead[电话/微信联系]
    NewLeads -->|否| OldLeads[继续跟进老线索]
    ContactLead --> Update1[更新状态 NEW → CONTACTED]
    OldLeads --> Followup[新建跟进记录]
    Update1 --> Followup
    Followup --> Type{跟进类型}
    Type -->|打电话| Phone[记录通话内容]
    Type -->|微信| Wechat[记录聊天要点]
    Type -->|面谈| Meeting[记录面谈纪要 + 位置]
    Phone --> SetNext[设置下次跟进时间]
    Wechat --> SetNext
    Meeting --> SetNext
    SetNext --> Result{结果判断}
    Result -->|强意向| UpdateI[状态 → INTENTIONAL]
    Result -->|无意向| UpdateInv[状态 → INVALID + 原因]
    Result -->|继续跟进| Next([循环])
    UpdateI --> PushAssets[发送招商资料包]
    PushAssets --> Negotiate[商务洽谈]
    Negotiate --> Consent{达成合作？}
    Consent -->|否| UpdateInv
    Consent -->|是| Convert[转客户: 创建 Customer]
    Convert --> DraftContract[起草合同]
    DraftContract --> SubmitApproval[提交审批流]
    SubmitApproval --> WaitApproval[等待审批结果]
    WaitApproval --> Approved{通过？}
    Approved -->|驳回| FixDraft[修改后重提]
    FixDraft --> SubmitApproval
    Approved -->|通过| Sign[线下签约]
    Sign --> UploadContract[上传合同扫描件]
    UploadContract --> End([状态 → SIGNED])
```

### 关键规则
- BR-202 状态机
- BR-204 超期回公海
- BR-207 跟进不可删
- BR-208 转客户条件

---

## 3. 运营主管：项目与门店管理

### 路径：配置招商项目 → 发布小程序 → 跟踪进展 → 门店开业

```mermaid
flowchart TD
    Start([新品牌/新项目]) --> CreateBrand[创建品牌档案]
    CreateBrand --> CreateProject[创建招商项目 status=DRAFT]
    CreateProject --> ConfigPolicy[配置加盟政策]
    ConfigPolicy --> UploadAssets[上传资料包]
    UploadAssets --> SetTargets[设定目标地区 + 数量]
    SetTargets --> SetCalc[配置投资计算器]
    SetCalc --> Preview[预览小程序效果]
    Preview --> OK{确认？}
    OK -->|否| AdjustConfig[调整配置]
    AdjustConfig --> Preview
    OK -->|是| Publish[发布 status=RECRUITING]
    Publish --> Announce[推送通知给销售]
    Announce --> Monitor[监控招商漏斗]
    Monitor --> Daily{每日检查}
    Daily --> Leads[查看线索数]
    Daily --> Conv[查看转化率]
    Daily --> Signed[查看签约数]
    Leads --> Action{需调整？}
    Conv --> Action
    Signed --> Action
    Action -->|是| Optimize[调整投放/政策/分配规则]
    Action -->|否| Continue[持续监控]
    Optimize --> Monitor
    Continue --> Signed2{有签约？}
    Signed2 -->|是| ApproveMerchant[审批加盟商资质]
    ApproveMerchant --> CreateStore[创建门店记录]
    CreateStore --> Planning[PLANNING]
    Planning --> Progress[跟进建店进度]
    Progress --> Milestone{到达关键节点}
    Milestone -->|首款到账| ToDecor[审批→DECORATING]
    Milestone -->|试营业完成| ToOpen[审批→OPENED]
    ToDecor --> Progress
    ToOpen --> Running([门店运营中])
```

---

## 4. 审批人：合同审批

```mermaid
flowchart TD
    Start([收到审批通知]) --> Open[打开待办中心]
    Open --> Pick[选择一个审批任务]
    Pick --> Review[查看合同详情]
    Review --> CheckItems{逐项检查}
    CheckItems --> ProjectMatch[项目是否匹配]
    CheckItems --> AmountReasonable[金额是否合理]
    CheckItems --> LegalOK[条款是否合规]
    CheckItems --> AssetsComplete[资料是否齐全]
    ProjectMatch --> Decide{判断}
    AmountReasonable --> Decide
    LegalOK --> Decide
    AssetsComplete --> Decide
    Decide -->|通过| Approve[填写意见 + 通过]
    Decide -->|驳回| Reject[填写驳回原因]
    Decide -->|需讨论| Delegate[加签 / 转交]
    Approve --> NextNode{还有下一节点？}
    Reject --> NotifySubmitter[通知发起人修改]
    Delegate --> Target[指定协审人]
    NextNode -->|是| PassNext[流转下一审批人]
    NextNode -->|否| FinalApproved[合同 → SIGNED]
    PassNext --> End([结束])
    FinalApproved --> End
    NotifySubmitter --> End
    Target --> End
```

---

## 5. 加盟商：自助门店管理

```mermaid
flowchart TD
    Start([加盟商登录]) --> Home[个人工作台]
    Home --> MyStores[查看我的门店列表]
    MyStores --> Pick[选择门店]
    Pick --> Overview[门店概况]
    Overview --> Tasks{日常操作}
    Tasks --> InputData[录入每日经营数据]
    Tasks --> ViewContract[查看我的合同]
    Tasks --> ViewBilling[查看账单]
    Tasks --> Messages[查看系统通知]
    InputData --> Upload[拍照/上传截图]
    Upload --> AI[AI 识别预填]
    AI --> Review[人工核对]
    Review --> Confirm[确认提交]
    Confirm --> Done1([数据入库])
    ViewContract --> PaymentPlan[查看回款计划]
    PaymentPlan --> NeedPay{有逾期？}
    NeedPay -->|是| Contact[联系财务]
    NeedPay -->|否| Normal([正常])
    ViewBilling --> Download[下载账单 PDF]
    Messages --> Reply{需响应？}
    Reply -->|是| Process[处理通知]
    Reply -->|否| Mark[标记已读]
```

---

## 6. 财务：回款登记

```mermaid
flowchart TD
    Start([收到银行流水]) --> OpenFinance[打开财务模块]
    OpenFinance --> FindContract[查找对应合同]
    FindContract --> Match{能匹配？}
    Match -->|否| Research[联系销售/加盟商核实]
    Research --> Match
    Match -->|是| Record[登记回款]
    Record --> FillFields[填写金额/日期/方式]
    FillFields --> LargeCheck{金额 > 10k? BR-702}
    LargeCheck -->|是| UploadProof[上传转账凭证]
    LargeCheck -->|否| NoProof[无需凭证]
    UploadProof --> Validate{金额校验 BR-701}
    NoProof --> Validate
    Validate -->|超额| Error[报错: 超合同应收]
    Validate -->|通过| Save[保存记录]
    Save --> AutoUpdate[自动更新合同已付金额]
    AutoUpdate --> CheckClosure{合同已付清？}
    CheckClosure -->|是| MarkPaid[合同标记已付清]
    CheckClosure -->|否| KeepExecuting[保持 EXECUTING]
    MarkPaid --> Notify[通知销售 + 加盟商]
    KeepExecuting --> End([完成])
    Notify --> End
    Error --> FillFields
```

---

## 7. 用户与 AI 助手交互

### 场景：销售问"本月我的签约情况"

```mermaid
sequenceDiagram
    participant U as 销售用户
    participant F as 前端
    participant B as 后端 Agent
    participant T as Tool Registry
    participant D as 数据库
    participant K as Kimi API

    U->>F: 打开 AI 抽屉
    U->>F: "本月我的签约情况"
    F->>B: POST /ai/chat/{conversationId}
    B->>B: 加载历史 + 用户上下文
    B->>B: 构建 System Prompt
    B->>K: 流式调用 chat/completions
    K->>K: 理解意图 → 决定调用工具
    K-->>B: tool_call: get_sales_ranking(period=this_month, userId=...)
    B->>T: 查找工具
    T->>B: QueryRankingTool
    B->>B: 三层权限校验<br/>1. 黑名单 ✓<br/>2. 角色权限 ✓<br/>3. 数据范围=SELF
    B->>D: SELECT ... WHERE owner_id = current_user
    D-->>B: [{month: "2026-05", contracts: 3, amount: 150000}]
    B->>K: tool_result: [...]
    K-->>B: 流式输出自然语言
    B-->>F: SSE: "您本月已签约 **3 单**，总额 **¥150,000**..."
    F->>U: Markdown 渲染显示
```

### 场景：销售问"把张三的线索转给李四"（越权）

```mermaid
sequenceDiagram
    participant U as 销售用户
    participant B as 后端 Agent
    participant K as Kimi

    U->>B: "把张三的线索转给李四"
    B->>K: 调用 AI
    K-->>B: tool_call: assign_lead(leadId=..., assigneeUserId=...)
    B->>B: 权限校验
    Note over B: 销售的 dataScope=SELF<br/>"张三的线索"不属于当前用户<br/>校验失败
    B-->>K: tool_error: 您无权操作他人线索
    K-->>B: 流式输出
    B-->>U: "抱歉，您没有权限操作他人持有的线索。<br/>如需转派，请联系运营主管。"
```

### 场景：销售请求批量转公海（高风险）

```mermaid
sequenceDiagram
    participant U as 销售用户
    participant F as 前端
    participant B as 后端
    participant K as Kimi

    U->>B: "把我超过 30 天没跟进的线索都转公海"
    B->>K: 调用
    K-->>B: tool_call: query_overdue_followups(...)
    B->>B: 查询（数据权限过滤 = SELF）
    B-->>U: "您名下有 23 条超过 30 天未跟进的线索"
    U->>B: "是的，都转走"
    B->>K: 继续对话
    K-->>B: tool_call: transfer_lead_to_pool(leadIds=[...])
    B->>B: requireConfirmation=true,<br/>数量=23 > 20 → severity=HIGH
    B->>B: 生成 ActionProposal, status=PENDING
    B-->>F: action_proposal event
    F->>U: 弹出 HIGH 风险弹窗
    Note over F,U: 请输入"确认"<br/>本次操作将通知您的上级
    U->>F: 输入"确认" + 点击执行
    F->>B: POST /ai/actions/{actionId}/approve
    B->>B: 再次权限校验 + 执行
    B->>B: 审计日志 + 通知上级
    B-->>K: tool_result: {affected: 23}
    K-->>B: 生成回复
    B-->>U: "✅ 已将 23 条线索转回公海，已通知 @王经理"
```

---

## 8. 门店数据录入（多渠道）

```mermaid
flowchart TD
    Start([开始当日数据录入]) --> Channel{数据来源？}
    Channel -->|官方 API| API[系统自动拉取]
    Channel -->|邮件导出| Email[定时任务扫邮箱]
    Channel -->|浏览器插件| Plugin[员工点插件抓取]
    Channel -->|AI 识别| Photo[员工上传截图]
    Channel -->|手工| Manual[员工填表单]

    API --> Parse1[解析标准响应]
    Email --> Parse2[解析 CSV/Excel 附件]
    Plugin --> Parse3[解析页面 DOM]

    Parse1 --> PreFill
    Parse2 --> PreFill
    Parse3 --> PreFill

    Photo --> OCR[调用通义 VL / GPT-4V]
    OCR --> Conf{置信度 > 0.8?}
    Conf -->|否| HighRiskReview[强制人工核对]
    Conf -->|是| PreFill

    PreFill[预填表单]
    Manual --> Form
    PreFill --> Form
    HighRiskReview --> Form

    Form[人工核对页面]
    Form --> Check{数据有异常？BR-507}
    Check -->|是| FlagAnomaly[标记异常 + 原因]
    Check -->|否| SubmitOK[正常提交]
    FlagAnomaly --> SubmitAnomaly[异常提交]
    SubmitOK --> Dedupe{storeId+date 已存在？}
    SubmitAnomaly --> Dedupe
    Dedupe -->|是| CompareVersion[保留历史版本, 按 BR-506 决定主数据]
    Dedupe -->|否| Insert[插入新记录]
    CompareVersion --> Audit
    Insert --> Audit[写入审计 + 通知]
    Audit --> Dashboard([进入看板数据])
```

---

## 附录：旅程关联的 API 预览

| 旅程 | 关键 API |
|------|---------|
| 1. C 端留资 | `POST /mini/leads` |
| 2. 销售跟进 | `PATCH /leads/:id/status` `POST /leads/:id/followups` |
| 3. 运营管理 | `POST /projects` `PATCH /stores/:id/status` |
| 4. 审批 | `POST /approvals/:id/approve` `POST /approvals/:id/reject` |
| 5. 加盟商 | `GET /merchant/me/stores` `POST /stores/:id/daily-data` |
| 6. 财务 | `POST /contracts/:id/payments` |
| 7. AI 交互 | `POST /ai/chat` `POST /ai/actions/:id/approve` |
| 8. 数据录入 | `POST /stores/:id/daily-data` `POST /ai/ocr/store-data` |

完整 API 定义将在 Phase 4 产出到 `docs/api-contract.md`。
