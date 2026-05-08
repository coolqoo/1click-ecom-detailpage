<div align="center">

# 🛍️ 1Click Ecom PDP Skill

**面向 AI Agent 的高级跨境电商 PDP 转化策略引擎**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tested On](https://img.shields.io/badge/Tested_on-OpenClaw_|_Hermes_|_Codex_|_Claude_Code-2ea44f?style=for-the-badge&logo=openai&logoColor=white)](#)
[![AI Agent Ready](https://img.shields.io/badge/AI_Agent-Ready-8A2BE2?style=for-the-badge&logo=probot&logoColor=white)](#)

*深度洞察转化诱因 ｜ 端到端生成高转化图包与文案 ｜ 无缝对接主流 API*

</div>

---

> **Ecom PDP Skill** 的核心理念是：**先判断商品为什么能卖**。
> 
> 它能够智能输出高转化的**英文基准文案**、**主图 / 详情页视觉结构**、**图内短文案**以及**可执行的 AI 生图 Prompt**。在配置 OpenAI 兼容的图片 API 后，更可直接为您生成完整的电商 PDP 图包，实现真正的端到端交付。

## ✨ 核心特性

- **🎯 深度转化诊断**：智能分析产品的核心购买驱动力（视觉驱动、痛点驱动或情绪价值驱动）。
- **🌍 极致跨境本地化**：生成原汁原味的 English (US) 营销文案，完美适配 Amazon, Shopify, TikTok Shop 等多渠道。
- **📸 端到端出图能力**：根据策略 Prompt 自动生成 5 张主图 + 7~9 张详情页连贯视觉图。
- **🤖 广泛的框架兼容**：专为 Agent 打造，已在 OpenClaw, Hermes, Codex, Claude Code 等主流智能体框架上进行深度验证与测试。

---

## 🚀 快速开始

将以下指令发送给你的 AI Agent：

```text
请安装这个 Skill：`https://github.com/coolqoo/1click-ecom-detailpage`
```

安装完成后，配置生图模型 API（参考下方 [🔑 API 配置](#-api-配置)），即可通过自然语言直接驱动。

*(注意：若未配置 API，系统将仅输出可执行的生图 Prompt。)*

**直接发给 Agent 的示例指令：**
```text
用 ecom-pdp 给这款产品做 Amazon US PDP 图包：
输出 5 张主图 + 8 张详情页图。
```

---

## 💻 部署与配置

<details>
<summary><b>点击展开手动安装指南</b></summary>

**环境要求：**
- AI Agent 具有本地 Skill 目录的读取权限。
- Python 3.10+（生图脚本纯净且仅依赖标准库）。

如果您的 Agent 运行在 `~/.codex/skills` 目录下，可从本仓库根目录手动安装：

```bash
mkdir -p ~/.codex/skills/ecom-pdp
rsync -a --exclude .git --exclude .env --exclude "generated-images/" ./ ~/.codex/skills/ecom-pdp/
```

**验证安装：**
```bash
python3 ~/.codex/skills/ecom-pdp/scripts/generate_image.py --help
```

</details>

### 🔑 API 配置 (解锁直接生图)

为了开启图包的**一键生成**，请在项目根目录复制环境变量文件：

```bash
cp .env.example .env
```

并在 `.env` 中填入兼容的服务凭证：

```dotenv
IMG_BASE_URL=https://api.openai.com/v1
IMG_MODEL=gpt-image-1.5
IMG_API_KEY=your-api-key
```

> **安全提示**：请妥善保管您的密钥，切勿将 `.env` 提交至代码库中。脚本同时兼容 `OPENAI_API_KEY` 等常见环境变量。

---

## 💡 实战场景与用法

### 🤖 零代码自然语言调用
在 AI Agent 中以对话形式发起任务：

```text
用 ecom-pdp 给这款便携榨汁杯做 Amazon US PDP 图包：
目标人群是健身和通勤人群，卖点是 20 秒打碎、USB-C 充电、便携防漏。
输出 5 张主图 + 8 张详情页图，先给 Prompt；如果本地 API 配置齐全就直接出图。
```

### 🛠️ 进阶命令行调用

<details>
<summary><b>点击查看更多高级用法</b></summary>

**仅输出 Prompt 策略文件：**
```bash
python3 scripts/generate_image.py \
  --mode prompt \
  --prompt "premium Amazon main image for a portable blender, clean white background, large product, concise benefit label" \
  --job-dir generated-images/portable-blender-pack-20260509-120000 \
  --asset-type main \
  --size 1024x1024
```

**从预设文件自动生成：**
```bash
python3 scripts/generate_image.py \
  --prompt-file prompts/main-01.txt \
  --job-dir generated-images/portable-blender-pack-20260509-120000 \
  --asset-type main
```

**基于产品参考图生成一致性资产（Product Angle Sheet）：**
```bash
python3 scripts/generate_image.py \
  --prompt-file prompts/angle-sheet.txt \
  --image product.png \
  --job-dir generated-images/portable-blender-pack-20260509-120000 \
  --asset-type angle-sheet
```

</details>

---

## ⚙️ 核心引擎与工作流

### 🔄 智能执行链路
1. **多级上下文补齐**：自动按权重补全信息缺失（用户输入 > 附件上下文 > 自动联网研究 > 逻辑推理 > 默认假设）。
2. **转化驱动洞察**：智能剖析当前商品属于 Visual-Driven, Pain-Driven 还是 Emotion-Value-Driven。
3. **策略卡输出**：生成 `Buyer Reason Card`（购买理由卡），定调英文基准文案与核心 CTA。
4. **视觉风格锁定**：建立全局 `Campaign Style Lock`，确保几十张套图风格严丝合缝。
5. **按需直接交付**：用户明确指令且 API 就绪时，直接调用内部脚本渲染出完整资产图包。

### 🛡️ 智能合规偏好 (Compliance Engine)
系统默认**关闭**合规审查以保证创意自由度。若您要求“开启合规 / 风险审查”：
- 将严格过滤功效承诺、医疗暗示、绝对化用语及不当比较。
- 强制要求数据、认证、销量及用户真实评价来源合法且可验证。
- 没有真实素材时，自动以功能解析 / FAQ / 场景代替评价区块。

### 🧠 主动提问与容错机制
当核心信息（如产品本体、核心受众、目标平台等）缺失时，Agent 会发起不超过 3-5 个核心提问。若得到“你看着办”或“快速出图”的授权，系统将自动启用**假设与推断**能力继续流程，并在输出末尾高亮提示 `Assumptions / Defaults Used`，充分保证流程通畅。

---

## 📦 输出交付规范

系统会为每一次产出规划清晰的任务流目录结构，方便后续人工审核及 A/B 测试：

```text
generated-images/<product-slug>-pack-<yyyymmdd-hhmmss>/
  ├── angle-sheet/  # 🛠️ 临时产品角度基准图（用于一致性控制）
  ├── main/         # 🖼️ 主图组（1024x1024）
  ├── detail/       # 📜 详情页长图组（1024x1536）
  ├── prompts/      # 📝 每张资产图的独立执行 Prompt
  ├── extras/       # 🎨 接口额外生成的变体或备选图
  └── custom/       # 🧪 临时调试与自定义生成图
```

### 📏 图片包黄金法则
只要提到“详情页 / PDP / 主图堆栈 / 整套商品图”，Skill 默认遵循以下交付模型：
- **5 张主图**：首图卖点 → 机制解析 → 利益证明 → 场景对比 → 优惠保障。
- **7-9 张详情图**：首屏承接 → 痛点放大 → 机制解释 → 步骤场景 → 竞品对比 → 好评背书 → 风险逆转 (CTA)。
- 每张图**独立 Prompt** 生成，拒绝劣质拼图，强制应用全局 Style Lock。

---

## 🎯 三大转化驱动模型 (Conversion Drivers)

| 驱动模式 | 适用场景 | 策略重心 |
| --- | --- | --- |
| 👁️ **Visual-Driven** | 外观、质感、礼品感强、前后对比明显的产品 | 极致的视觉主张、质感放大、场景匹配、扫读利益点 |
| ⚡ **Pain-Driven** | 解决反复烦恼、降低风险、提升效率的产品 | 痛点挖掘 → 机制解析 → 利益证明 → 信任背书 → CTA |
| 💖 **Emotion-Value** | 表达自我身份、归属感、社交地位或冲动消费品 | 情绪钩子、身份叙事、社交信号放大、低摩擦引导 |

---

## 📋 真实输入输出参考

### 典型输入结构 (Input)
```text
Product: Self-heating eye mask
Category: Sleep & wellness
Audience: stressed office workers in the US market
Differentiators: 40-minute heat duration, unscented option...
Current weak points: decent CTR, low add-to-cart, weak trust perception
Goal: improve CVR and trust
Need: 5 hero images + 8 PDP detail images
```

### 专业交付形态 (Output Shape)
<details>
<summary><b>点击查看策略输出缩略版</b></summary>

```text
1. Conversion Driver Diagnosis
   Primary: Pain-Driven
   Why: recurring discomfort + clear relief mechanism + trust barrier.

2. Buyer Reason Card
   Target Buyer: stressed office workers.
   Purchase Trigger: eye fatigue and sleep friction after long screen time.
   ...

3. English Baseline
   Hero headline: Melt Away Screen-Day Tension
   ...

4. Hero Image Sequence
   Frame 1: problem snapshot
   ...

5. Image Prompts
   Prompt 01: Campaign Style Lock... [independent executable prompt]
```
</details>

---

## ⚠️ 局限性说明
- **生图能力边界**：当前支持文本生图与单张产品参考图生图，暂不支持基于 mask 的精准局部重绘。
- **外部接口依赖**：高度依赖 OpenAI 兼容的 Images API。图像质量、连贯性与耗时取决于您配置的底层模型（如 DALL·E 3 / Flux 等）及服务商。
- **转化归因**：本 Skill 输出为高转化潜力的策略与创意基线，真实商业回报（CTR/CVR/AOV）仍受限于您的产品力、市场定价与流量采买策略。

---
<div align="center">
  <p><i>Empowering E-commerce AI Agents with High-Converting Visuals</i></p>
</div>
