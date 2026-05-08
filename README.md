# Cross-Border PDP Conversion Strategy Skill

一个面向 Codex / OpenClaw 的跨境电商 PDP 转化策略 Skill。

它的目标不是先做“好看图片”，而是先判断商品为什么能卖，再输出英文基准文案、主图 / 详情页结构、图内短文案、可执行 AI 生图 Prompt，并在配置 OpenAI 兼容图片 API 后直接出图。

## 适用场景

- Amazon listing、Shopify PDP、TikTok Shop、Amazon A+ content。
- 商品主图堆栈、PDP 详情页图片、广告图、优惠图、对比图、场景图。
- CTR、CVR、加购率、AOV、信任感弱等跨境电商转化问题。
- 英文基准文案、市场本地化、单位 / 货币 / 场景适配。
- 生成整套商品图 Prompt，或直接调用图片 API 生图。

普通视觉图也可以处理，但这个 Skill 的核心定位是跨境电商转化。

## 核心工作流

1. 收集产品、受众、价格带、渠道、卖点、证明素材、当前漏斗弱点。
2. 诊断主要转化驱动力：视觉驱动、痛点驱动、情感价值驱动。
3. 生成 Buyer Reason Card，明确用户为什么现在会买。
4. 先输出 English (US) baseline，再做可选本地化。
5. 确定每张图的图内短文案，再写 Prompt。
6. 多图任务建立 Campaign Style Lock，保持整套图风格一致。
7. 默认输出 5 张主图 + 7-9 张详情页图片。
8. 用户明确要求生图且 API 配置完整时，调用 `scripts/generate_image.py`。

合规默认弱化：除非你主动要求“合规检查 / 平台合规 / 风险审查”，Skill 不输出独立合规模块；只保留最小真实性底线，不虚构数据、认证、销量、评分、真实评价或品牌授权。

## 转化驱动力

### Visual-Driven

适合外观、质感、礼品感、风格匹配、前后对比明显的产品。

输出重点：视觉主张、质感细节、场景匹配、快速扫读利益点。

### Pain-Driven

适合买家有反复烦恼、风险、低效、时间损失或不适的产品。

输出顺序：痛点挖掘 → 解决机制 → 利益证明 → 信任 → Offer + CTA。

### Emotion-Value-Driven

适合身份表达、自我关怀、归属感、地位、新奇和冲动购买产品。

输出重点：情绪钩子、身份叙事、产品作为实现方式、社交信号、低摩擦 CTA。

## 输出内容

策略 / Prompt 模式通常输出：

1. Conversion Driver Diagnosis
2. Buyer Reason Card
3. English Baseline
4. Localization Notes，按需输出
5. Offer + CTA Architecture
6. Campaign Style Lock，多图任务必填
7. Hero Image Sequence
8. PDP Detail Image Sequence
9. Image Prompts
10. Assumptions + Test Priorities
11. Self-review Scorecard

Generate 模式会额外输出生成文件路径。

## API 配置

这个 Skill 不内置 API，也不共享密钥。你需要在项目根目录创建 `.env`：

```dotenv
IMG_BASE_URL=https://api.openai.com/v1
IMG_MODEL=gpt-image-1.5
IMG_API_KEY=your-api-key
```

脚本也兼容常见别名：

- `OPENAI_BASE_URL`
- `OPENAI_API_BASE`
- `OPENAI_IMAGE_MODEL`
- `OPENAI_MODEL`
- `OPENAI_API_KEY`

不要把真实 API key 写进 README、`SKILL.md`、脚本、Git 提交或聊天记录。

## 生图脚本用法

直接传入 Prompt：

```bash
python3 scripts/generate_image.py --prompt "clean product hero image, premium studio lighting, white background" --size 1024x1024
```

从文件读取 Prompt：

```bash
python3 scripts/generate_image.py --prompt-file prompt.txt --output-dir generated-images
```

使用产品参考图生成更一致的商品图：

```bash
python3 scripts/generate_image.py --prompt-file prompt.txt --image product.png --output-dir generated-images
```

更多参数：

```bash
python3 scripts/generate_image.py \
  --prompt-file prompt.txt \
  --image product.png \
  --output-dir generated-images \
  --size 1024x1024 \
  --quality high \
  --format png \
  --n 1
```

指定 `.env` 文件：

```bash
python3 scripts/generate_image.py --env-file .env --prompt-file prompt.txt
```

脚本支持：

- `--prompt`
- `--prompt-file`
- `--output-dir`
- `--env-file`
- `--size`
- `--quality`
- `--format`
- `--n`
- `--image`

脚本只使用 Python 标准库，不需要安装第三方依赖。

## 图片包规则

当你提到“详情页、PDP、Amazon A+、Shopify 商品页、主图堆栈、整套商品图、商品详情图片”时，Skill 默认输出完整图片包：

- 5 张主图：首图卖点、机制 / 功能、利益证明、对比或场景、优惠 / 保障。
- 7-9 张详情页图片：首屏承接、痛点 / 欲望放大、机制解释、核心利益、使用步骤、场景覆盖、对比选择、信任背书、FAQ / 风险逆转 / CTA。
- 主图默认 `1024x1024`。
- 详情页图片默认 `1024x1536`。
- 每张图都使用独立 Prompt，避免把多屏详情页挤在一张拼图里。
- 多图必须复用同一段 Campaign Style Lock。

## 实物产品基准图流程

如果是真实实物产品，并且你提供了产品参考图，Skill 不应直接生成 5 张主图 + 8 屏详情页。

正确流程：

1. 先生成一张临时 `Product Angle Sheet`。
2. 这张基准图只用于锁定产品身份，不作为最终交付图。
3. 基准图要包含正面、左 45 度、右 45 度、侧面厚度、背面或磁吸面、接口 / 按钮 / LED 细节、产品 + 包装盒组合、吸附手机背面的使用角度。
4. 基准图禁止出现促销角标、价格、折扣、评分、Bestseller、物流、CTA 或正式营销文案。
5. 如果基准图里产品外观跑偏，先重生基准图，不进入正式 5+8。
6. 正式 5+8 每张图都以这张基准图作为参考图生成。

正式图 Prompt 中关于基准图只允许使用这一句：

```text
Use the product angle sheet only as product identity reference.
```

默认 Style Lock：

```text
Campaign Style Lock: consistent premium cross-border ecommerce visual system across the entire image set; fixed palette of clean off-white background, deep charcoal text, one product-matched accent color, and one soft secondary accent; neutral-cool studio lighting; modern geometric sans-serif headline placeholders only; consistent rounded rectangular info labels; consistent thin-line icon style; clean high-end product photography mixed with minimal infographic elements; stable product scale and placement; generous whitespace; no color palette changes, no mixed fonts, no random backgrounds, no inconsistent lighting, no mismatched icon styles.
```

## 示例输入

```text
Product: Self-heating eye mask
Category: Sleep & wellness
Price band: USD 19-29
Audience: stressed office workers in the US market
Differentiators: 40-minute heat duration, unscented option, soft skin-safe material
Proof assets: 4.7 star reviews, dermatology-tested report, 30-day guarantee
Channel: Amazon PDP + main image stack
Current weak points: decent CTR, low add-to-cart, weak trust perception
Goal: improve CVR and trust
Need: 5 hero images + 8 PDP detail images, with executable image prompts
```

## 输出形状示例

```text
1. Conversion Driver Diagnosis
   Primary: Pain-Driven
   Why: recurring discomfort + clear relief mechanism + trust barrier.

2. Buyer Reason Card
   Target Buyer: stressed office workers.
   Purchase Trigger: eye fatigue and sleep friction after long screen time.
   Core Belief Shift: from "just another eye mask" to "a low-effort decompression ritual".

3. English Baseline
   Hero headline: Melt Away Screen-Day Tension
   Proof line: 40-minute gentle warmth
   CTA style: soft risk reversal

4. Hero Image Sequence
   Frame 1: problem snapshot
   Frame 2: warmth mechanism
   Frame 3: relief benefit
   Frame 4: trust frame
   Frame 5: offer + guarantee

5. Image Prompts
   Prompt 01: Campaign Style Lock... [independent executable prompt]
```

## 推荐工作流

1. 先提供产品、受众、渠道、价格带、差异化和证明素材。
2. 让 Skill 输出 English baseline 和整套图片 Prompt。
3. 人工确认 Buyer Reason Card、Offer + CTA 和图内短文案。
4. 配置 `IMG_*` 环境变量后生图。
5. 保留 2-3 个核心钩子做 A/B 测试：CTR、加购率、CVR、AOV。

## 局限性

- 支持文本生图和单张产品参考图生图；暂不支持 mask 局部重绘。
- 需要 OpenAI 兼容 Images API；非兼容服务可能需要额外适配。
- 不同服务商对 `size`、`quality`、`format`、`n` 的支持可能不同。
- 生图质量、速度和费用取决于你选择的模型和服务商。
- Skill 提供转化策略和生产简报，不保证实际投放表现。
