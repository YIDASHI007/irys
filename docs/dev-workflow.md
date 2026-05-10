# 🚀 Irys 项目 · 零基础开发步骤清单

> **这是你的主开发手册。每天打开它,从上往下做。**
>
> 📍 **配套文档**:
> - 做页面时查 [`docs/page-structure.md`](./page-structure.md) - 完整页面结构树
> - 找功能文档查 [`docs/dev-index.md`](./dev-index.md) - 功能索引表
> - Cursor 自动读取 [`.cursorrules`](../.cursorrules) - AI 规则
>
> 📌 **使用说明**:
> 1. 从 Step 1 开始,一步一步做
> 2. 每步完成后,**对照验收清单打勾** ✅
> 3. 全部打勾后,才进入下一步
> 4. 如果有步骤卡住,来问我(别硬扛超过 30 分钟)
> 5. 每完成一步,记得 `git commit + push`
>
> **⚠️ 重要心理准备**:
> - 这份清单覆盖 **6 个月** 的开发
> - 你完全做完大约 **80-100 步**
> - 今天能做 1-2 步就是胜利
> - 有步骤你做不完很正常,去问 AI 或我
>
> 🎯 **每步的结构**:
> ```
> Step X · [功能名称]        ⏱️ 预计耗时
>   📌 目标(做完什么样)
>   📋 准备工作(装什么/读什么)
>   💬 给 AI 的提示词(直接复制)
>   ✅ 验收清单(全打勾才能下一步)
>   💡 卡住了怎么办
>   🔗 相关文档
> ```

---

## 📊 总进度速览

```
🏁 准备阶段 (Step 1-5)                    约 1 周
🏗️  Phase A · 项目骨架 (Step 6-10)         约 1 周
👤 Phase B · 账号权限 M1 (Step 11-20)     约 2-3 周
🏠 Phase C · 工作台 M2 (Step 21-25)       约 1 周
📞 Phase D · CRM M3 (Step 26-35)          约 3 周
🏢 Phase E · 招商 M4 + 加盟商 M5 (Step 36-45)   约 3 周
🏪 Phase F · 门店 M6 (Step 46-55)         约 2 周
📝 Phase G · 合同 M7 (Step 56-62)         约 2 周
🤖 Phase H · AI M14 (Step 63-73)          约 3 周
🖼️  Phase I · AI OCR M15 (Step 74-80)      约 2 周
📊 Phase J · 看板 + 其他 (Step 81-88)     约 2 周
🚢 Phase K · 部署上线 (Step 89-92)        约 1 周
────────────────────────────────────
总计 约 6 个月(每天投入 3-4 小时)
```

---

# 🏁 准备阶段

## Step 1 · 搭建开发环境

⏱️ 预计耗时:**半天到 1 天**

### 📌 目标
你的电脑上能用 Cursor 打开 Irys 项目,能执行命令。

### 📋 准备工作

#### 1. 安装软件(按顺序装)
- [ ] **Cursor** - https://cursor.com (主力编辑器)
- [ ] **Node.js 20+** - https://nodejs.org
- [ ] **Git** - https://git-scm.com
- [ ] **GitHub Desktop** - https://desktop.github.com
- [ ] **pnpm** - 装完 Node.js 后运行:`npm install -g pnpm`
- [ ] **Docker Desktop** - https://docker.com (用于数据库)

#### 2. 注册账号
- [ ] GitHub 账号(你已经有了)
- [ ] **月之暗面 Kimi 开放平台** - https://platform.moonshot.cn
  - 实名认证
  - 充值 ¥50 足够你开发期间用
  - 新建 API Key,妥善保存

#### 3. 买(或准备)
- [ ] Cursor Pro 订阅 ¥150/月(14 天免费)
- [ ] 先不用买服务器/域名

### 💬 验证环境(给 AI 的提示词)

**如果你遇到安装问题,用这个提示词问 Cursor**:

```
我是编程小白,按照 docs/dev-workflow.md 的 Step 1 在装环境。

我的操作系统:[Mac / Windows 写清楚]
我刚装完:[你装的软件]
我遇到的问题:[完整描述 + 错误截图]

请:
1. 用白话告诉我这个错误是什么意思
2. 给我 3 种从简单到复杂的解决方案
3. 不要让我装我没装的软件
```

### ✅ 验收清单

- [ ] 打开终端(Mac:Terminal / Win:PowerShell)能运行 `node -v` 显示 v20.x
- [ ] `pnpm -v` 能正常显示
- [ ] `git --version` 能正常显示
- [ ] Cursor 能打开,左边有文件目录
- [ ] GitHub Desktop 能登录你的账号
- [ ] Docker Desktop 启动后小图标常亮(鲸鱼图标)
- [ ] 你有 Kimi API Key 了(保存在密码管理器或记事本)
- [ ] **最重要**:你能从上面随便选一个软件截图给朋友看,说"我装好了"

### 💡 卡住了怎么办
- Mac 装 Node 建议用 `nvm` 方式,搜"nvm mac 安装"
- Windows 装 Git 全部默认下一步即可
- Docker 在 Windows 可能需要开启 WSL2,搜"WSL2 安装"
- **最终杀手锏**:问 Cursor,粘贴完整错误给它

---

## Step 2 · 克隆你自己的仓库到本地

⏱️ 预计耗时:**30 分钟**

### 📌 目标
你的电脑里有 Irys 仓库,能用 Cursor 打开。

### 📋 准备工作
已经完成 Step 1。

### 💬 操作步骤

1. 打开 **GitHub Desktop**
2. 点 `File → Clone repository`
3. 选 `YIDASHI007/irys`
4. 选择本地保存位置(推荐:桌面或 `/Users/你/projects/irys`)
5. 点 `Clone`

**选择分支**:
- 右上角点 `Current Branch`
- 切换到 `docs/phase1-m15-ai-ocr`(包含最新文档)

**用 Cursor 打开**:
- 点 Cursor 中 `File → Open Folder`
- 选择刚才 clone 的 `irys` 文件夹
- Cursor 左边应该能看到 `docs/`、`.cursorrules` 等

### ✅ 验收清单

- [ ] 电脑桌面或指定位置有 `irys` 文件夹
- [ ] 文件夹里能看到 `README.md`、`docs/`
- [ ] Cursor 打开该文件夹,左边文件树正常显示
- [ ] `.cursorrules` 文件存在(可能是隐藏文件,在 Cursor 里能看到)
- [ ] 在 Cursor 里能点开 `docs/requirements.md` 看到内容

### 💡 卡住了怎么办
- 找不到 `.cursorrules`?它是隐藏文件,Mac 用 `Cmd+Shift+.` 显示隐藏文件
- Cursor 打开项目后没有激活 `.cursorrules`?重启 Cursor

---

## Step 3 · 让 Cursor "认识" 你的项目

⏱️ 预计耗时:**15 分钟**

### 📌 目标
测试 Cursor 能读懂你的项目文档,AI 会按小白模式回答。

### 💬 给 AI 的提示词(复制到 Cursor 的 Ctrl+L 聊天窗口)

```
我刚刚第一次打开这个 Irys 项目。
请你:
1. 读取 .cursorrules 文件
2. 读取 docs/requirements.md 的前 100 行
3. 读取 docs/dev-workflow.md 的前 50 行

然后告诉我:
1. 我是什么身份(小白还是资深)?
2. 这个项目技术栈是什么?
3. 我接下来应该做什么?(看 dev-workflow.md 现在到哪一步)

用 3 段中文回答,每段不超过 100 字。
```

### ✅ 验收清单

- [ ] Cursor 回答里明确说"你是小白"
- [ ] 回答里列出了 NestJS + Vue 3 等关键技术
- [ ] 回答里告诉你下一步是 Step 4
- [ ] 你能感觉到 AI 在按"小白模式"回复你

### 💡 卡住了怎么办
- 如果 AI 给你高深代码 → 它没读 `.cursorrules`,重新点 Ctrl+L,明确说"先读 .cursorrules"
- 如果 AI 不用中文 → 再次强调"请用中文回答"

---

## Step 4 · 配置 Kimi API Key 到环境变量

⏱️ 预计耗时:**15 分钟**

### 📌 目标
创建 `.env` 文件存放你的 Kimi API Key,后续所有代码可以用。

### 📋 准备工作
- 你已经有 Kimi API Key(在 Step 1 拿到)

### 💬 给 AI 的提示词

```
我是小白,刚搭好 Irys 项目环境。
我需要创建一个 .env 文件来存 Kimi API Key。

请:
1. 在项目根目录帮我创建 .env.example(示例,不填真实值,可以 commit 到 git)
2. 在项目根目录帮我创建 .env(填入我的真实值,不 commit)
3. 创建/修改 .gitignore 确保 .env 不会被提交
4. 文件内容要包含:
   - KIMI_API_KEY(AI 模型 Key)
   - DATABASE_URL(数据库连接字符串,暂时写 SQLite)
   - JWT_SECRET(随机字符串,你帮我生成一个)
   - AI_ENCRYPTION_KEY(32 字节 hex,你帮我生成一个)

每个变量加中文注释说明用途。
最后告诉我:
- 哪些是必须我填的
- 哪些你已经帮我生成了
```

然后:

```
生成好后,打开 .env 文件,
把 KIMI_API_KEY=sk-xxxxx 中的 xxxxx 替换成我的 Key
(我不告诉你我的 Key,我自己填)
```

### ✅ 验收清单

- [ ] 项目根目录有 `.env` 文件(你能看到,但 Git 不会跟踪)
- [ ] 项目根目录有 `.env.example` 文件(Git 会跟踪)
- [ ] `.gitignore` 里有 `.env` 这一行
- [ ] `.env` 里有 `KIMI_API_KEY=sk-你的真实 Key`
- [ ] `JWT_SECRET` 和 `AI_ENCRYPTION_KEY` 都有值(不是空的)
- [ ] **运行 `git status`,看不到 `.env` 文件**(说明被 ignore 了)

### 💡 卡住了怎么办
- `.env` 不见了?它被隐藏了,Cursor 里能看到
- 不知道 Kimi API Key 怎么生成?去 https://platform.moonshot.cn/console/api-keys
- Git 把 .env 跟踪了?运行 `git rm --cached .env` 再改 .gitignore

### 🔒 安全提醒
**永远不要把 `.env` 文件推到 GitHub!**
如果不小心推上去了,立即:
1. 去 Kimi 控制台删掉该 Key,重新生成
2. 问 AI 如何从 git 历史中移除该文件

---

## Step 5 · 做一次 "Hello World"(热身)

⏱️ 预计耗时:**1 小时**

### 📌 目标
在真正开干之前,体验一次"从 0 到浏览器显示"的完整流程。

### 💬 给 AI 的提示词

```
我是完全的编程小白,第一次做项目。
在开始 Irys 之前,我想先做一个超简单的 Hello World 练手。

请在项目里创建一个临时的 hello-world/ 文件夹,里面:
1. 一个 index.html
2. 一个按钮,点击后显示"我是 [你的名字],今天开始学编程!"(名字先写"小白")
3. 用最基础的 HTML + CSS + JS,不用任何框架
4. 代码不超过 50 行
5. 每行关键代码用中文注释

生成后,告诉我:
- 文件在哪里
- 怎么打开看(比如双击)
- 我改哪一行能改名字
```

### ✅ 验收清单

- [ ] 项目里有 `hello-world/index.html`
- [ ] 双击打开,浏览器能看到一个页面
- [ ] 页面上有个按钮
- [ ] 点按钮会弹出文字
- [ ] 你能修改代码里的名字,刷新后生效
- [ ] **你感受到了**"写代码 → 看到结果"的快乐 😊

### 💡 卡住了怎么办
- 双击 html 没反应?用 Cursor 右键 `Open with Live Server` 插件
- 中文乱码?HTML 头部加 `<meta charset="UTF-8">`

### 🎉 里程碑
**做完这一步,你已经走出最难的第一步了!** 后面都是这个感觉的放大版。

💾 **保存进度**:
```
git add hello-world/ .env.example .gitignore
git commit -m "chore: Step 1-5 环境搭建完成"
git push
```

---

# 🏗️ Phase A · 项目骨架(Step 6-10)

> 这一阶段的目标:把 Irys 项目真正的骨架搭起来,前后端能各自启动一个"空壳"。
> **不要实现任何业务功能**。只做地基。

## Step 6 · 初始化 pnpm Monorepo

⏱️ 预计耗时:**2 小时**

### 📌 目标
项目有标准的 monorepo 结构,pnpm workspace 配置正确。

### 📋 相关文档
- `docs/requirements.md` §8 技术栈
- `docs/dev-index.md` "Monorepo 结构"

### 💬 给 AI 的提示词

```
我要搭建 Irys 项目的 monorepo 骨架。

【我是】编程小白
【技术要求】
- pnpm workspace
- 不用 Turborepo(简单点,后期再加)

【期望目录结构】
irys/
├── apps/
│   ├── backend/          (NestJS,后面的 Step 做)
│   ├── admin/            (Vue 3,后面的 Step 做)
│   └── mini/             (uni-app,后面的 Step 做)
├── packages/
│   ├── shared-types/     (共享 TypeScript 类型)
│   └── shared-utils/     (共享工具函数)
├── docs/                 (已存在)
├── package.json          (root)
├── pnpm-workspace.yaml
└── .env.example          (已存在)

【本步只做】
1. 创建 apps/ 和 packages/ 空目录(带 .gitkeep)
2. 创建 root package.json(只写基本信息,不装依赖)
3. 创建 pnpm-workspace.yaml
4. 修改根目录的 .gitignore,忽略 node_modules/、dist/、.env

【不要做】
- 不要现在初始化 backend / admin / mini
- 不要装任何 npm 包
- 不要写任何业务代码

完成后告诉我:
1. 创建了哪些文件
2. 怎么测试 pnpm workspace 配置对不对
```

### ✅ 验收清单

- [ ] 项目有 `apps/` 目录(空但有 .gitkeep)
- [ ] 项目有 `packages/` 目录(空但有 .gitkeep)
- [ ] 根目录有 `package.json`
- [ ] 根目录有 `pnpm-workspace.yaml`
- [ ] 运行 `pnpm install`(空安装)不报错
- [ ] 运行 `pnpm list --depth 0` 能看到 workspace 标识

### 💡 卡住了怎么办
- pnpm 命令找不到?`npm install -g pnpm`
- Workspace 不识别?看 pnpm-workspace.yaml 缩进,YAML 对缩进敏感

💾 保存:`git add . && git commit -m "feat(a): Step 6 初始化 monorepo 骨架" && git push`

---

## Step 7 · 创建共享包 shared-types

⏱️ 预计耗时:**1 小时**

### 📌 目标
有一个 `packages/shared-types`,里面放 Irys 的所有枚举(从需求文档来)。

### 📋 相关文档
- `docs/requirements.md` §9 核心数据实体
- `docs/business-rules.md`(各种状态枚举)

### 💬 给 AI 的提示词

```
我要创建 packages/shared-types 共享类型包。
这个包存放前后端共用的 TypeScript 枚举。

【本步只做】
1. 在 packages/shared-types/ 下初始化 package.json
   - 名字: @irys/shared-types
   - 版本: 0.0.1
   - 入口: src/index.ts
2. 创建 tsconfig.json(最简配置)
3. 创建 src/index.ts,里面导出以下枚举:

必需枚举(来自需求文档):

// 用户角色
enum UserRole {
  SUPER_ADMIN, OPS_MANAGER, SALES, FINANCE,
  REVIEWER, CONTENT_EDITOR, MERCHANT_OWNER,
  STORE_STAFF, EXTERNAL_USER
}

// 数据权限范围
enum DataScope { ALL, DEPARTMENT, SELF, CUSTOM }

// 线索状态(BR-202)
enum LeadStatus { NEW, CONTACTED, INTENTIONAL, INVALID, CONVERTED }

// 线索来源
enum LeadSource { MINI_PROGRAM, WEBSITE, PHONE, EXHIBITION, REFERRAL, MANUAL }

// 招商项目状态(BR-301)
enum ProjectStatus { DRAFT, RECRUITING, PAUSED, CLOSED }

// 加盟商状态(BR-402)
enum MerchantStatus { ACTIVE, SUSPENDED, TERMINATED }

// 加盟商等级
enum MerchantLevel { GOLD, SILVER, BRONZE }

// 门店生命周期(BR-501)
enum StoreStatus {
  PLANNING, SIGNING, DECORATING, TRAINING,
  SOFT_OPENING, OPENED, CLOSED
}

// 合同状态(BR-601)
enum ContractStatus {
  DRAFT, APPROVING, SIGNED, EXECUTING,
  EXPIRED, TERMINATED
}

// AI 操作状态
enum ActionStatus {
  PENDING, APPROVED, EXECUTED, FAILED,
  REJECTED, EXPIRED
}

// AI 操作风险等级
enum ActionSeverity { LOW, MEDIUM, HIGH }

// 数据源(门店每日数据 BR-506)
enum DataSource { API, EMAIL, RPA, AI_OCR, MANUAL }

// OCR 场景(M15,MVP 仅第一个)
enum OCRScene {
  STORE_DAILY_DATA,    // MVP
  CONTRACT_SCAN,       // v2 预留
  ID_CARD,
  BUSINESS_LICENSE,
  RECEIPT
}

// OCR Job 状态
enum OCRJobStatus {
  PENDING, AI_PROCESSING, AI_FAILED,
  AWAITING_REVIEW, REVIEWING, CONFIRMED,
  REJECTED, ABANDONED, ANOMALY_FLAGGED
}

4. 每个枚举上方加中文注释,说明对应的 BR 编号或需求文档章节

【不要做】
- 不要实现任何 DTO、接口、工具函数
- 不要装 class-validator 等库

最后告诉我:
1. 创建了哪些文件
2. 怎么验证这个包在根目录可用(比如 pnpm 命令)
```

### ✅ 验收清单

- [ ] `packages/shared-types/package.json` 存在
- [ ] `packages/shared-types/src/index.ts` 存在
- [ ] 打开 `index.ts`,能看到上面所有枚举
- [ ] 每个枚举有中文注释
- [ ] 在根目录运行 `pnpm -F @irys/shared-types build` 能成功(或至少不报错)

💾 保存:`git commit -m "feat(a): Step 7 创建 shared-types 包" && git push`

---

## Step 8 · 初始化后端项目(NestJS 空架子)

⏱️ 预计耗时:**2-3 小时**

### 📌 目标
`apps/backend` 能启动,访问 `http://localhost:3000/health` 能看到 `{"status":"ok"}`。

### 📋 相关文档
- `docs/requirements.md` §8 后端技术栈

### 💬 给 AI 的提示词

```
我要初始化 apps/backend NestJS 项目。

【目标】
能启动,访问 /health 返回 {"status":"ok","timestamp":"..."}

【本步做什么】
1. 用 NestJS CLI 初始化项目:
   cd apps/backend
   nest new . --package-manager pnpm --skip-install --skip-git --language TypeScript

2. 修改 package.json:
   - name: @irys/backend
   - 添加 pnpm-workspace 支持
   - 装 @irys/shared-types workspace 依赖

3. 创建 HealthController,只有一个 /health GET 接口

4. 修改 src/main.ts:
   - 启用 CORS
   - 启用全局 ValidationPipe
   - 端口从环境变量读(默认 3000)
   - 加一条启动日志:"🚀 Backend ready at http://localhost:3000"

5. 在 .env.example 根目录和 apps/backend/.env 里添加:
   PORT=3000

【不要做】
- 不要装 Prisma / Redis(下一步做)
- 不要做 JWT / 鉴权(后面做)
- 不要写 User/Lead 等业务模型

最后告诉我:
1. 改了哪些文件
2. 需要装哪些包(逐条列出,我自己装)
3. 怎么启动(具体到运行哪个 pnpm 命令)
4. 怎么验证(浏览器访问什么地址)
```

**当 AI 告诉你"装哪些包"后,你逐条在终端执行,比如:**

```bash
cd apps/backend
pnpm add @nestjs/common @nestjs/core @nestjs/platform-express
# (实际包名以 AI 给的为准)
```

### ✅ 验收清单

- [ ] `apps/backend/src/main.ts` 存在
- [ ] `apps/backend/package.json` 存在
- [ ] 运行 `pnpm install` 成功
- [ ] 运行 `pnpm -F @irys/backend start:dev` 能看到启动日志
- [ ] 浏览器访问 `http://localhost:3000/health`,看到 JSON 响应
- [ ] 控制台没有红色报错

### 💡 卡住了怎么办
- 端口被占用?改 PORT=3001 或杀掉占用进程
- `nest` 命令不存在?`pnpm add -g @nestjs/cli` 或在 apps/backend 里用 `pnpm exec nest`
- 启动后白屏?`/health` 是 API,不是网页,直接在地址栏访问应该看到 JSON

💾 保存:`git commit -m "feat(a): Step 8 backend 骨架 + /health 接口"`

---

## Step 9 · 初始化前端项目(Vue 3 空架子)

⏱️ 预计耗时:**2-3 小时**

### 📌 目标
`apps/admin` 能启动,访问 `http://localhost:5173` 能看到 "Irys 后台管理系统"。

### 💬 给 AI 的提示词

```
我要初始化 apps/admin Vue 3 前端项目。

【目标】
浏览器访问 localhost:5173,看到 "Irys 后台管理系统" 首页。

【本步做什么】
1. 在 apps/admin 下用 Vite 创建 Vue 3 + TypeScript 项目:
   cd apps/admin
   pnpm create vite . --template vue-ts

2. 修改 package.json:
   - name: @irys/admin
   - 装 @irys/shared-types 依赖(workspace)

3. 安装 Element Plus:
   pnpm add element-plus
   pnpm add @element-plus/icons-vue

4. 安装 Vue Router 和 Pinia:
   pnpm add vue-router@4 pinia

5. 安装 Axios:
   pnpm add axios

6. 修改 src/main.ts,引入 Element Plus

7. 创建一个最简单的 src/App.vue,显示:
   - el-container 布局
   - Header: "Irys 企业管理后台"
   - Main: "Welcome"
   - Footer: "v0.0.1"

8. 配置环境变量:
   - apps/admin/.env.development: VITE_API_BASE_URL=http://localhost:3000

【不要做】
- 不要做登录、路由、鉴权(后续步骤做)
- 不要装 VueQuery / SWR 等

最后告诉我:
1. 改了哪些文件
2. 装了哪些包
3. 怎么启动
4. 浏览器看什么
```

### ✅ 验收清单

- [ ] `apps/admin/src/App.vue` 存在且被修改
- [ ] `apps/admin/package.json` 存在
- [ ] `pnpm -F @irys/admin dev` 能启动
- [ ] 浏览器访问 `http://localhost:5173` 看到布局页
- [ ] 页面上显示"Irys 企业管理后台"
- [ ] 没有红色 Element Plus 警告

💾 保存:`git commit -m "feat(a): Step 9 admin 骨架 + Element Plus"`

---

## Step 10 · 前后端连通第一次(联调测试)

⏱️ 预计耗时:**1 小时**

### 📌 目标
前端按一个按钮,能调用后端 `/health`,页面显示结果。
**这一步是最爽的一步**,你会看到"前后端真的连起来了"。

### 💬 给 AI 的提示词

```
我要验证前后端能通信。

【当前状态】
- 后端 apps/backend 运行在 localhost:3000,有 /health 接口
- 前端 apps/admin 运行在 localhost:5173
- 两个都能独立启动了

【本步做什么】
1. 在 apps/admin/src 下创建 api/ 目录
2. 创建 api/client.ts,封装 axios:
   - baseURL 从 import.meta.env.VITE_API_BASE_URL 读取
   - 请求超时 10 秒
   - 加基础的 response interceptor
3. 创建 api/health.ts,导出 checkHealth() 函数
4. 修改 App.vue:
   - 加一个 Element Plus 的 Button,文案"测试后端连接"
   - 加一个文本框显示结果
   - 点击按钮 → 调用 checkHealth() → 显示返回的 JSON

5. 解决 CORS 问题:
   - 如果前端调用后端被 CORS 拦截,修改后端 main.ts 允许 localhost:5173

【不要做】
- 不要现在做统一错误处理(简单 try-catch 即可)
- 不要做 loading 动画
- 不要加 TypeScript 严格类型(能跑就行)

最后告诉我:
1. 我点按钮后,预期看到什么?
2. 如果没看到,第一步排查什么?
```

### ✅ 验收清单

- [ ] 前端有个"测试后端连接"按钮
- [ ] 点击按钮后,页面显示 `{"status":"ok","timestamp":"..."}` 或类似
- [ ] 浏览器开发者工具(F12)→ Network 标签,看到 /health 请求 200
- [ ] 没有 CORS 红色错误

### 💡 卡住了怎么办
- CORS 报错?最常见,让 AI 修改后端 `main.ts` 的 CORS 配置
- 按钮没反应?F12 看 Console 有什么错
- 后端没启动?要同时开两个终端:一个跑 backend,一个跑 admin

### 🎉 里程碑
**Phase A 完成!你有了一个可跑的前后端项目!**

💾 保存:
```
git add .
git commit -m "feat(a): Step 10 前后端联调跑通 ✨"
git push
```

---

# 👤 Phase B · 账号权限(M1)· Step 11-20

> 这一阶段目标:完成整个账号权限体系。
> 完成后你能:登录进系统、管理员工、分配角色。

## Step 11 · Prisma + 数据库初始化

⏱️ 预计耗时:**2 小时**

### 📌 目标
项目集成 Prisma,创建第一个 User 表,能往数据库写数据。

### 📋 相关文档
- `docs/requirements.md` M1.2 员工账号
- `docs/business-rules.md` BR-101, BR-1201, BR-1203

### 💬 给 AI 的提示词

```
我要给 backend 集成 Prisma 和数据库。

【使用策略】
- 开发环境:SQLite(零配置,文件存储,方便)
- 生产环境:PostgreSQL(代码兼容,部署时切换)

【本步做什么】
1. 在 apps/backend/ 初始化 Prisma:
   pnpm add -D prisma
   pnpm add @prisma/client
   pnpm exec prisma init --datasource-provider sqlite

2. 修改 prisma/schema.prisma,添加 User 模型:
   - id: String (cuid)
   - phone: String (unique,BR-101 手机号全局唯一)
   - name: String
   - passwordHash: String
   - status: String (ACTIVE/DISABLED)
   - tenantId: String (BR-1203 多租户预留,默认 "default")
   - createdAt: DateTime
   - updatedAt: DateTime
   - deletedAt: DateTime? (BR-1201 软删除)

3. 执行 migration:
   pnpm exec prisma migrate dev --name init

4. 创建 PrismaService:
   - src/prisma/prisma.service.ts
   - 继承 PrismaClient
   - 启动时 $connect,关闭时 $disconnect
   
5. 创建 PrismaModule(全局模块)

6. 验证:
   - 给 HealthController 加一个 /health/db 接口
   - 返回 User 表的记录数

【不要做】
- 不要现在做 User CRUD 接口(下一步做)
- 不要做复杂的种子数据
- 先只做 User 表,Role/Permission 等后面再加

最后告诉我:
1. 改了哪些文件
2. .env 需要什么新变量(DATABASE_URL)
3. 怎么用 Prisma Studio 查看数据库(命令)
4. 如果要清空数据库怎么做
```

### ✅ 验收清单

- [ ] `apps/backend/prisma/schema.prisma` 存在,包含 User 模型
- [ ] `apps/backend/prisma/migrations/` 有文件
- [ ] `apps/backend/prisma/dev.db`(SQLite 文件)存在
- [ ] 启动 `pnpm exec prisma studio` 能打开数据库可视化界面
- [ ] 访问 `http://localhost:3000/health/db` 返回 `{count: 0}`

💾 保存:`git commit -m "feat(b): Step 11 集成 Prisma + User 表"`

---

## Step 12 · 实现"注册"功能(最简版)

⏱️ 预计耗时:**3 小时**

### 📌 目标
后端有 `POST /auth/register` 接口,能创建用户并把密码加密存库。

### 📋 相关文档
- `docs/requirements.md` M1.2, M1.5
- `docs/business-rules.md` BR-101, BR-103

### 💬 给 AI 的提示词

```
我要实现注册接口。

【目标】
POST /auth/register
  Body: { phone, name, password }
  返回: { id, phone, name } (不返回密码!)

【业务规则】
- BR-101: 手机号全局唯一
- BR-103: 密码至少 8 位,必须包含字母 + 数字

【本步做什么】
1. 装依赖:
   pnpm add bcrypt
   pnpm add -D @types/bcrypt
   pnpm add class-validator class-transformer

2. 创建 src/modules/auth 目录,里面:
   - dto/register.dto.ts (用 class-validator 验证)
   - auth.service.ts
   - auth.controller.ts
   - auth.module.ts

3. RegisterDto 要求:
   - phone: 手机号格式,必填
   - name: 1-20 字符,必填
   - password: 至少 8 位,必须含字母+数字(自定义 validator,标注 BR-103)

4. auth.service.ts 的 register() 方法:
   - 先查手机号是否已存在 → 存在就抛 ConflictException("该手机号已注册")
   - 用 bcrypt(10 轮)哈希密码
   - 写入数据库
   - 返回脱敏后的 User(不含 passwordHash)

5. auth.controller.ts:
   - POST /auth/register 绑定 register
   - 用 @Body() + DTO

6. 把 AuthModule 注册到 AppModule

【不要做】
- 不要做登录接口(下一步)
- 不要做 JWT
- 不要做短信验证码

测试方法:
- 用 curl 或 Postman 测:
  POST http://localhost:3000/auth/register
  body: {"phone":"13800000000","name":"小白","password":"Aa123456"}
- 用 prisma studio 查看数据库有这条记录
- 再次同样请求应该报错 "该手机号已注册"
- 密码太短(如 "123")应该报 BR-103 错误

最后告诉我:
1. 改了哪些文件
2. 装了哪些包
3. 用 curl 具体怎么测
```

### ✅ 验收清单

- [ ] 后端有 `POST /auth/register` 接口
- [ ] 用 Postman 发送正确请求,返回 200 + 用户信息(不含密码)
- [ ] 数据库里能看到新用户,`passwordHash` 字段是 bcrypt 哈希(不是明文!)
- [ ] 重复注册同一手机号,返回 409 冲突
- [ ] 密码 "123" 注册,返回 400 校验失败
- [ ] 密码 "abcdefgh"(无数字)注册,返回 400(BR-103)

💾 保存:`git commit -m "feat(b): Step 12 注册接口 + BR-101/103"`

---

## Step 13 · 实现"登录"功能(JWT)

⏱️ 预计耗时:**4 小时**(JWT 是新概念,要多理解)

### 📌 目标
`POST /auth/login` 接口返回 JWT Token,前端拿到后可以访问受保护接口。

### 📋 相关文档
- `docs/requirements.md` M1.5
- `docs/business-rules.md` BR-104, BR-105

### 💬 给 AI 的提示词

```
我要实现登录功能。

【目标】
POST /auth/login
  Body: { phone, password }
  返回: { accessToken, refreshToken, user }

保护接口能通过 Authorization: Bearer <token> 访问。

【业务规则】
- BR-104: 连续失败 5 次锁 15 分钟
- BR-105: Access 2 小时, Refresh 7 天

【本步做什么】
1. 装依赖:
   pnpm add @nestjs/jwt @nestjs/passport passport passport-jwt
   pnpm add -D @types/passport-jwt

2. 给 User 表加字段(需要做 migration):
   - loginFailedCount: Int (默认 0)
   - lockedUntil: DateTime?

3. 修改 auth.service.ts,添加 login():
   - 查用户 → 不存在抛 Unauthorized
   - 检查是否被锁(lockedUntil > now) → 抛错"已锁定,N 分钟后重试"
   - bcrypt 比对密码:
     - 不匹配 → loginFailedCount++,如果 ≥5 设置 lockedUntil=now+15min,写数据库,抛 Unauthorized
     - 匹配 → 清零失败次数,签发 JWT
   - 签发两个 Token:
     - Access: sub=userId, type='access', 2 小时过期
     - Refresh: sub=userId, type='refresh', 7 天过期

4. 创建 JwtStrategy(passport-jwt):
   - 验证 Bearer Token
   - 从数据库查 User,挂到 request.user

5. 创建 AuthGuard:
   - @UseGuards(AuthGuard('jwt')) 就能保护接口

6. 给 HealthController 加个 /health/me 接口:
   - 用 AuthGuard 保护
   - 返回当前登录用户的 name 和 phone

7. JWT_SECRET 从 .env 读

【不要做】
- 不要做 Refresh Token 刷新接口(下一步)
- 不要做登出接口
- 不要做短信登录

测试:
- 注册一个用户 → 登录 → 拿到 token
- 用 token 访问 /health/me → 200
- 不带 token 访问 /health/me → 401
- 错误密码登录 5 次 → 第 6 次应该报"已锁定"

最后告诉我:
1. 改了哪些文件
2. 需要做 prisma migrate 吗?
3. 用 Postman 怎么测
```

### ✅ 验收清单

- [ ] 正常登录返回 accessToken 和 refreshToken
- [ ] 带 Bearer Token 访问 `/health/me` 成功
- [ ] 不带 Token 访问 `/health/me` 返回 401
- [ ] 连续 5 次错误密码,第 6 次报锁定
- [ ] 15 分钟后自动解锁(可手动改数据库的 `lockedUntil` 快速测试)

### 💡 卡住了怎么办
- JWT 不理解?问 AI:"用快递取件码的比喻讲 JWT"
- Postman 不会用?搜"Postman 带 Bearer Token"

💾 保存:`git commit -m "feat(b): Step 13 登录 + JWT + BR-104/105"`

---

## Step 14 · 前端登录页面

⏱️ 预计耗时:**3 小时**

### 📌 目标
前端有 `/login` 页面,输入账号密码能真实登录,Token 存 localStorage,跳转到首页。

### 💬 给 AI 的提示词

```
我要做登录页面(前端)。

【目标】
- 访问 http://localhost:5173/login
- 输入手机号 + 密码 → 登录成功后 Token 存 localStorage → 跳转到 /
- 登录失败显示具体错误消息

【本步做什么】
1. 安装路由:
   - 配置 Vue Router(如果还没)
   - 路由:
     - /login → Login.vue
     - / → Home.vue(需登录)

2. 创建 Pinia store:
   - src/stores/auth.ts
   - state: token, user
   - action: login(phone, password), logout()
   - 持久化到 localStorage

3. 创建 views/Login.vue:
   - Element Plus 的 el-form
   - 手机号输入框(前端也做格式校验)
   - 密码输入框(type=password)
   - 登录按钮(loading 状态)
   - 失败消息显示

4. 创建 views/Home.vue:
   - 显示"欢迎回来, {user.name}"
   - 退出登录按钮

5. Axios 拦截器:
   - Request: 自动带 Authorization
   - Response 401: 清除 token,跳回 /login

6. 路由守卫:
   - / 需要登录(router.beforeEach 检查 token)
   - 未登录跳 /login

【不要做】
- 不要做"记住我"
- 不要做"忘记密码"
- 不要做注册页(注册已有后端接口,用户手动用 Postman 创建即可)

测试流程:
1. 用 Postman 注册一个用户 13800000000 / Aa123456
2. 前端打开 /login
3. 登录 → 看到首页
4. 刷新页面,还是登录状态(因为 token 在 localStorage)
5. 退出登录 → 跳回 /login

最后告诉我:
1. 改了哪些文件
2. 装了什么新包
3. 怎么测试
```

### ✅ 验收清单

- [ ] 访问 `/` 未登录会自动跳到 `/login`
- [ ] 输入错误账号密码显示错误
- [ ] 登录成功跳到 `/`,看到用户姓名
- [ ] 刷新浏览器,还是登录状态
- [ ] 点退出登录,跳回 `/login`,localStorage 里 token 被清除

💾 保存:`git commit -m "feat(b): Step 14 前端登录页 ✨"`

### 🎉 里程碑
**你的系统可以登录了!这是整个项目最有成就感的一刻!**

---

## Step 15 · 角色和权限模型设计

⏱️ 预计耗时:**2 小时**

### 📌 目标
设计 Role、Permission 表结构并创建,为后续权限控制打底。

### 📋 相关文档
- `docs/requirements.md` M1.3
- `docs/business-rules.md` BR-106, BR-107

### 💬 给 AI 的提示词

```
我要设计角色权限模型。

【理念】
- 权限基于"权限点"(permission code),如 lead:read, lead:write
- 角色是权限点的集合
- 用户可以有多个角色

【本步做什么】(只建表,不实现逻辑)

1. Prisma schema 添加:

model Role {
  id          String   @id @default(cuid())
  code        String   @unique   // "SUPER_ADMIN" / "SALES" etc
  name        String              // "超级管理员" / "销售"
  description String?
  isBuiltIn   Boolean  @default(false)   // 内置角色不可删
  dataScope   String   @default("SELF")   // ALL/DEPARTMENT/SELF/CUSTOM
  tenantId    String   @default("default")
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
  
  permissions RolePermission[]
  users       UserRole[]
}

model Permission {
  id          String   @id @default(cuid())
  code        String   @unique   // "lead:read"
  name        String              // "查看线索"
  module      String              // "M3"
  group       String?             // "CRM"
  createdAt   DateTime @default(now())
  
  roles       RolePermission[]
}

model UserRole {
  userId      String
  roleId      String
  assignedAt  DateTime @default(now())
  
  user        User @relation(fields: [userId], references: [id])
  role        Role @relation(fields: [roleId], references: [id])
  
  @@id([userId, roleId])
}

model RolePermission {
  roleId          String
  permissionId    String
  
  role            Role @relation(fields: [roleId], references: [id])
  permission      Permission @relation(fields: [permissionId], references: [id])
  
  @@id([roleId, permissionId])
}

别忘了 User 模型加 `roles UserRole[]`

2. 执行 migration: `prisma migrate dev --name role-permission`

3. 创建 seed 文件 prisma/seed.ts:
   - 内置 7 种角色: SUPER_ADMIN, OPS_MANAGER, SALES, FINANCE, REVIEWER, CONTENT_EDITOR, MERCHANT_OWNER
   - 内置约 30 个权限点(列出主要模块的 read/write):
     - user:read, user:write
     - role:read, role:write
     - lead:read, lead:write, lead:assign
     - store:read, store:write
     - contract:read, contract:write, contract:approve
     - finance:read, finance:write
     - ai:use
     - ai_ocr:use (仅 SUPER_ADMIN)
     - ...
   - 给 SUPER_ADMIN 分配所有权限
   - 给 SALES 分配 lead:read, lead:write, ai:use
   - 其他角色也做基础配置

4. 配置 package.json:
   "prisma": {
     "seed": "ts-node prisma/seed.ts"
   }

5. 执行 seed: `pnpm exec prisma db seed`

【不要做】
- 不要现在做角色 CRUD 接口(下一步)
- 不要改登录逻辑
- 不要做前端

测试:
- prisma studio 能看到 Role、Permission 表有数据
- 7 个内置角色都在
- SUPER_ADMIN 角色有所有权限关联

最后告诉我:
1. 改了哪些文件
2. 怎么重置数据库重新 seed
```

### ✅ 验收清单

- [ ] Prisma 生成了 4 个新表
- [ ] `pnpm exec prisma db seed` 成功
- [ ] Prisma Studio 能看到 7 个角色 + 30 左右权限
- [ ] SUPER_ADMIN 的权限最多(看 `RolePermission` 关联)

💾 保存:`git commit -m "feat(b): Step 15 角色权限模型 + seed"`

---

## Step 16-20 · 完成 M1 账号权限模块

> 为节省篇幅,后续步骤简化写。每步的详细提示词用 **Step 12-14 的格式** 去问 AI,用 `docs/dev-index.md` 找对应文档。

### Step 16 · 给登录接口加角色信息
⏱️ 2 小时
**目标**:登录返回的 user 里包含 roles 和 permissions 数组。

**提示词核心**:
```
登录接口返回 user 时带上 roles[] 和 permissions[]。
permissions 是所有角色权限的并集(BR-106)。
前端 Pinia store 保存这些,方便权限判断。
```

**验收**:Postman 登录,看到 user 里有 roles 和 permissions。

### Step 17 · 权限守卫(后端)
⏱️ 3 小时
**目标**:`@RequirePermissions('lead:read')` 装饰器能保护接口。

**提示词核心**:
```
创建 RequirePermissions 装饰器 + PermissionsGuard。
没对应权限返回 403。
给 /health/me 接口加 @RequirePermissions('user:read') 测试。
```

**验收**:SUPER_ADMIN 能访问,无权限用户 403。

### Step 18 · 前端菜单 + 按钮权限
⏱️ 3 小时
**目标**:没权限的菜单不显示,没权限的按钮不渲染。

**提示词核心**:
```
在 Pinia auth store 加 hasPermission(code) 方法。
写一个 v-permission 指令,用法 v-permission="'lead:write'"。
前端布局左侧菜单,按权限过滤项。
```

**验收**:用 SALES 登录,看不到"系统设置"菜单。

### Step 19 · 员工管理页面(M1.2 CRUD)
⏱️ 6 小时
**目标**:有员工列表、创建、编辑、禁用功能。

**提示词核心**:
```
参考 docs/requirements.md M1.2。
后端:UserController 实现 list/create/update/disable。
前端:UserList.vue 展示表格 + 操作按钮。
注意 BR-108 离职处理。
每个接口加对应的 @RequirePermissions。
```

**验收**:能创建新员工、分配角色、禁用账号。

### Step 20 · 组织架构树(M1.1)
⏱️ 5 小时
**目标**:能创建层级组织,员工能分配到某个组织。

**提示词核心**:
```
参考 docs/requirements.md M1.1。
OrgUnit 树状结构,最多 6 级。
前端用 el-tree 展示。
员工编辑时能选部门(级联选择器)。
```

**验收**:能创建"集团 > 分公司 > 部门 > 小组"4 层,员工能属于某个组织。

### 🎉 Phase B 完成标志
- [ ] 你能登录进系统
- [ ] 你能看到自己的角色和权限
- [ ] 你能创建员工、分配角色
- [ ] 你能管理组织架构
- [ ] 不同角色登录看到不同菜单

**恭喜!你已经完成了最难的 Phase B(账号权限是地基)。**

---

# 🏠 Phase C · 工作台(M2)· Step 21-25

### Step 21 · 首页布局(左侧菜单 + 顶部导航)
⏱️ 3 小时
**提示词核心**:
```
参考 docs/requirements.md M2。
el-container 布局:
- Aside 左侧菜单(按权限过滤)
- Header 顶部(用户头像 + 退出)
- Main 内容区
菜单数据写死一个 config 文件(后续会做动态)。
```

### Step 22 · 工作台首页数据卡片
⏱️ 3 小时
**提示词核心**:
```
首页显示 4 个统计卡片:
- 我的线索数
- 待办数
- 本月签约
- 本月目标
接口暂时返回 mock 数据,后端做个 /dashboard/me 接口返回写死的数字。
```

### Step 23 · 待办中心
⏱️ 4 小时
**提示词核心**:
```
参考 docs/requirements.md M2 + user-journeys.md 旅程 4。
后端加 Todo 表(title, type, status, relatedEntity, assigneeUserId, dueAt)
前端做待办列表页,按"我的/我发起/抄送"三 Tab。
```

### Step 24-25 · 快捷操作 + 公告
⏱️ 共 4 小时
**提示词核心**:
```
- 快捷操作区:"新建线索""新建合同"等按钮
- 公告区:置顶 3 条系统公告(后端 Announcement 表)
```

---

# 📞 Phase D · CRM(M3)· Step 26-35

### Step 26 · Lead 数据模型
⏱️ 2 小时
**文档**:`docs/requirements.md` M3.1 + `business-rules.md` BR-201 到 BR-209

**提示词核心**:
```
创建 Lead 表,字段:
- id, tenantId(BR-1203)
- name, phone(BR-201 唯一,带 unique 索引)
- city, intendedBrand, budget
- source(LeadSource 枚举)
- status(LeadStatus 枚举,BR-202)
- assigneeUserId(负责销售,null=公海)
- assignedAt, lastFollowUpAt
- referrerId(BR-209 转介绍)
- remark
- createdAt, updatedAt, deletedAt

加索引:phone, assigneeUserId, status
```

### Step 27 · 线索 CRUD 接口
⏱️ 5 小时
**提示词核心**:
```
参考 M3.1。
实现:
- GET /leads (分页 + 筛选)
- GET /leads/:id
- POST /leads (BR-201 去重)
- PATCH /leads/:id
- DELETE /leads/:id (软删除)

数据权限:SALES 只能查自己持有 + 公海(BR-106/107)
```

### Step 28 · 线索状态流转
⏱️ 3 小时
**文档**:BR-202

**提示词核心**:
```
实现 PATCH /leads/:id/status
按 BR-202 状态机校验流转合法性。
不允许的流转抛 BadRequestException。
```

### Step 29 · 线索分配
⏱️ 4 小时
**文档**:BR-203, BR-204, BR-206

**提示词核心**:
```
POST /leads/:id/assign
手动分配:运营/主管指定负责人。
BR-206 抢单限流(每销售每日最多抢 20 条)。
```

### Step 30 · 跟进记录
⏱️ 4 小时
**文档**:M3.4, BR-207, BR-208

**提示词核心**:
```
FollowUp 表:
- leadId, content, type, createdBy, createdAt
- 1 小时内可编辑(BR-207)
- 永不删除

POST /leads/:id/followups
GET /leads/:id/followups (时间线)
```

### Step 31 · 线索列表前端页
⏱️ 6 小时
**提示词核心**:
```
views/Leads/List.vue:
- 顶部筛选栏(状态、来源、销售、时间)
- 表格(Element Plus el-table)
- 分页
- 批量操作按钮(分配、转公海)
权限控制(lead:read/write/assign)。
```

### Step 32 · 线索详情前端页
⏱️ 5 小时
**提示词核心**:
```
views/Leads/Detail.vue:
- 左侧:基本信息 + 编辑
- 右侧:跟进记录时间线 + 快速新增
- 顶部:状态流转按钮(下拉菜单)
```

### Step 33 · 定时任务:超期回公海(BR-204)
⏱️ 4 小时
**提示词核心**:
```
装 @nestjs/schedule。
每天凌晨 2 点,扫描:
- assigneeUserId != null
- lastFollowUpAt < 15 天前 或 assignedAt < 15 天前
清除 assigneeUserId(回公海),记录审计日志。
```

### Step 34 · 客户管理(M3.2)
⏱️ 4 小时
**提示词核心**:
```
Lead 状态变 CONVERTED 时(BR-208),自动创建 Customer 记录。
CustomerController 提供 list/detail/update。
```

### Step 35 · 小程序留资接口(M3.1 来源)
⏱️ 3 小时
**提示词核心**:
```
提供 POST /mini/leads 接口(无需登录)。
应用 BR-201 去重 + BR-901 频率限制。
source 强制 MINI_PROGRAM。
```

### 🎉 Phase D 完成标志
你能在后台走通完整的"创建线索 → 分配 → 跟进 → 转客户"流程。

---

# 🏢 Phase E · 招商项目(M4)+ 加盟商(M5)· Step 36-45

### Step 36 · Brand + RecruitmentProject 模型
⏱️ 3 小时
### Step 37 · 招商项目 CRUD
⏱️ 5 小时
### Step 38 · 加盟政策 Policy 子模型
⏱️ 3 小时
### Step 39 · 资料包管理(文件上传)
⏱️ 4 小时
文档:`docs/requirements.md` M4.4,`business-rules.md` BR-304, BR-1207
### Step 40 · 投资计算器
⏱️ 3 小时
### Step 41 · 招商项目列表前端
⏱️ 4 小时
### Step 42 · Merchant 模型 + CRUD(M5.1)
⏱️ 4 小时
### Step 43 · 加盟商资质审核(M5.1)
⏱️ 4 小时
### Step 44 · 加盟商等级(M5.3)
⏱️ 3 小时
### Step 45 · 加盟商登录视图(M5.2)
⏱️ 5 小时
**重点**:加盟商登录后数据隔离(BR-404)

---

# 🏪 Phase F · 门店(M6)· Step 46-55

### Step 46 · Store 模型(M6.1 含经纬度 BR-504)
⏱️ 2 小时
### Step 47 · 门店 CRUD
⏱️ 4 小时
### Step 48 · 门店生命周期(BR-501,M6.2)
⏱️ 5 小时
**重点**:状态机校验 + 审批流集成(BR-502)
### Step 49 · 门店地图(M6.4)
⏱️ 5 小时
**提示**:用高德地图或百度地图 JS SDK
### Step 50 · StoreDailyData 模型(M6.5)
⏱️ 2 小时
**规则**:BR-505 唯一性 + BR-506 多源优先级
### Step 51 · 手工录入页面
⏱️ 4 小时
### Step 52 · 异常检测(BR-507)
⏱️ 5 小时
### Step 53 · 数据查询看板(某店历史)
⏱️ 4 小时
### Step 54 · 邮件附件解析录入(自动化)
⏱️ 6 小时
**提示**:用 IMAP 扫邮箱,解析 Excel 附件
### Step 55 · 门店任务(M6.3 占位)
⏱️ 3 小时
**提示**:MVP 先做最简单的任务列表,达人探店二期做

---

# 📝 Phase G · 合同审批(M7)· Step 56-62

### Step 56 · Contract 模型
⏱️ 2 小时
### Step 57 · 合同 CRUD + 状态机(BR-601)
⏱️ 5 小时
### Step 58 · 审批流引擎(简化版)
⏱️ 7 小时
**文档**:M7.2, BR-604, BR-605
**提示**:MVP 不做可视化配置,用代码定义流程
### Step 59 · 审批前端(我审批/我发起/抄送)
⏱️ 5 小时
### Step 60 · 合同模板(变量占位)
⏱️ 5 小时
### Step 61 · 合同到期预警(BR-606)
⏱️ 3 小时
### Step 62 · 财务回款登记(M8.1 最小版)
⏱️ 4 小时
**规则**:BR-701, BR-702

---

# 🤖 Phase H · AI 智能助手(M14)· Step 63-73

> ⚠️ 这是最难的部分,每步都要仔细读 `docs/ai-security.md`

### Step 63 · AIProviderConfig 模型
⏱️ 3 小时
**文档**:M14.1,BR-1106
**重点**:API Key 用 AES-256-GCM 加密存储

### Step 64 · Kimi API Client 封装
⏱️ 4 小时
**提示词核心**:
```
封装一个 KimiProvider 类,实现 LLMProvider 接口(为 v2 多 Provider 预留)。
支持流式 + 工具调用。
base_url: https://api.moonshot.cn/v1 (OpenAI 兼容)。
从环境变量或 AIProviderConfig 读 API Key。
```

### Step 65 · AI 配置页(管理员端 + 用户端)
⏱️ 4 小时
**文档**:M14.1 混合 Key 模式
**重点**:Key 不能返回给前端(只显示 "已配置")

### Step 66 · AIConversation + AIMessage 模型
⏱️ 2 小时

### Step 67 · 基础聊天接口(无工具调用)
⏱️ 5 小时
**目标**:能和 Kimi 聊天,流式返回

### Step 68 · 前端聊天界面(抽屉)
⏱️ 6 小时
**重点**:
- SSE 流式接收
- Markdown 渲染
- 会话列表

### Step 69 · Tool Registry 框架
⏱️ 5 小时
**文档**:`docs/ai-tools-registry.md` §1
**重点**:三层权限校验架构(ai-security.md §1)

### Step 70 · 实现前 5 个查询工具
⏱️ 8 小时
**工具**:T01, T02, T07, T11, T15 (dev-index.md 里标了优先级)

### Step 71 · Action Proposal 确认流
⏱️ 6 小时
**文档**:M14.4, BR-1103, ai-security.md §4

### Step 72 · 实现前 5 个写入工具
⏱️ 8 小时
**工具**:T16, T17, T18, T21, T22

### Step 73 · 黑名单 + 配额熔断 + 审计
⏱️ 5 小时
**文档**:ai-security.md §2, §10, §9
**规则**:BR-1102, BR-1105, BR-1107

### 🎉 Phase H 完成标志
你能:
- 用 AI 问"我这周跟进了几个客户"→ AI 真的查数据库回答
- 对 AI 说"帮我分配这 5 条线索给李四"→ 弹窗确认 → 执行

---

# 🖼️ Phase I · AI OCR(M15)· Step 74-80

> ⚠️ 全程参考 `docs/ai-ocr-module.md`
> ⚠️ 权限守卫:仅 SUPER_ADMIN!

### Step 74 · OCRJob + OCRImage 模型
⏱️ 3 小时
**文档**:ai-ocr-module.md §11

### Step 75 · SuperAdminOnlyGuard(硬编码守卫)
⏱️ 2 小时
**文档**:ai-ocr-module.md §10.1 + BR-1301
**重点**:Controller + Service 双层校验

### Step 76 · 图片上传 + Hash 去重
⏱️ 5 小时
**规则**:BR-1303 SHA-256 全局唯一

### Step 77 · Kimi 多模态调用(识别)
⏱️ 6 小时
**文档**:ai-ocr-module.md §6 Prompt 模板

### Step 78 · 核对页前端
⏱️ 8 小时
**文档**:ai-ocr-module.md §14
**重点**:
- 左图右表单
- 低置信红色高亮
- 修改痕迹追踪(BR-1305)
- 提交前二次确认

### Step 79 · 异常检测 + 审计
⏱️ 4 小时
**规则**:BR-1315, BR-1316, BR-1317,ai-ocr-module.md §9

### Step 80 · AI OCR 集成到 AI 助手
⏱️ 3 小时
**重点**:T31, T32 两个工具(`ai-tools-registry.md`)

---

# 📊 Phase J · 看板 + 其他(Step 81-88)

### Step 81 · 招商漏斗看板(M11.1)
⏱️ 5 小时
### Step 82 · 销售排行榜
⏱️ 3 小时
### Step 83 · 财务看板
⏱️ 4 小时
### Step 84 · CSV 导出(M11.5)
⏱️ 5 小时
**规则**:BR-1002, BR-1003
### Step 85 · 通知中心(M12)
⏱️ 5 小时
### Step 86 · 短信通道(M12.2,阿里云)
⏱️ 4 小时
### Step 87 · 审计日志查询页(M13.3)
⏱️ 4 小时
### Step 88 · 系统设置页(M13.1)
⏱️ 3 小时

---

# 🚢 Phase K · 部署上线(Step 89-92)

### Step 89 · 生产环境切换 PostgreSQL
⏱️ 4 小时

### Step 90 · Docker Compose 配置
⏱️ 4 小时
**组件**:backend + admin + postgres + redis + minio

### Step 91 · 买服务器 + 域名 + 部署
⏱️ 1-2 天
**建议**:阿里云轻量服务器(2核4G,~¥70/月)

### Step 92 · HTTPS + 监控 + 备份
⏱️ 1 天

### 🎉 正式上线!

---

# 📚 开发原则速查(贴在显示器上)

## 🔄 每一步的标准流程

```
1. 打开 dev-workflow.md,找到当前步骤
   ↓
2. 读对应的 docs/ 文档(用 dev-index.md 找)
   ↓
3. 复制"给 AI 的提示词",按需微调
   ↓
4. Cursor 里 Ctrl+L,粘贴提示词
   ↓
5. AI 先说"要改哪些文件",确认后再给代码
   ↓
6. 一个文件一个文件实施
   ↓
7. 测试(curl/Postman/浏览器)
   ↓
8. 对照"验收清单"打勾
   ↓
9. 全部打勾:
   git add .
   git commit -m "feat(x): Step N - xxx"
   git push
   ↓
10. 回到步骤 1,做下一步
```

## ⚠️ 常见坑速查

| 症状 | 可能原因 | 解决 |
|------|---------|------|
| 启动报错 "Cannot find module" | 忘了装依赖 | `pnpm install` |
| CORS 错误 | 前端后端端口不一致 | 后端 main.ts 加 CORS |
| 401 错误 | Token 过期 | 重新登录 |
| 数据库文件不存在 | 忘了 migrate | `prisma migrate dev` |
| 找不到 .env | 隐藏文件 | 确认是否被 .gitignore 正确忽略 |
| pnpm 命令不存在 | 没全局装 | `npm install -g pnpm` |
| 端口被占用 | 之前的进程没关 | 杀掉或换端口 |

## 🆘 卡住了找谁

1. **第 1 分钟**:再读一遍 AI 给你的完整错误信息
2. **第 5 分钟**:把错误 + 相关代码一起丢给 Cursor,用 `troubleshooting.md`(你可以创建一个)模板
3. **第 10 分钟**:Google 错误的核心关键词
4. **第 20 分钟**:问 ChatGPT 或 Claude 网页版(有时比 Cursor 强)
5. **第 30 分钟**:**停下来**。休息 30 分钟或找我

## 💡 提速技巧

### 让 AI 少出错的 3 句话
1. "先告诉我要改哪些文件,不要立即写代码"
2. "我是小白,用中文注释,代码控制在 50 行内"
3. "给我完代码后,告诉我怎么测试"

### 让 Cursor 更懂你的 2 个技巧
1. **`@docs/xxx.md`** - 引用指定文件
2. **选中代码再聊天** - Cursor 自动带上你选的代码

### 让进度可视化
- 每天开始前,在这份文档标今天的目标 Step
- 每天结束前,在 Git 里写清楚今天干了什么
- 每周日,回看一周进度,调整下周计划

---

# 🏁 最后的话

这份文档你不会一天看完,也不用一天看完。

**它是你接下来 6 个月的地图。**

每天只看 1-2 个 Step,一个一个打勾。

如果你今天只打了 1 个勾,你就比昨天厉害了。
如果你一周打了 5 个勾,你就比 90% 的人坚持下来了。

**慢就是快。**

---

## 📮 进度汇报模板(每周用)

每周日花 10 分钟填这个:

```
## 第 X 周进度汇报(日期)

### 本周完成
- [x] Step A
- [x] Step B

### 本周卡住
- Step C 在 xxx 卡了 2 天,最后通过 xxx 解决
- Step D 在 yyy 放弃,先跳过

### 下周计划
- [ ] Step E
- [ ] Step F

### 感想
(写点啥都行,这是你的日记)

### 花费
AI 订阅:¥XXX
服务器:¥0(未买)
合计:¥XXX
```

---

**开始吧!第一步:打开 Step 1,装环境。**

**你今天的任务:装 Cursor + Node.js + pnpm。**

**不多,这一件事做好了就是胜利。**

🚀 Good luck!
