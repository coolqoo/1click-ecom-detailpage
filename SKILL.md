---
name: crossborder-pdp-conversion-strategy
description: Build high-converting cross-border ecommerce PDP, hero image, product image stack, and AI image prompt strategy by resolving minimum inputs in priority order from user input, attachments, context, web research, logic inference, and explicit assumptions/defaults; then diagnose the conversion driver, produce an English (US) baseline, optionally localize while preserving intent, and generate executable image prompts or images through the bundled OpenAI-compatible image script.
---

# Cross-Border PDP Conversion Strategy Skill

当用户需要跨境电商商品主图、PDP 详情页、Amazon / Shopify / TikTok Shop 图片、A+ content、广告图、商品图文案、转化优化、英文基准文案、本地化适配，或直接 AI 生图时，使用这个 Skill。

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

先做 **Conversion Driver Diagnosis**，再决定图片和文案结构：

1. **Visual-Driven**：靠“看见”成交，适合外观、质感、礼品感、前后对比明显的产品。
2. **Pain-Driven**：靠“问题紧迫 + 解决方案”成交，适合反复烦恼、风险、低效、损失明确的产品。
3. **Emotion-Value-Driven**：靠“身份、向往、情绪价值”成交，适合自我表达、关怀、冲动、新奇和社交属性强的产品。

所有主图、PDP 模块、图内文案和 Prompt 都必须服务所选转化驱动力。Every block must serve conversion. Remove decorative sections.

---

## Workflow

1. 先执行 **Minimum Input Resolution Gate**：按信息权重补齐最小输入，优先用户材料，其次联网研究，再逻辑推理，最后才用假设 / 默认设定。
2. 收集最小输入；非关键缺失可标注 `Assumption` / `Default` 后继续，事实类内容只采用可追溯来源。
3. 诊断 1 个主转化驱动力，必要时补 1 个次级驱动力。
4. 生成 **Buyer Reason Card**，锁定买家为什么现在会买。
5. 输出 **English (US) Baseline**：先写英文基准策略和图文案。
6. 如用户要求本地化，再做 **Localization Layer**，保留说服意图并按目标市场重写。
7. 为多图任务建立 **Campaign Style Lock**，统一风格、色板、光线、布局和产品呈现。
8. 如果是真实实物产品且用户提供了参考图，先执行 **Product Angle Sheet Pipeline**，再生成完整商品图包。
9. 通过 **Image Copy Gate**：每张图先确定图内短文案，再写独立 Prompt。
10. 输出主图序列、PDP 详情页序列、可执行 Prompt；如果明确要求生图，再调用 `scripts/generate_image.py`。
11. 用 **Self-review Scorecard** 自审，未达标先重写。

合规模块只在用户主动要求“合规检查 / 平台合规 / 风险审查”时输出；默认只保留最小真实性底线。

---

## Minimum Inputs

跨境电商任务优先收集：

- Product name + category + price band
- Audience segment + purchase context
- Target market and channel constraints: Amazon, Shopify, TikTok Shop, Walmart, Etsy, etc.
- Top differentiators: material, function, design, speed, cost, bundle, guarantee
- Proof assets: test data, certifications, review themes, user feedback, press, warranty terms
- Review and recommendation assets: user praise, testimonial snippets, recommendation reasons, review themes
- Current weak points: low CTR, low CVR, low add-to-cart, weak trust, low AOV, high return concern
- Offer assets: discount, bundle, free shipping, guarantee, urgency, bonus
- Compliance preference: ask whether to consider platform / ad / category compliance; default is ignore
- Localization target, if needed
- Output need: strategy only, Prompt only, full image pack, or direct image generation

---

## Minimum Input Resolution Gate

搜集最小输入时，必须按以下权重从高到低处理。高权重信息覆盖低权重信息；低权重信息只用于补充用户输入、附件和上下文。

1. **用户输入 / 附件 / 上下文**：用户文字、上传图片、参考图、文件名、链接、历史对话、项目文件。最高优先级。
2. **用户追问补齐**：初始材料缺字段时，先问用户补齐；用户未答、授权继续或要求快速出图时，再进入联网研究。
3. **自行联网研究**：产品官网、品牌页、公开商品页、平台规则、公开测评或规格资料。适合补产品参数、卖点、价格区间、市场语言、渠道语境等可查事实。
4. **逻辑推理**：基于品类、渠道、目标市场、已知卖点做合理推断。只能用于转化驱动力、受众场景、图片结构等策略判断。
5. **假设 / 默认设定**：最后手段。只能用于核心真实性之外的缺口，且必须明确告知用户。

流程：

1. 先从用户文本、图片、链接、文件名、历史上下文中提取已知信息。
2. 对仍缺失的信息，先询问用户补齐。
3. 用户未回答、要求继续或明确授权自行查资料时，再联网搜索可公开查证的信息。
4. 公开资料有限但可合理判断的信息，使用逻辑推理，并标记为 `Inferred`。
5. 仍缺字段但需要继续推进时，必须标记为 `Assumption` 或 `Default`。
6. 合规偏好由用户选择；最小输入阶段要问“是否需要考虑平台/广告/类目合规”，默认忽略。

### Source Labels

输出或内部记录最小输入时，用这些标签标明来源：

- `User-provided`：用户明确提供。
- `Attachment/context`：附件、参考图、项目文件或历史上下文得出。
- `Web-researched`：联网研究得出；最终回答里简短列出来源。
- `Inferred`：逻辑推理得出。
- `Assumption`：为推进任务做出的假设。
- `Default`：Skill 默认设定。

只要使用了 `Inferred`、`Assumption` 或 `Default`，最终输出必须包含 **Assumptions / Defaults Used**，用短列表告知用户。只有在用户明确要求确认后再继续，或硬性约束会明显改变结果时，才暂停等待确认。

### Compliance Preference

最小输入阶段要询问合规偏好：

- 默认值：`Default: Compliance ignored by default; Compliance Path runs only when user explicitly opts in.`
- 如果用户明确说“考虑合规 / 平台合规 / 广告合规 / 类目合规 / 风险审查”，才进入 **Compliance Path**。
- 如果用户未选择合规，正常走转化和生图路线，省略独立合规模块。
- 默认忽略合规时，数据、认证、销量和品牌授权仍需来自用户提供或可验证来源；用户好评 / 推荐按 Review Compliance Switch 处理。

Compliance Path 只在用户明确启用时执行：

1. 询问目标平台、国家/地区、类目和禁用表达。
2. 检查图片文案中的功效、医疗、认证、比较、折扣、评价、授权和绝对化表达。
3. 输出可用表达、需证据表达、建议弱化表达。
4. 再进入 English baseline、图片序列和 Prompt。

### Review Compliance Switch

用户好评 / 推荐素材按合规开关处理：

- **Compliance enabled**：只能使用真实用户好评、真实推荐、真实评论主题或用户提供的 testimonial。没有真实素材时，取消 Review / recommendation 这张图，把该屏替换为利益、使用步骤、FAQ、保障或场景图。
- **Compliance disabled / ignored**：如果没有真实好评或推荐素材，可以编写模拟好评、推荐理由、review-style quote 或 social proof 文案用于转化；在 **Assumptions / Defaults Used** 中说明该内容为生成的营销文案。
- 第三方平台截图、真实用户名、认证标识和可核验评价数量只在用户提供真实素材时使用。

### Assumptions / Defaults Disclosure

任何策略、Prompt 或生图结果，只要使用了逻辑推理、假设或默认设定，必须告诉用户：

- `Inferred:` 从哪些已知信息推理出什么。
- `Assumption:` 为推进任务临时假设了什么。
- `Default:` 使用了哪些 Skill 默认值，例如主图 `1024x1024`、详情页 `1024x1536`、English baseline first、默认 Campaign Style Lock。

在 Prompt 外显式列出假设。用户应该能一眼看到哪些内容来自自己、哪些来自联网研究、哪些是推理或默认。

---

## Buyer Reason Card

商品 / PDP / 广告图任务必须先输出 Buyer Reason Card：

1. **Target Buyer**：谁在买，处于什么使用场景。
2. **Purchase Trigger**：为什么现在会考虑买。
3. **Core Belief Shift**：图片要让用户从什么旧认知转到什么新认知。
4. **Primary Selling Reason**：最强购买理由，只选一个主理由。
5. **Proof Material**：已有证据素材；没有证据就写 proof placeholder。
6. **Review / Recommendation Material**：用户好评、推荐理由、评论主题；按 Review Compliance Switch 决定使用真实素材、跳过该图或生成模拟推荐。
7. **Offer Lever**：价格、组合、保障、物流、赠品或低风险承诺。
8. **Evidence-Bound Claims**：数据、认证、销量、真实评价、品牌授权等表达只在有证据时使用。

这个卡片决定后续图文案。先锁定买家理由，再写 Prompt。

---

## Conversion Driver Logic

### A. Visual-Driven

Use when purchase depends on visual appeal, style fit, finish, texture, before/after visibility, or giftability.

重点：

- Thumb-stop visual claim: style/value in 1 second
- Texture, detail, scale, finish, craft cues
- Lifestyle context: where / when / how it looks right
- Scan-friendly benefit anchors

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
7. Assumptions / Defaults Used + Test Priorities

规则：

- 英文卖点按美国市场语境重写，保持自然、直接、可扫读。
- 图内文案要短、强、可扫读，适合移动端和主图。
- 保留 hook / belief shift / action cue。
- 证明型文案必须来自用户给定素材；没有证据时用 proof placeholder。

---

## Localization Layer

本地化是加在 English baseline 后面的适配层，核心策略沿用 English baseline。

Process:

1. Lock conversion intent in English baseline.
2. Adapt by market while preserving the same persuasion job.
3. Validate length, cultural sensitivity, unit / scene / currency relevance.

Rules:

- Rewrite high-performing lines for local market context.
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
- Support labels: 2-4 short labels; concise labels only.
- Proof / offer line: only if useful and evidence-backed or clearly placeholder.
- Review / recommendation line: if compliance is enabled, use only real praise/testimonials/review themes; if compliance is disabled, synthetic review-style copy is allowed and must be disclosed.
- CTA style: direct CTA, soft CTA, risk reversal, bundle CTA, or CTA omitted.

图内文字规则：

- 主图和详情页图片都要少字、大字、强层级。
- 图内只放短文案，长说明移到页面正文或模块说明。
- 如果模型容易生成乱码，Prompt 中写：`clean layout with short readable headline placeholders, concise labels only`.

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
10. Style consistency requirements: fixed color palette, single font system, stable backgrounds, consistent lighting, matched icon styles.

默认 Style Lock：

```text
Campaign Style Lock: consistent premium cross-border ecommerce visual system across the entire image set; fixed palette of clean off-white background, deep charcoal text, one product-matched accent color, and one soft secondary accent; neutral-cool studio lighting; modern geometric sans-serif headline placeholders only; consistent rounded rectangular info labels; consistent thin-line icon style; clean high-end product photography mixed with minimal infographic elements; stable product scale and placement; generous whitespace; fixed color palette, single font system, stable backgrounds, consistent lighting, matched icon styles.
```

多图 Prompt 强制规则：

- 每张 Prompt 第一段必须复用同一段 Campaign Style Lock。
- 单张图只能改变画面目的、主体动作、局部构图和短文案。
- 保持色板、冷暖调、字体、背景、光线、图标和标签样式一致。
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
8. Review / recommendation stack: user praise, review themes, recommendation reasons, testimonial snippets, social proof layout.
9. Trust stack: materials, packaging, warranty, proof placeholder.
10. FAQ / risk reversal / CTA: concerns, fit, bundle, guarantee, close.

详情页生成规则：

- 详情页必须优先使用用户好评和推荐素材强化信任与购买理由。
- 合规启用时：只使用真实好评、真实推荐或真实评论主题；没有真实素材时，用利益、使用步骤、FAQ、保障或场景图替换 Review / recommendation 图。
- 合规忽略 / 关闭时：没有真实素材也可以编写模拟好评、推荐理由或 review-style quote，并在 Assumptions / Defaults Used 中说明。
- 第三方平台截图、真实用户名、认证标识和可核验评价数量只在用户提供真实素材时使用。

---

## Product Angle Sheet Pipeline

真实实物产品的完整商品图包需要先锁定产品身份。用户提供产品参考图，并要求主图堆栈、PDP 详情页、整套商品图或直接生图时，先生成一张临时 **Product Angle Sheet**。

Product Angle Sheet 目的：

- 只用于锁定产品身份和外观，销售转化由正式图包完成。
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
- 仅包含产品角度与结构信息；促销角标、价格、折扣、评分、Bestseller、物流、CTA 和正式营销文案留到正式图包阶段。
- 背景使用干净浅色工作室风格；允许多角度排列，版式保持基准图用途，与最终 PDP 版式区分。

Consistency Gate：

- 如果 Product Angle Sheet 中产品形状、材质、品牌、包装、关键部件明显跑偏，先重生 Product Angle Sheet。
- 产品身份稳定后，再进入完整商品图包。

正式图包引用规则：

- 每张正式图都必须使用 Product Angle Sheet 作为参考图。
- 正式图 Prompt 中关于 Product Angle Sheet 只允许使用这一句：

```text
Use the product angle sheet only as product identity reference.
```

- 正式图 Prompt 只保留上述 Product Angle Sheet reference line。

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
10. Cleanliness constraints: concise text, verified logos only, stable background, uncluttered composition.

Prompt 要具体到可执行，聚焦会影响生成结果的关键细节。

---

## Direct Image Generation

直接生图使用 OpenAI 兼容 Images API。优先在项目根目录放 `.env`，真实 API key 只放在本地环境配置：

```dotenv
IMG_BASE_URL=https://api.openai.com/v1
IMG_MODEL=gpt-image-1.5
IMG_API_KEY=your-api-key
```

脚本也兼容：`OPENAI_BASE_URL`、`OPENAI_API_BASE`、`OPENAI_IMAGE_MODEL`、`OPENAI_MODEL`、`OPENAI_API_KEY`。

默认 `--mode auto`：

- `IMG_BASE_URL`、`IMG_MODEL`、`IMG_API_KEY` 配置齐全时，脚本直接生成图片。
- 配置缺失时，脚本只输出 Prompt；传入 `--job-dir` 时，同步保存到 `<job-dir>/prompts/`。
- 明确只要 Prompt 时使用 `--mode prompt`。
- 明确强制生图时使用 `--mode image`。

命令示例：

```bash
python3 scripts/generate_image.py --prompt "clean product hero image..." --job-dir generated-images/product-pack-20260509-010946 --asset-type main --size 1024x1024
python3 scripts/generate_image.py --prompt-file prompts/detail-01.txt --job-dir generated-images/product-pack-20260509-010946 --asset-type detail --size 1024x1536
python3 scripts/generate_image.py --prompt-file prompts/angle-sheet.txt --image product.png --job-dir generated-images/product-pack-20260509-010946 --asset-type angle-sheet
python3 scripts/generate_image.py --env-file .env --prompt-file prompt.txt --job-dir generated-images/product-pack-20260509-010946 --asset-type main
```

规则：

- 短 Prompt 用 `--prompt`，长 Prompt 用 `--prompt-file`。
- 有产品参考图时用 `--image product.png`；脚本会改用 `/images/edits` 并把本地图片作为参考图传入。
- 每次完整商品图包创建唯一 `--job-dir`：`generated-images/<product-slug>-pack-<yyyymmdd-hhmmss>`。
- 临时角度图用 `--asset-type angle-sheet`，保存到 `<job-dir>/angle-sheet/`。
- 主图用 `--asset-type main`，保存到 `<job-dir>/main/`。
- 详情页用 `--asset-type detail`，保存到 `<job-dir>/detail/`。
- 额外返回变体或备选图用 `--asset-type extras`，保存到 `<job-dir>/extras/`。
- Prompt 自动保存到 `<job-dir>/prompts/`。
- 主图默认 `1024x1024`；详情页默认 `1024x1536`，如模型仅支持近似尺寸则选最接近尺寸并说明。
- 缺少 `.env` 或 `IMG_*` 配置时，只输出 Prompt 和配置说明。
- 真实 API key 只保存在本地环境变量或 `.env`，输出中使用占位值。

---

## Self-review Scorecard

最终输出前自审：

- Conversion clarity: 用户 1 秒内是否知道为什么该看下去。
- Buyer reason fit: 是否服务 Buyer Reason Card 的主购买理由。
- English baseline quality: 是否像自然的跨境商品文案。
- Mobile readability: 图内文字是否短、清楚、层级强。
- Visual consistency: 多图是否复用同一 Style Lock。
- Platform fit: 是否适配 Amazon / Shopify / TikTok Shop 等渠道语境。
- Evidence honesty: 是否避免虚构数据、认证、评分和品牌授权；用户好评 / 推荐是否按 Review Compliance Switch 处理。

正式 Compliance Review 只在用户主动要求合规检查时输出；明显会虚构或误导时，做最小提醒并改写。

---

## Output Format

策略 / Prompt 模式：

如果按信息权重补齐后，Critical Missing Info 仍缺失，先只输出：

1. **Missing Info Questions**
2. **Known Inputs Extracted**
3. **Attempted Resolution**，说明已从用户材料、联网研究或逻辑推理尝试补齐哪些字段
4. **Why These Questions Matter**

关键信息补齐后再输出：

1. **Conversion Driver Diagnosis**
2. **Buyer Reason Card**
3. **English Baseline**
4. **Localization Notes**，仅在用户要求本地化时输出
5. **Offer + CTA Architecture**
6. **Campaign Style Lock**，多图任务必填
7. **Hero Image Sequence**
8. **PDP Detail Image Sequence**，PDP / 详情页 / 整套商品图任务必填
9. **Image Prompts**
10. **Assumptions / Defaults Used**，只要用到推理、假设或默认设定就必填
11. **Test Priorities**
12. **Self-review Scorecard**

Generate 模式：

1. **Conversion Driver Diagnosis**
2. **Buyer Reason Card**
3. **English Baseline Copy**
4. **Campaign Style Lock**
5. **Image Pack Plan**
6. **Final Image Prompts**
7. **Generated Files**
8. **Assumptions / Defaults Used**
9. **Notes**

输出要能被 marketer、designer、media buyer 和 image model 直接执行。
