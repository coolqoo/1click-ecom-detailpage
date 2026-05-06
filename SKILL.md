---
name: visual-creator
description: Create visual concepts, image-generation prompts, and optional AI-generated images for product hero images, marketing creatives, social posts, ads, ecommerce PDP visuals, and general visual design tasks. Use when the user asks for visual strategy, image prompt writing, product/marketing image direction, or direct text-to-image generation with their own OpenAI-compatible API.
---

# Visual Creator Skill

当用户需要视觉策略、图片 Prompt、商品主图、营销图、社媒图、广告图、电商 PDP 视觉，或要求直接 AI 生图时，使用这个 Skill。

这个 Skill 有两种模式：

1. **Brief / Prompt 模式**：只输出视觉简报和可执行图片 Prompt。
2. **Generate 模式**：当用户明确要求“生图、生成图片、出图、render image”时，先输出最终 Prompt，再调用 `scripts/generate_image.py`。

不要暴露、索要、写入、提交或回显真实 API key。使用者必须通过自己的环境变量配置 API。

---

## 生图配置

直接生图使用 OpenAI 兼容 Images API。优先在项目根目录放 `.env`，不要把真实 API key 写进仓库：

```dotenv
IMG_BASE_URL=https://api.openai.com/v1
IMG_MODEL=gpt-image-1.5
IMG_API_KEY=your-api-key
```

脚本也兼容常见别名：`OPENAI_BASE_URL`、`OPENAI_API_BASE`、`OPENAI_IMAGE_MODEL`、`OPENAI_MODEL`、`OPENAI_API_KEY`。

生图脚本：

```bash
python3 scripts/generate_image.py --prompt "clean product hero image..." --size 1024x1024
python3 scripts/generate_image.py --prompt-file prompt.txt --output-dir outputs
python3 scripts/generate_image.py --env-file .env --prompt-file prompt.txt
```

如果缺少任何生图配置，说明需要在 `.env` 里配置什么，并把最终 Prompt 交给用户，方便用户稍后自行运行。

---

## 核心流程

1. 判断视觉任务类型。
2. 只收集会实质影响图片结果的缺失信息。
3. 构建视觉简报。
4. 如果任务包含多张图，先建立 **Campaign Style Lock**，锁定整套图的色板、冷暖调、字体、背景、光线、布局和图标风格。
5. 写出可执行图片 Prompt；多图任务必须把同一段 Campaign Style Lock 原样放进每张 Prompt。
6. 如果任务是商品图、详情页图或营销图，先做转化驱动力诊断。
7. 如果用户要求电商详情页、PDP、主图堆栈或整套商品图，默认输出 **5 张主图 + 7-9 张详情页图片** 的图片包。
8. 如果用户要求直接出图，调用 `scripts/generate_image.py`。
9. 返回 Prompt、生成文件路径和关键假设。

---

## 最小输入

任何视觉任务都优先确认这些信息：

- 目标：图片要达成什么效果。
- 用途：商品主图、广告图、社媒图、Banner、PDP 模块、缩略图、概念图等。
- 主体：产品、人物、场景、物体或抽象概念。
- 受众和使用语境。
- 风格：真实摄影、编辑部风格、高级棚拍、UGC、3D 渲染、插画等。
- 构图、比例、平台尺寸。
- 是否需要图片内文字。
- 负面约束：避免 logo、避免文字、避免杂乱、避免医疗承诺等。

如果缺少非关键字段，明确假设后继续，不要无谓阻塞。

---

## 通用图片 Prompt 结构

默认用英文写 Prompt，除非用户要求其他语言。

Prompt 按这个结构组织：

1. Campaign Style Lock，多图任务必填且每张图完全一致。
2. 主体和场景。
3. 图片目的和情绪意图。
4. 构图、镜头和取景。
5. 光线、颜色、材质和纹理。
6. 风格和真实感等级。
7. 平台限制和画幅比例。
8. 图片内文字处理。
9. 负面约束。

Prompt 要足够具体，可以直接执行；也不要过度规定无关细节，避免和用户目标冲突。

---

## 整套图片风格一致性规则

当生成主图 + 详情页、PDP 图片包、广告组图、社媒组图或任何多张图片时，必须先定义一个 **Campaign Style Lock**。这是整套图的视觉合同，不是灵感描述。

### Campaign Style Lock 必填字段

1. **视觉方向**：例如 premium tech ecommerce、clean household care、warm gift editorial。
2. **固定色板**：限制为 2-3 个主色 + 1 个强调色；写清楚背景色、文字色、强调色，不要每张图重新配色。
3. **冷暖调**：明确 warm / cool / neutral，并要求全套一致。
4. **字体系统**：统一为一种字体风格，例如 modern geometric sans-serif；禁止混用衬线、手写、复古、卡通字体。
5. **背景系统**：统一背景材质、空间和深浅，例如 clean light gray studio background 或 deep navy premium tech background。
6. **光线系统**：统一光源方向、阴影强度、反光质感和氛围。
7. **布局系统**：统一留白、圆角、分栏、标签、编号和信息图组件风格。
8. **图标 / 插画系统**：如果用图标，统一线宽、形状、颜色和复杂度。
9. **产品呈现规则**：产品角度、大小比例、材质表现和是否居中必须稳定。
10. **禁止漂移项**：明确禁止 changing color palette, mixed fonts, inconsistent lighting, random backgrounds, mismatched icon styles。

### 默认 Style Lock 模板

如果用户没有给品牌规范，使用保守统一的电商视觉系统：

```text
Campaign Style Lock: consistent premium ecommerce visual system across the entire image set; fixed palette of clean off-white background, deep charcoal text, one product-matched accent color, and one soft secondary accent; neutral-cool studio lighting; modern geometric sans-serif headline placeholders only; consistent rounded rectangular info labels; consistent thin-line icon style; clean high-end product photography mixed with minimal infographic elements; stable product scale and placement; generous whitespace; no color palette changes, no mixed fonts, no random backgrounds, no inconsistent lighting, no mismatched icon styles.
```

### 多图 Prompt 强制规则

- 每张图 Prompt 的第一段必须是同一段 Campaign Style Lock，不能改写、缩短或换同义词。
- 单张图只能改变：画面目的、主体动作、局部构图和短文案。
- 单张图不能改变：色板、冷暖调、字体风格、背景系统、光线系统、图标风格和信息标签样式。
- 如果用户要求重生其中一张图，必须复用原来的 Campaign Style Lock。
- 如果已生成图片风格不一致，优先重写 Prompt 包，而不是逐张随意补描述。

---

## 商品和营销转化流程

商品主图、电商图片、广告图和 PDP 视觉不要从固定模板开始，要先判断转化驱动力。

选择一个主要驱动力：

### A. 视觉驱动型

适用于购买决策依赖外观、风格匹配、光洁度、质感、前后对比或礼品属性的产品。

重点：

- 一眼抓住产品吸引力。
- 质感、细节、工艺和质量信号。
- 使用场景和视觉层级。
- 简短利益点。

### B. 痛点驱动型

适用于买家有明确摩擦、风险、时间损失、不适或反复烦恼的产品。

强制顺序：

1. 痛点挖掘 / 风险触发。
2. 利益 / 解决方案。
3. 信任和证明。
4. 优惠 + CTA。

重点是具体问题、缓解机制、证据和风险逆转。

### C. 情感价值驱动型

适用于购买和身份、信心、归属、地位、关怀、快乐、新奇或冲动相关的产品。

重点：

- 情绪钩子。
- 身份或向往。
- 产品作为实现方式。
- 社交证明和低摩擦行动。

---

## 商品图序列模板

当用户提到“详情页、PDP、Amazon A+、Shopify 商品页、主图堆栈、整套商品图、商品详情图片”时，不要只停留在 5 张主图。必须追加详情页图片序列，并把每一屏都写成可单独生图的 Prompt。

### 视觉驱动主图序列

1. 一眼可懂的视觉主张。
2. 核心功能或质感特写。
3. 使用场景匹配。
4. 普通方案 vs 升级方案对比。
5. 优惠、物流、保障或 CTA 画面。

### 痛点驱动主图序列

1. 问题快照。
2. 解决机制。
3. 利益证明。
4. 信任画面。
5. 优惠 + 紧迫 CTA。

### 情感价值主图序列

1. 情绪场景钩子。
2. 身份 / 价值表达。
3. 产品作为实现方式。
4. 归属、地位或社交信号。
5. 带情绪强化的优惠 + CTA。

---

## 详情页图片序列模板

详情页图片用于移动端纵向浏览，默认每张图独立成屏，尺寸优先使用 `1024x1536` 或平台指定竖版比例。除非用户明确只要文案，否则每个模块都要输出对应图片 Prompt。

### 通用 PDP 详情页图片序列

1. 首屏承接：延续主图卖点，说明产品为谁解决什么问题。
2. 痛点放大：展示用户当前的不便、损失、风险或反复烦恼。
3. 机制解释：用视觉化结构说明产品如何发挥作用，避免虚构无法证明的数据。
4. 核心利益：把 2-4 个主要利益做成易扫读的信息图。
5. 使用步骤：用 3-4 步说明怎么用，降低理解成本。
6. 场景覆盖：展示典型使用场景、适用对象或使用前后状态。
7. 对比选择：普通方案 vs 本产品，突出可观察差异和体验差异。
8. 信任背书：展示材料、包装、质检、保障、真实评价等已有证据；没有证据就写“proof placeholder”，不要编造认证。
9. FAQ / 风险逆转 / CTA：处理残留、适用范围、售后、组合优惠等临门疑虑。

### 驱动力适配

- 视觉驱动型：增加质感细节、尺寸比例、使用场景和礼品感。
- 痛点驱动型：严格按“问题严重性 → 解决机制 → 利益证明 → 信任 → CTA”推进。
- 情感价值驱动型：增加生活方式、身份表达、社交场景和情绪回报。

### 图片内文字规则

- 详情页图片可以有短文案，但必须短、清楚、适合移动端。
- 每屏主标题建议 3-7 个英文词或 6-12 个中文字。
- 说明性文字用 2-4 个短标签，不要生成大段小字。
- 如果模型容易生成乱码，Prompt 中明确要求 “clean layout with short readable headline placeholders, no dense body text”。

---

## 多图生成执行规则

当用户要求直接生成整套电商图片：

1. 先建立 Campaign Style Lock，并写入图片包计划。
2. 再为每张图建立编号、用途、画幅、图片内短文案和独立 Prompt。
3. 主图默认 `1024x1024`；详情页图片默认 `1024x1536`。
4. 每张图使用独立 Prompt 文件，避免一次 Prompt 生成多屏拼图。
5. 每张独立 Prompt 必须以同一段 Campaign Style Lock 开头。
6. 输出目录用产品英文 slug，例如 `generated-images/laundry-detergent-pods-pdp/`。
7. 如果 API 或模型不支持某个尺寸，改用最接近的支持尺寸，并在结果中说明。
8. 如果缺少 `.env` 或生图配置，只输出完整 Prompt 包，不调用脚本。
9. 不要虚构认证、实验数据、评分、销量、真实评价或品牌授权。

---

## 直接生图规则

当用户要求生成图片：

1. 先输出最终 Prompt。
2. 短 Prompt 用 `--prompt`，长 Prompt 用 `--prompt-file`。
3. 根据平台选择 `--size`，没有要求时默认 `1024x1024`。
4. 只有用户指定目录时才使用 `--output-dir`，否则使用 `generated-images/`。
5. 如果缺少 `IMG_API_KEY` 等配置，不要调用脚本；返回 Prompt 和配置命令示例。

命令形状：

```bash
python3 scripts/generate_image.py --prompt "..." --size 1024x1024
```

脚本支持：

- `--prompt`
- `--prompt-file`
- `--output-dir`
- `--size`
- `--quality`
- `--format`
- `--n`

---

## QA 检查

最终输出前确认：

- Prompt 符合用户真实目标。
- 主体、构图、风格和用途明确。
- 商品 / 营销任务包含转化驱动力诊断。
- 证据缺失时不虚构效果、认证或数据。
- 图片内文字短且必要。
- 负面约束覆盖常见失败点。
- 输出和文件里没有 API key 或私密凭据。

---

## 输出格式

Brief / Prompt 模式返回：

1. **Visual Brief**
2. **Final Image Prompt**
3. **Negative Constraints**
4. **Assumptions**

商品或营销任务追加：

1. **Conversion Driver Diagnosis**
2. **Campaign Style Lock**，当任务包含多张图片
3. **Hero Image Sequence**
4. **PDP Detail Image Sequence**，当请求涉及详情页、PDP 或整套商品图
5. **Copy Lines**，如果图片需要文字
6. **Test Priorities**

Generate 模式返回：

1. **Final Image Prompt**
2. **Campaign Style Lock**，多图任务必须返回
3. **Image Pack Plan**，包含每张图的编号、用途、尺寸和短文案
4. **Generated Files**
5. **Assumptions / Notes**
