---
name: resume-forge
description: >-
  Adapt ANY existing resume (in any format/template — PDF / docx / text /
  screenshot) INTO this polished LaTeX resume template: migrate the content,
  fix the typesetting to a clean 2-page layout, and rewrite the wording to be
  clear and concise following this template's proven writing method. Also
  supports polishing and desensitizing. Use when the user gives a resume and
  wants it re-typeset into this template / made cleaner / anonymized. Ships the
  ready LaTeX template, a company-logo asset library, and helper scripts.
---

# resume-forge — 把任意简历适配进本模板 + 排版调优 + 按范式写清楚

这个 Skill 做的**不是**"把某份简历抽象成一个空模板"，而是：**把用户手上任意来源、任意模板的简历内容，迁移进本仓库这套精排模板里**，调好排版，并按这套模板的写法把内容写得**清晰明了**。三种用法可单独或组合：

1. **内容适配到本模板**：任意简历（PDF/docx/文本/截图）→ 用本模板重新精排（同一套版式：蓝色小节、无边框色块、真 logo、内联代码框），排到干净的 2 页。
2. **按范式书写 / 润色**：套用 `PRINCIPLES.md` 的强简历写法（量化、owner 化、给机制、命名概念、去水分），把原内容改写得清晰明了——**只改措辞不动事实**。
3. **脱敏**：把姓名/电话/邮箱/微信/GitHub 号/学校/个人域名换成顶部占位符或虚构值。

核心资产：
- `template/resume_template.tex` — 现成的中文 XeLaTeX 简历模板（蓝色小节、无边框色块、真 logo、内联代码框）。
- `template/assets/logos/*.pdf` + `*.svg` — 公司 logo 素材库（抖音/B站/GitHub/字节/阿里/华为…），`\logo{名字}` 调用。
- `template/assets/emblems/` — **985/211 校徽库**（104 所,顶校矢量 pdf、其余 png），`\emblem{sysu}` 调用,替换抬头学校前的小三角；slug 见 `references/emblem_index.pdf` / `assets/emblems/emblem_index.tsv`。
- `references/logo_index.pdf` / `references/emblem_index.pdf` — logo / 校徽总览。
- `PRINCIPLES.md` — 强简历写法十条原则（润色/新写时逐条对照）。
- `scripts/` — 抽取、取 logo、编译脚本。

---

## 何时用哪个模式

- 用户给了一份简历文件并说"做成模板 / LaTeX / 1:1 复刻 / 脱敏" → **模式 1（+3）**。
- 用户说"润色 / 改得更好 / 优化措辞" → **模式 2**（先读 `PRINCIPLES.md`）。
- 用户已有此模板、只想填自己内容 → 改 `resume_template.tex` 顶部 `\newcommand` 占位符即可。

---

## 模式 1：改造迁移成模板（1:1）

**步骤**

1. **读原件**：PDF/图片直接用 Read 工具看版式与内容；docx 用 `scripts/extract_resume.py` 抽文本。逐块记录：抬头、各小节、每个项目的（标题/公司/时间/标签/链接）、层级符号、内联代码项、配色、logo。
2. **脱敏**（模式 3）：把 PII 提到 `.tex` 顶部 `\newcommand`（`\CName \CPhone \CEmail \CWeChat \CGitHub \CSchool \CProdA/B`），正文用宏引用。姓名/学校若要"虚构值"就填一个体面的假名/假校名（如"苏亦宁""江海大学·软件工程专业"），别用丑的尖括号。
3. **套版式**：以 `template/resume_template.tex` 为骨架，把内容填进去。**技术内容与写法一字不改**（那是简历的价值）。命令速查：
   - `\rsection{小节名}` → 蓝色标题 + 分割线
   - `\cbar[可选色]{\logo{公司}}{标题}{右侧时间/标签/链接}` → 项目色块头（`barbg` 灰 / `barpink` 粉）
   - `\ptitle{项目子标题}` → 蓝色项目标题
   - `\code{system\_prompt}` → 内联代码框
   - `\logo{douyin}` `\logo{bilibili}` `\logo{bytedance}` … → 真 logo
4. **取 logo**：缺的公司用 `scripts/fetch_logos.py "抖音=douyin,B站=bilibili,字节=bytedance"`（内部走 Simple Icons + cairosvg 转矢量 PDF），产物落到 `template/assets/logos/`。
5. **编译**：`bash scripts/compile.sh template/resume_template.tex`（用 tectonic，自动装包）。
6. **对着原件抠细节**（见下方保真清单）。用 Read 工具看编译出的 PDF，逐块比对，改到一致为止。

---

## 模式 2：润色

1. 先读 `PRINCIPLES.md`（十条原则）。
2. 逐条经历过一遍：结构是否 背景→目标→职责→指标？有没有量化？是不是 owner 口吻？有没有给出真实机制而非名词堆砌？有没有可命名的抽象？形容词水分删了吗？
3. **红线**：只改表达，不编事实、不夸数字。缺数字就标注让作者补。保留作者有个性的技术命名。
4. 交付方式随场景：直接改 `.tex`，或给"原句→改后句"对照表让作者自己贴。

---

## 保真清单（1:1 复刻时逐项核对，都是踩过的坑）

- **色块无外边框**：`\newtcbox` 必须 `boxrule=0pt, frame hidden, colframe=同底色`，纯色填充微圆角（`arc=2pt`）。
- **蓝色分割线**：线宽约 `1.6pt`；标题↔线约 `1.5pt`、线↔正文约 `4pt`，间距贴原版。
- **超链接**：`hyperref` + `\href`，`urlcolor` 用主蓝，可点。
- **内联代码**：系统里真实存在的实体（`system_prompt`/`memory.json`/CLI）用 `\code{}` 等宽灰框标出。
- **配色**：主蓝 `#1F5FBF`、灰条 `#EEF0F2`、粉条 `#FBECEC`、代码灰 `#F2F2F2`（按原件取色微调）。
- **字体**：`Noto Serif CJK SC`(中文) + `Liberation Serif/Sans`(西文) + `DejaVu Sans Mono`(等宽)。缺字体先 `fc-list :lang=zh` 看有啥。
- **加粗只加结论与数字**，别通篇加粗。

---

## 环境坑（tectonic + CJK）

- **fontawesome5 会让 tectonic 段错误**——别用；图标改用 `pifont`(`\ding{37}`电话/`\ding{41}`信封) + 真 logo `\includegraphics`。
- 字体名要用**系统实际装的**（`TeX Gyre Termes` 常常没有 → 用 `Liberation Serif`）。
- SVG→PDF 用 `cairosvg`（`python3 -m venv` 装，避开 PEP 668）；`libcairo.so.2` 需在系统里。
- Simple Icons CDN：`https://cdn.simpleicons.org/<slug>` 返回带品牌色的 SVG。抖音 slug 常取不到，用 `tiktok`（同音符 logo）代。

---

## 开源发布建议

连同简历模板一起开源时，目录建议：
```
resume/            成品简历(脱敏或虚构信息版) .tex + .pdf
resume-forge/      本 Skill(SKILL.md + PRINCIPLES.md + template/ + scripts/ + references/)
```
README 里写清：改顶部 `\newcommand` 填信息、`\logo{}` 用法、`scripts/fetch_logos.py` 扩 logo、`compile.sh` 编译。
图标来源 Simple Icons（品牌商标，仅用于简历标注真实经历 / nominative use）。
