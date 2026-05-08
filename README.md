# Cross-Border PDP Conversion Strategy Skill

一个面向 Codex / OpenClaw 的跨境电商 PDP 转化策略 Skill。

它的目标是先判断商品为什么能卖，再输出英文基准文案、主图 / 详情页结构、图内短文案、可执行 AI 生图 Prompt，并在配置 OpenAI 兼容图片 API 后直接出图。

## 适用场景

- Amazon listing、Shopify PDP、TikTok Shop、Amazon A+ content。
- 商品主图堆栈、PDP 详情页图片、广告图、优惠图、对比图、场景图。
- CTR、CVR、加购率、AOV、信任感弱等跨境电商转化问题。
- 英文基准文案、市场本地化、单位 / 货币 / 场景适配。
- 生成整套商品图 Prompt，或直接调用图片 API 生图。

普通视觉图也可以处理，但这个 Skill 的核心定位是跨境电商转化。

## 核心工作流

1. 先按权重补齐最小输入：用户输入 / 附件 / 上下文 > 自行联网研究 > 逻辑推理 > 假设 / 默认设定。
2. 收集产品、受众、价格带、渠道、卖点、证明素材、用户好评 / 推荐、合规偏好、当前漏斗弱点。
3. 诊断主要转化驱动力：视觉驱动、痛点驱动、情感价值驱动。
4. 生成 Buyer Reason Card，明确用户为什么现在会买。
5. 先输出 English (US) baseline，再做可选本地化。
6. 确定每张图的图内短文案，再写 Prompt。
7. 多图任务建立 Campaign Style Lock，保持整套图风格一致。
8. 默认输出 5 张主图 + 7-9 张详情页图片。
9. 用户明确要求生图且 API 配置完整时，调用 `scripts/generate_image.py`。

合规默认忽略：只有你主动要求“合规检查 / 平台合规 / 风险审查”时，Skill 才输出独立合规模块；默认只保留最小真实性底线，数据、认证、销量或品牌授权必须来自用户提供或可验证来源。用户好评 / 推荐按合规开关单独处理。

## 缺失信息补齐机制

信息缺失时，Skill 会先问用户补齐缺失字段；用户未答、授权继续或要求快速出图时，再联网研究公开资料。

1. **用户输入 / 附件 / 上下文**：用户文字、上传图、参考图、链接、文件名、历史上下文、项目文件。
2. **用户追问补齐**：初始材料缺字段时，先问用户补齐。
3. **自行联网研究**：产品官网、品牌页、公开商品页、平台规则、公开测评或规格资料。
4. **逻辑推理**：基于品类、渠道、目标市场和已知卖点推断策略方向。
5. **假设 / 默认设定**：最后手段，只用于核心真实性之外的缺口。

高权重信息覆盖低权重信息。低权重信息只用于补充用户输入、附件或上下文。

经过上述补齐后仍需用户确认时，才问用户的关键信息：

- 产品身份：产品是什么；实物产品至少要有产品名、参考图或清楚外观描述。
- 目标市场 / 语言：例如 US English、德国德语、日本日语。
- 渠道 / 资产类型：Amazon、Shopify、TikTok Shop、广告图、PDP、主图堆栈。
- 输出模式：只要策略 / Prompt，还是直接生图。
- 硬性约束：必须出现或必须避开的品牌名、价格、折扣、颜色、卖点、禁用表达。

优先询问但可用假设继续的信息：

- 价格带、折扣、物流、保障。
- 目标人群和购买场景。
- 核心差异化和证明素材。
- 用户好评、推荐理由、评论主题、testimonial snippets。
- 合规偏好：是否要考虑平台 / 广告 / 类目合规；默认忽略。
- 当前漏斗弱点：CTR、CVR、加购率、信任感、AOV。
- 竞品方向、参考风格、SKU / 颜色 / 配件。

提问原则：

- 初始材料缺字段时先问用户；用户未答、授权继续或要求快速出图时，再联网研究公开资料。
- 合规偏好属于用户选择，最小输入阶段需要问；用户未明确启用时默认忽略合规。
- 一次最多问 3-5 个真正影响结果的问题。
- 上下文已明显给出的信息直接采用。
- 用户说“你看着办 / 先出一版”时可以继续，但会列出 `Assumptions Used`。
- 非关键缺失用假设处理；关键缺失先追问。

输出中会用短列表告知信息来源：

- `User-provided`：用户明确提供。
- `Attachment/context`：附件、参考图、项目文件或历史上下文得出。
- `Web-researched`：联网研究得出。
- `Inferred`：逻辑推理得出。
- `Assumption`：为推进任务做出的假设。
- `Default`：Skill 默认设定。

只要用了逻辑推理、假设或默认值，输出必须包含 **Assumptions / Defaults Used**，例如默认主图尺寸、详情页尺寸、默认 Style Lock、推断目标市场等。

## 合规偏好

合规默认忽略。Skill 只会在用户明确要求“考虑合规 / 平台合规 / 广告合规 / 类目合规 / 风险审查”时走合规路线。

启用合规后会额外处理：

- 目标平台、国家 / 地区、类目和禁用表达。
- 功效、医疗、认证、比较、折扣、评价、授权、绝对化表达。
- 哪些表达可用，哪些需要证据，哪些建议弱化。

未启用合规时，省略独立合规模块；数据、认证、销量或品牌授权仍需来自用户提供或可验证来源。用户好评 / 推荐按合规开关单独处理。

用户好评 / 推荐规则：

- 合规启用：只用真实好评、真实推荐或真实评论主题；没有真实素材时，用利益、使用步骤、FAQ、保障或场景图替换 Review / recommendation 图。
- 合规忽略 / 关闭：没有真实素材时，可以编写模拟好评、推荐理由或 review-style quote，并在 `Assumptions / Defaults Used` 中说明。
- 第三方平台截图、真实用户名、认证标识和可核验评价数量只在用户提供真实素材时使用。

## 转化驱动力

### Visual-Driven

适合外观、质感、礼品感、风格匹配、前后对比明显的产品。

输出重点：视觉主张、质感细节、场景匹配、快速扫读利益点。

### Pain-Driven

适合买家有反复烦恼、风险、低效、时间损失或使用负担的产品。

输出顺序：痛点挖掘 → 解决机制 → 利益证明 → 信任 → Offer + CTA。

### Emotion-Value-Driven

适合身份表达、自我关怀、归属感、地位、新奇和冲动购买产品。

输出重点：情绪钩子、身份叙事、产品作为实现方式、社交信号、低摩擦 CTA。

## 输出内容

策略 / Prompt 模式通常输出：

1. Missing Info Questions，仅在按权重补齐后仍关键缺失时输出
2. Conversion Driver Diagnosis
3. Buyer Reason Card
4. English Baseline
5. Localization Notes，按需输出
6. Offer + CTA Architecture
7. Campaign Style Lock，多图任务必填
8. Hero Image Sequence
9. PDP Detail Image Sequence
10. Image Prompts
11. Assumptions / Defaults Used，只要用到推理、假设或默认设定就输出
12. Test Priorities
13. Self-review Scorecard

Generate 模式会额外输出生成文件路径。

## API 配置

这个 Skill 通过你本地配置的 API 工作，密钥由你自己保存。你需要在项目根目录创建 `.env`：

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

真实 API key 只放在本地 `.env` 或运行环境中；README、`SKILL.md`、脚本、Git 提交和聊天记录使用占位值。

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

脚本只使用 Python 标准库，无需安装第三方依赖。

## 图片包规则

当你提到“详情页、PDP、Amazon A+、Shopify 商品页、主图堆栈、整套商品图、商品详情图片”时，Skill 默认输出完整图片包：

- 5 张主图：首图卖点、机制 / 功能、利益证明、对比或场景、优惠 / 保障。
- 7-9 张详情页图片：首屏承接、痛点 / 欲望放大、机制解释、核心利益、使用步骤、场景覆盖、对比选择、用户好评 / 推荐、信任背书、FAQ / 风险逆转 / CTA。
- 主图默认 `1024x1024`。
- 详情页图片默认 `1024x1536`。
- 每张图都使用独立 Prompt，避免把多屏详情页挤在一张拼图里。
- 多图必须复用同一段 Campaign Style Lock。

详情页必须使用用户好评和推荐素材：

- 合规启用时：只使用真实好评、真实推荐或真实评论主题；没有真实素材时，用利益、使用步骤、FAQ、保障或场景图替换 Review / recommendation 图。
- 合规忽略 / 关闭时：没有真实素材也可以编写模拟好评、推荐理由或 review-style quote，并在 `Assumptions / Defaults Used` 中说明。
- 第三方平台截图、真实用户名、认证标识和可核验评价数量只在用户提供真实素材时使用。

## 实物产品基准图流程

如果是真实实物产品，并且你提供了产品参考图，Skill 会先生成一张临时 `Product Angle Sheet`，再生成完整商品图包。

正确流程：

1. 先生成一张临时 `Product Angle Sheet`。
2. 这张基准图只用于锁定产品身份，最终交付图另行生成。
3. 基准图要包含正面、左 45 度、右 45 度、侧面厚度、背面或磁吸面、接口 / 按钮 / LED 细节、产品 + 包装盒组合、吸附手机背面的使用角度。
4. 基准图只包含产品角度与结构信息；促销角标、价格、折扣、评分、Bestseller、物流、CTA 和正式营销文案留到正式图包阶段。
5. 如果基准图里产品外观跑偏，先重生基准图。
6. 产品身份稳定后，完整商品图包里的每张图都以这张基准图作为参考图生成。

正式图 Prompt 中关于基准图只允许使用这一句：

```text
Use the product angle sheet only as product identity reference.
```

默认 Style Lock：

```text
Campaign Style Lock: consistent premium cross-border ecommerce visual system across the entire image set; fixed palette of clean off-white background, deep charcoal text, one product-matched accent color, and one soft secondary accent; neutral-cool studio lighting; modern geometric sans-serif headline placeholders only; consistent rounded rectangular info labels; consistent thin-line icon style; clean high-end product photography mixed with minimal infographic elements; stable product scale and placement; generous whitespace; fixed color palette, single font system, stable backgrounds, consistent lighting, matched icon styles.
```

## 示例输入

```text
Product: Self-heating eye mask
Category: Sleep & wellness
Price band: USD 19-29
Audience: stressed office workers in the US market
Differentiators: 40-minute heat duration, unscented option, soft skin-safe material
Proof assets: 4.7 star reviews, dermatology-tested report, 30-day guarantee
Review / recommendation assets: review theme says warmth feels relaxing; users recommend it for after-work screen fatigue
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

1. 先提供产品、目标市场、渠道、输出模式和硬性约束；参考图和链接越完整越好。
2. Skill 会先从用户材料提取已知信息，缺字段先问用户；用户未答、授权继续或要求快速出图时，再联网研究和逻辑推理补齐。
3. 让 Skill 输出 English baseline 和整套图片 Prompt。
4. 人工确认 Buyer Reason Card、Offer + CTA 和图内短文案。
5. 配置 `IMG_*` 环境变量后生图。
6. 保留 2-3 个核心钩子做 A/B 测试：CTR、加购率、CVR、AOV。

## 局限性

- 支持文本生图和单张产品参考图生图；当前支持范围未包含 mask 局部重绘。
- 需要 OpenAI 兼容 Images API；非兼容服务可能需要额外适配。
- 各服务商对 `size`、`quality`、`format`、`n` 的支持可能有差异。
- 生图质量、速度和费用取决于你选择的模型和服务商。
- Skill 提供转化策略和生产简报；实际投放表现取决于产品、素材、渠道、预算和测试执行。
