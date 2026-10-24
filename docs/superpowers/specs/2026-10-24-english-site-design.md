# 英文版网站设计（xy-cloud.org/en/）

日期：2026-10-24
状态：已确认设计方向（结构方案 A），待用户审阅本文档

## 目的

让海外读者能直接了解株式会社XY并发起合作。读者有两类：

1. **海外教育机构**（大学、语言学校、培训机构）：潜在的 Compass / chinichi-OS 客户，或 AI 导入咨询客户
2. **投资方・合作伙伴**（含 Apple、银行等平台的审核）：要确认公司真实存在、业务可信

成功标准：海外读者不用看日文就能弄清 XY 做什么、为什么可信、怎么联系；英文页能被 Google 单独收录。

## 不做的事

- 不加中文版或其他语言（以后需要再按同样结构加 `/zh/`）
- 不引入构建工具、模板引擎或 JS 语言切换；保持静态 HTML
- 不改日文页的内容（只加语言切换和 hreflang）
- 不改设计风格；英文页沿用 `css/style.css`，只补少量英文排版需要的样式

## 结构

`/en/` 目录下放与日文版一一对应的页面，文件名相同：

| 日文版 | 英文版 | 处理方式 |
|---|---|---|
| `index.html` | `en/index.html` | 改写（见「内容」） |
| `company.html` | `en/company.html` | 改写为 Corporate Profile |
| `compass.html` | `en/compass.html` | 翻译 |
| `chinichi.html` | `en/chinichi.html` | 翻译 |
| `cases.html` | `en/cases.html` | 改写（集团内学校如实说明） |
| `fde.html` | `en/fde.html` | 翻译 |
| `faq.html` | `en/faq.html` | 改写为海外客户会问的问题 |
| `contact.html` | `en/contact.html` | 翻译＋加栏位 |
| `privacy.html` | `en/privacy.html` | 翻译（标注以日文版为准） |
| `news.html` | `en/news.html` | 翻译 |
| `recruit.html` | `en/recruit.html` | 翻译＋注明工作地点东京 |
| `column.html` | `en/column.html` | 翻译 |
| `column-education-dx.html` | `en/column-education-dx.html` | 翻译＋背景说明 |
| `column-zokujinka.html` | `en/column-zokujinka.html` | 翻译＋背景说明 |
| `404.html` | （共用） | 改成日英双语一页，GitHub Pages 只认根目录的 404 |

- 英文页里的资源路径用 `../css/style.css`、`../assets/...`，所有素材共用
- 英文页之间的链接用相对路径（`company.html` 指向 `en/company.html`）

### 语言切换

- 每页导航（PC 和手机菜单）加「日本語 / EN」切换，链接到**对应语言的同一页**
- 页脚也放一处同样的切换
- 当前语言用粗体或下划线标出，另一个是链接

### SEO

- 每对中日页面都加：
  `<link rel="alternate" hreflang="ja" href="https://xy-cloud.org/<page>">`
  `<link rel="alternate" hreflang="en" href="https://xy-cloud.org/en/<page>">`
  `<link rel="alternate" hreflang="x-default" href="https://xy-cloud.org/<page>">`
- 英文页：`<html lang="en">`、`og:locale=en_US`、英文 title／description／og 文案；canonical 指向自己的英文网址
- 结构化数据（JSON-LD）英文页用英文的 `name: "XY, K.K."`、`alternateName: "株式会社XY"`
- `sitemap.xml` 补上 14 个英文网址
- og 图片暂时共用 `assets/og.png`

## 内容

整体语气：给海外专业读者看的公司网站，平实、具体，不用夸张的营销用语。不是逐字直译，按海外读者能理解的方式改写。

### 首页
- 定位句方向："AI-native school operations, built by educators in Tokyo"，突出"自己经营学校、自己开发系统"
- 保留：痛点、6 个服务领域、AI 能力、强项、产品（Compass／chinichi-OS）、代表人介绍、实绩数字
- **删除补助金区块**（IT 导入补助金只在日本有效）
- 「OPC（One Person Company）」改写为"决策者和开发者直接对接、AI 辅助开发"，不强调"只有一个人"
- 实绩数字保留（约 440 名出願、6～8 人降到 1～2 人）

### Corporate Profile（company）
| 项目 | 内容 |
|---|---|
| Company name | XY, K.K.（株式会社XY） |
| Address | 3F Sankei Bldg., 1-28-10 Takadanobaba, Shinjuku-ku, Tokyo 169-0075, Japan |
| Representative | Iken Setsu（薛 偉軒）, Representative Director & CEO |
| Established | February 7, 2024 |
| Capital | JPY 1,000,000 |
| Fiscal year | October 1 – September 30 |
| Corporate Number | 9011101106148 |
| D-U-N-S Number | 964338668 |
| Phone | +81-80-4876-7999 |
| Email | setsuiken@xy-cloud.org |
| Business | 用英文概括实际业务（教育机构业务系统和 AI 的开发与导入），定款原文的事业目的附英文意译 |

公告方法（官报）对海外读者没有意义，不列。

### 导入实绩（cases）
如实写成 "schools operated within our education group"：羽場学園、平井学園、SGG 外語学院是集团内的学校。强调这是每天实际在用的系统。

### FAQ
改写为海外客户会问的问题：远程导入与支持、支持哪些语言、数据存放位置、结算币种和方式、是否支持本地部署、合同签订方式等。答案以现有日文 FAQ 和网站已有的事实为依据；没有依据的问题不写（不编造服务条件）。

### Contact
- 表单英文化，仍用现有的 Web3Forms access key 发到 setsuiken@xy-cloud.org
- 新增栏位：Country、Organization type（Educational institution / Investor / Partner / Other）
- 邮件主题加 `[EN]` 前缀，方便区分来源
- 电话写成国际格式

### Privacy
翻译全文，开头注明：日文版为正式文本，内容不一致时以日文版为准。

### Recruit / Column / News
- 招聘：翻译，注明工作地点在东京、需要的日语能力照日文版的条件写
- 专栏：翻译，开头补一句"本文以日本的教育机构为例"
- 新闻：逐条翻译

### 404
日英双语：上半日文、下半英文，各自给"回首页"链接（`/` 和 `/en/`）。

## 日文页的改动

只加两样：语言切换链接、hreflang 标记。内容、样式都不动。

## 检查（上线前）

1. 本地用 `python3 -m http.server` 预览
2. 脚本检查：
   - 所有页面的内部链接和资源路径都能打开（包括 `../` 路径）
   - 英文页里没有残留的日文假名或汉字（公司日文名「株式会社XY」、人名「薛 偉軒」、学校名等允许列表除外）
   - 每对中日页面的 hreflang 互相指向、canonical 正确
   - `sitemap.xml` 是合法的 XML，并包含全部英文网址
3. 截图检查：英文首页、Corporate Profile、Contact 的桌面版和手机版（375px），确认英文长单词不撑破版面
4. 联系表单在英文页能正常提交（Web3Forms 返回成功）——需要用户同意后再实际发一封测试邮件
5. 确认没问题后推送 main，线上再确认一次

## 维护

README 加一条规则：改日文页时，同步修改 `/en/` 下同名页面；新增日文页时，同时新增英文页并更新 hreflang 和 sitemap。

## 未决事项

- 人名的英文写法：按日文版的读音写成 "Iken Setsu"（与 Apple 开发者账号上的「セツ イケン」一致）。如果护照上的拼法不同，以护照为准，在审阅时确认。
