# Sus-CV — 1:1 精排的中文技术简历 LaTeX 模板

**主体是这套简历模板**：无边框色块小节、真公司 logo、985/211 校徽、超链接、内联代码框，一份好简历该有的排版细节都 1:1 复刻好了，改几个占位符就能用。

- **`resume/`** — 现成的简历模板（`.tex` + 渲染好的 `.pdf`），公司 logo 库 + 985/211 校徽库都在里面。**这是主角。**
- **`resume-forge/`**（锦上添花）— 一个 Claude Code **Skill**：把你手上**任意来源、任意模板**的简历，迁移进这套模板、调好排版、按范式把内容写清楚（附润色与脱敏）。没有它也能直接用模板；有它就多一个自动化助手。

## 效果预览

<p align="center">
  <img src="docs/preview-1.png" width="48%" alt="简历第1页"/>
  <img src="docs/preview-2.png" width="48%" alt="简历第2页"/>
</p>

> 上图为 `resume/resume_template.pdf` 的渲染效果(虚构信息版)。

## 快速上手（用简历模板）
```bash
cd resume/
# 改 resume_template.tex 顶部 8 个 \newcommand 填你的信息(姓名/电话/邮箱/微信/GitHub/学校/域名)
tectonic resume_template.tex          # 或 xelatex
```
- 加公司 logo：正文写 `\logo{bytedance}`；素材库在 `assets/logos/`（23 个，见 `resume-forge/references/logo_index.pdf`）。
- 缺的公司：`python3 resume-forge/scripts/fetch_logos.py 公司slug`。
- 学校前放**校徽**：把抬头小三角换成 `\emblem{sysu}`（矢量优先）。

## 985/211 校徽素材库

抬头学校名前的小三角可换成真校徽。素材库 `assets/emblems/` 已内置 **106 所高校校徽**（全部 39 所 985 + 绝大多数 211），顶尖高校为**矢量 PDF**、其余为 PNG。

```latex
\emblem{sysu}~\CSchool     % 用法:slug 不带扩展名,矢量 pdf 优先、其次 png
```

- **slug 速查**：`resume-forge/references/emblem_index.pdf`（按 985 / 211 分区的可视总览）或 `assets/emblems/emblem_index.tsv`（`层次 / 中文名 / 英文名 / slug / 来源`）。常用：`thu`=清华、`pku`=北大、`sysu`=中山、`sjtu`=上交、`zju`=浙大、`fdu`=复旦、`ustc`=中科大。

<p align="center"><img src="docs/emblems-preview.png" width="80%" alt="985/211 校徽素材库预览"/></p>

## resume-forge Skill（可选 · 锦上添花）
> 只想要简历模板的话，这一节可以跳过——直接改 `resume/resume_template.tex` 就行。

把 `resume-forge/` 放进 `~/.claude/skills/`（或作为 plugin）。之后对 Claude 说：
- "把我这份简历（任意格式/模板）适配进这个模板 / 1:1 复刻 / 脱敏" → 走**内容迁移 + 排版调优**流程。
- "润色我的简历" → 按 `resume-forge/PRINCIPLES.md`（强简历十条原则）改，**只改措辞不动事实**。

## 内容
- `resume-forge/SKILL.md` — 三种用法工作流 + 1:1 保真清单 + 环境坑。
- `resume-forge/PRINCIPLES.md` — 从一份顶尖简历蒸馏的写法原则（量化/owner化/机制化/命名概念/去水分…）。
- `resume-forge/template/` — 模板 + logo 素材库 + 985/211 校徽库（`assets/emblems/`）。
- `resume-forge/references/` — `logo_index.pdf`（公司 logo 总览）+ `emblem_index.pdf`（校徽总览）。
- `resume-forge/scripts/` — 抽取 / 取 logo / 编译。

## 依赖
XeLaTeX（推荐 tectonic，自带自动装包）+ 字体 `Noto Serif CJK SC` / `Liberation Serif` / `DejaVu Sans Mono`。
取 logo 需 `cairosvg`（`python -m venv` 装，系统需 `libcairo`）。

## 相关项目（友情链接）

- [**Hisn00w/ASu-skills**](https://github.com/Hisn00w/ASu-skills) — 同样受阿酥求职简历经验启发做的简历包装工具（Codex / Claude Code 技能 + 大厂极简 HTML 模板），思路相近，可搭配参考。

## 许可 / 素材来源
- 公司 logo 来自 [Simple Icons](https://simpleicons.org)；校徽来源见[致谢](#致谢)。
- **校徽与公司 logo 均为各机构的注册商标，仅用于在简历上标注申请人真实的教育 / 工作经历（nominative use）**；本仓库不主张任何商标权利，商业或再分发用途请自行确认授权。

## 致谢

感谢以下小红书博主的公开分享与启发：

- [**阿酥在coding**](https://xhslink.cn/m/2LHuLJZ30b2)：关于 Coding 面试经验的分享。

**985/211 校徽素材库**站在这些开源工作之上，一并致谢：

- [**pluwen**](https://www.figma.com/@pluwen)：顶尖高校矢量校徽的原始设计者（Figma「中国大学矢量校徽合集」）；
- [**soulteary/china-university-icon**](https://github.com/soulteary/china-university-icon)（CC0）：将上述矢量整理为规整的 SVG 合集，本库矢量校徽取自此；
- [**xioajiumi/Chinese_Universities**](https://github.com/xioajiumi/Chinese_Universities)：985/211 名录与校徽索引数据；
- [**Wikipedia / Wikimedia**](https://www.wikipedia.org) 与 [**软科 ShanghaiRanking**](https://www.shanghairanking.cn)：其余高校校徽来源。

> 各校校徽版权归各高校所有，此处仅用于在简历上标注真实教育经历（nominative use）。
