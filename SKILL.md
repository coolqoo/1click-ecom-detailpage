---
name: crossborder-pdp-conversion-strategy
description: Build high-converting cross-border ecommerce PDP, hero image, product image stack, and AI image prompt strategy by diagnosing the conversion driver first, producing an English (US) baseline, optionally localizing without losing intent, then generating executable image prompts or images through the bundled OpenAI-compatible image script.
---

# Cross-Border PDP Conversion Strategy Skill

当用户需要跨境电商商品主图、PDP 详情页、Amazon / Shopify / TikTok Shop 图片、A+ content、广告图、商品图文案、转化优化、英文基准文案、本地化适配，或直接 AI 生图时，使用这个 Skill。

这个 Skill 的核心不是“先做漂亮图”，而是先判断什么真正驱动购买，再把转化逻辑变成可执行的图文案和生图 Prompt。

## Trigger Signals

- "Amazon listing", "Shopify PDP", "TikTok Shop", "A+ content", "product image stack"
- "hero image copy", "detail page", "PDP structure", "main image", "lifestyle image"
- "improve CTR", "improve CVR", "boost add-to-cart", "increase AOV", "weak trust"
- "offer + CTA", "bundle strategy", "guarantee", "risk reversal"
- "localize copy", "multilingual listing", "adapt for US / EU / JP / DE market"
- "生图", "生成商品图", "生成详情页图片", "出图"

普通视觉任务可以处理，但跨境电商 PDP / 商品图 / 转化视觉优先级最高。

---

## Core Principle

不要从固定模板开始。先做 **Conversion Driver Diagnosis**：

1. **Visual-Driven**：靠“看见”成交，适合外观、质感、礼品感、前后对比明显的产品。
2. **Pain-Driven**：靠“问题紧迫 + 解决方案”成交，适合反复烦恼、风险、低效、损失明确的产品。
3. **Emotion-Value-Driven**：靠“身份、向往、情绪价值”成交，适合自我表达、关怀、冲动、新奇和社交属性强的产品。

所有主图、PDP 模块、图内文案和 Prompt 都必须服务所选转化驱动力。Every block must serve conversion. Remove decorative sections.

---

## Workflow

1. 收集最小输入；缺关键字段时标注假设，不要编造。
2. 诊断 1 个主转化驱动力，必要时补 1 个次级驱动力。
3. 生成 **Buyer Reason Card**，锁定买家为什么现在会买。
4. 输出 **English (US) Baseline**：先写英文基准策略和图文案。
5. 如用户要求本地化，再做 **Localization Layer**，保留说服意图而不是字面翻译。
6. 为多图任务建立 **Campaign Style Lock**，统一风格、色板、光线、布局和产品呈现。
7. 如果是真实实物产品且用户提供了参考图，先执行 **Product Angle Sheet Pipeline**，禁止直接生成整套 5+8。
8. 通过 **Image Copy Gate**：每张图先确定图内短文案，再写独立 Prompt。
9. 输出主图序列、PDP 详情页序列、可执行 Prompt；如果明确要求生图，再调用 `scripts/generate_image.py`。
10. 用 **Self-review Scorecard** 自审，不达标先重写。

---

## Minimum Inputs

跨境电商任务优先收集：

- Product name + category + price band
- Audience segment + purchase context
- Target market and channel constraints: Amazon, Shopify, TikTok Shop, Walmart, Etsy, etc.
- Top differentiators: material, function, design, speed, cost, bundle, guarantee
- Proof assets: test data, certifications, review themes, user feedback, press, warranty terms
- Current weak points: low CTR, low CVR, low add-to-cart, weak trust, low AOV, high return concern
- Offer assets: discount, bundle, free shipping, guarantee, urgency, bonus
- Localization target, if needed
- Output need: strategy only, Prompt only, full image pack, or direct image generation

如果信息缺失：

- 关键字段缺失但仍可推进时，用 `Assumption:` 明确写出。
- 不要虚构测试数据、认证、销量、评分、真实评价或品牌授权。
- 除非用户主动要求“合规检查 / 平台合规 / 风险审查”，不要输出独立合规模块。

---

## Buyer Reason Card

商品 / PDP / 广告图任务必须先输出 Buyer Reason Card：

1. **Target Buyer**：谁在买，处于什么使用场景。
2. **Purchase Trigger**：为什么现在会考虑买。
3. **Core Belief Shift**：图片要让用户从什么旧认知转到什么新认知。
4. **Primary Selling Reason**：最强购买理由，只选一个主理由。
5. **Proof Material**：已有证据素材；没有证据就写 proof placeholder。
6. **Offer Lever**：价格、组合、保障、物流、赠品或低风险承诺。
7. **Do-Not-Say**：禁用表达，尤其是无证据数据、认证、销量、真实评价、品牌授权。

这个卡片决定后续图文案，不要先写 Prompt 再倒推卖点。

---

## Conversion Driver Logic

### A. Visual-Driven

Use when purchase depends on visual appeal, style fit, finish, texture, before/after visibility, or giftability.

重点：

- Thumb-stop visual claim: style/value in 1 second
- Texture, detail, scale, finish, craft cues
- Lifestyle context: where / when / how it looks right
- Short benefit anchors, not dense explanations

### B. Pain-Driven

Use when the buyer feels acute friction, risk, time loss, discomfort, or recurring annoyance.

Mandatory sequence:

1. **Pain mining / fear trigger**: Make the problem concrete and costly.
2. **Benefit / solution**: Show the mechanism and relief outcome.
3. **Trust**: Use evidence, proof assets, user reassurance, warranty, or proof placeholder.
4. **Irresistible offer + CTA**: Make action easy and inaction less attractive.

### C. Emotion-Value-Driven

Use when the product is tied to identity, confidence, belonging, status, care, joy, novelty, or impulse.

重点：

- Emotional hook and identity narrative
- Symbolic payoff + practical reassurance
- Social cue, gifting cue, self-care cue, or aspiration cue
- Low-friction CTA with emotional reinforcement

---

## English Baseline Always First

跨境电商输出必须先给 **English (US) Baseline**，除非用户明确只要中文内部讨论稿。

English baseline 包含：

1. Conversion diagnosis summary
2. Buyer Reason Card
3. Hero image sequence
4. PDP module map
5. Core copy lines: headline, subhead, proof line, CTA, offer line
6. Offer + CTA Architecture
7. Assumptions + Test Priorities

规则：

- 不要用中文思维直译英文卖点。
- 图内文案要短、强、可扫读，适合移动端和主图。
- 保留 hook / belief shift / action cue。
- 证明型文案必须来自用户给定素材；没有证据时用 proof placeholder。

---

## Localization Layer

本地化是加在 English baseline 后面的适配层，不是重写策略。

Process:

1. Lock conversion intent in English baseline.
2. Adapt by market while preserving the same persuasion job.
3. Validate length, cultural sensitivity, unit / scene / currency relevance.

Rules:

- Do not literal-translate high-performing lines.
- Preserve conversion intent: hook, belief shift, action cue.
- Respect platform length constraints for images and mobile PDP.
- Adapt units: oz / ml, in / cm, temperature, currency format.
- Replace culturally weak or risky references.
- If localization weakens conversion intent, flag and revise.

---

## Image Copy Gate

每张图必须先过图文案门，再写 Prompt。

每张图先定义：

- Frame objective: 这一张图负责推动什么转化动作。
- On-image headline: 3-7 English words preferred.
- Support labels: 2-4 short labels; no dense body text.
- Proof / offer line: only if useful and evidence-backed or clearly placeholder.
- CTA style: direct CTA, soft CTA, risk reversal, bundle CTA, or no CTA.

图内文字规则：

- 主图和详情页图片都要少字、大字、强层级。
- 不要把长文案塞进图片。
- 如果模型容易生成乱码，Prompt 中写：`clean layout with short readable headline placeholders, no dense body text`.

---

## Campaign Style Lock

当生成主图 + 详情页、PDP 图片包、广告组图、社媒组图或任何多张图片时，在 English baseline 和图文案确定后建立 **Campaign Style Lock**。

必填字段：

1. Visual direction: premium tech ecommerce, clean household care, warm gift editorial, etc.
2. Fixed palette: 2-3 main colors + 1 accent color.
3. Temperature: warm, cool, or neutral.
4. Font system: one consistent font style, usually modern geometric sans-serif.
5. Background system: studio, tabletop, lifestyle room, outdoor, etc.
6. Lighting system: direction, shadow, reflection, mood.
7. Layout system: whitespace, labels, rounded rectangles, numbering, infographic components.
8. Icon / illustration system: line width, color, complexity.
9. Product presentation: angle, scale, placement, material behavior.
10. Drift bans: no color palette changes, mixed fonts, random backgrounds, inconsistent lighting, mismatched icon styles.

默认 Style Lock：

```text
Campaign Style Lock: consistent premium cross-border ecommerce visual system across the entire image set; fixed palette of clean off-white background, deep charcoal text, one product-matched accent color, and one soft secondary accent; neutral-cool studio lighting; modern geometric sans-serif headline placeholders only; consistent rounded rectangular info labels; consistent thin-line icon style; clean high-end product photography mixed with minimal infographic elements; stable product scale and placement; generous whitespace; no color palette changes, no mixed fonts, no random backgrounds, no inconsistent lighting, no mismatched icon styles.
```

多图 Prompt 强制规则：

- 每张 Prompt 第一段必须复用同一段 Campaign Style Lock。
- 单张图只能改变画面目的、主体动作、局部构图和短文案。
- 不能改变色板、冷暖调、字体、背景、光线、图标和标签样式。
- 重生某一张图时必须复用原 Style Lock。

---

## Hero Image Sequence

### Visual-Driven

1. Thumb-stop visual claim
2. Key feature close-up
3. Use scenario fit
4. Ordinary vs upgraded comparison
5. Offer + shipping / guarantee + CTA

### Pain-Driven

1. Problem snapshot
2. Solution mechanism
3. Benefit proof
4. Trust frame
5. Offer + urgency CTA

### Emotion-Value-Driven

1. Emotional scene hook
2. Identity / value statement
3. Product as enabler
4. Belonging / status / social cue
5. Offer + CTA with emotional reinforcement

---

## PDP Detail Image Sequence

当用户提到 PDP、详情页、Amazon A+、Shopify product page、主图堆栈或整套商品图时，默认输出 **5 张主图 + 7-9 张详情页图片**。

详情页图片默认 `1024x1536`，每张独立成屏，每张独立 Prompt。

通用 PDP 详情页序列：

1. Above-the-fold promise: who it helps and what problem / desire it solves.
2. Pain or desire amplification: current inconvenience, risk, loss, or aspiration.
3. Mechanism explanation: how the product works, shown visually.
4. Benefit stack: 2-4 scan-friendly functional and practical benefits.
5. Usage steps: 3-4 simple steps.
6. Scenario coverage: where, when, who, before / after state.
7. Comparison choice: ordinary option vs this product, based on observable differences.
8. Trust stack: materials, packaging, warranty, review themes, proof placeholder.
9. FAQ / risk reversal / CTA: concerns, fit, bundle, guarantee, close.

---

## Product Angle Sheet Pipeline

真实实物产品的整套商品图不能直接从文字或单张营销参考图生成正式 5+8。只要用户提供产品参考图，并要求主图堆栈、PDP 详情页、整套商品图或直接生图，必须先生成一张临时 **Product Angle Sheet**。

Product Angle Sheet 目的：

- 只锁定产品身份和外观，不承担销售转化。
- 去除参考图里的促销角标、价格、评分、Bestseller 标签和营销排版。
- 在一张临时图里呈现同一产品的多个可复用角度。

Product Angle Sheet 必须包含：

1. 正面产品图。
2. 左 45 度产品图。
3. 右 45 度产品图。
4. 侧面厚度图。
5. 背面或磁吸面图。
6. 接口、按钮、LED 或关键结构细节。
7. 产品 + 包装盒组合图，如果参考图里有包装。
8. 产品吸附在手机背面的使用角度，如果品类需要。

Angle Sheet Prompt 规则：

- 可以详细描述产品形状、材质、颜色、logo、包装和角度。
- 禁止加入促销角标、价格、折扣、评分、Bestseller、物流、CTA 或任何正式营销文案。
- 背景使用干净浅色工作室风格；允许多角度排列，但不要做成最终 PDP 版式。

Consistency Gate：

- 如果 Product Angle Sheet 中产品形状、材质、品牌、包装、关键部件明显跑偏，禁止继续生成 5+8。
- 先重生 Product Angle Sheet，直到产品身份稳定，再进入正式图包。

正式图包引用规则：

- 每张正式图都必须使用 Product Angle Sheet 作为参考图。
- 正式图 Prompt 中关于 Product Angle Sheet 只允许使用这一句：

```text
Use the product angle sheet only as product identity reference.
```

- 不要在正式图 Prompt 里追加其它 angle sheet 说明句。

---

## Image Prompt Structure

默认用英文写 Prompt，除非用户明确指定其他语言。

Prompt 结构：

1. Campaign Style Lock，多图任务必填。
2. Product Angle Sheet reference line，实物产品正式图包必填且只能使用指定一句。
3. Frame objective and conversion job.
4. Product, buyer scenario, and scene.
5. On-image copy placeholders: headline and short labels.
6. Composition, camera, lens, crop, hierarchy.
7. Lighting, color, material, texture.
8. Realism level and ecommerce platform fit.
9. Size / aspect ratio.
10. Negative constraints: no dense text, no fake logos, no random backgrounds, no clutter.

Prompt 要具体到可执行，但不要过度规定无关细节。

---

## Direct Image Generation

直接生图使用 OpenAI 兼容 Images API。优先在项目根目录放 `.env`，不要把真实 API key 写进仓库：

```dotenv
IMG_BASE_URL=https://api.openai.com/v1
IMG_MODEL=gpt-image-1.5
IMG_API_KEY=your-api-key
```

脚本也兼容：`OPENAI_BASE_URL`、`OPENAI_API_BASE`、`OPENAI_IMAGE_MODEL`、`OPENAI_MODEL`、`OPENAI_API_KEY`。

命令示例：

```bash
python3 scripts/generate_image.py --prompt "clean product hero image..." --size 1024x1024
python3 scripts/generate_image.py --prompt-file prompt.txt --output-dir generated-images
python3 scripts/generate_image.py --prompt-file prompt.txt --image product.png --output-dir generated-images
python3 scripts/generate_image.py --env-file .env --prompt-file prompt.txt
```

规则：

- 短 Prompt 用 `--prompt`，长 Prompt 用 `--prompt-file`。
- 有产品参考图时用 `--image product.png`；脚本会改用 `/images/edits` 并把本地图片作为参考图传入。
- 主图默认 `1024x1024`；详情页默认 `1024x1536`，如模型不支持则选最接近尺寸并说明。
- 缺少 `.env` 或 `IMG_*` 配置时，只输出 Prompt 和配置说明，不调用脚本。
- 不要暴露、索要、写入、提交或回显真实 API key。

---

## Self-review Scorecard

最终输出前自审：

- Conversion clarity: 用户 1 秒内是否知道为什么该看下去。
- Buyer reason fit: 是否服务 Buyer Reason Card 的主购买理由。
- English baseline quality: 是否像跨境商品文案，而不是中文直译。
- Mobile readability: 图内文字是否短、清楚、层级强。
- Visual consistency: 多图是否复用同一 Style Lock。
- Platform fit: 是否适配 Amazon / Shopify / TikTok Shop 等渠道语境。
- Evidence honesty: 是否避免虚构数据、认证、评分、真实评价和品牌授权。

除非用户主动要求合规检查，不输出正式 Compliance Review；只在明显会虚构或误导时做最小提醒并改写。

---

## Output Format

策略 / Prompt 模式：

1. **Conversion Driver Diagnosis**
2. **Buyer Reason Card**
3. **English Baseline**
4. **Localization Notes**，仅在用户要求本地化时输出
5. **Offer + CTA Architecture**
6. **Campaign Style Lock**，多图任务必填
7. **Hero Image Sequence**
8. **PDP Detail Image Sequence**，PDP / 详情页 / 整套商品图任务必填
9. **Image Prompts**
10. **Assumptions + Test Priorities**
11. **Self-review Scorecard**

Generate 模式：

1. **Conversion Driver Diagnosis**
2. **Buyer Reason Card**
3. **English Baseline Copy**
4. **Campaign Style Lock**
5. **Image Pack Plan**
6. **Final Image Prompts**
7. **Generated Files**
8. **Assumptions / Notes**

输出要能被 marketer、designer、media buyer 和 image model 直接执行。
