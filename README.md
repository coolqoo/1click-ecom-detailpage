# Ecom PDP Skill

> Turn raw product inputs into a conversion-first ecommerce PDP image system — strategy, English copy, image sequences, executable prompts, and optional direct image generation.

<p align="center">
  <strong>Built for AI agents that ship product pages, not pretty moodboards.</strong>
</p>

<p align="center">
  <img alt="Skill" src="https://img.shields.io/badge/AI%20Skill-ecom--pdp-111827?style=for-the-badge">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Dependencies" src="https://img.shields.io/badge/Dependencies-stdlib%20only-10B981?style=for-the-badge">
  <img alt="Images API" src="https://img.shields.io/badge/Images%20API-OpenAI--compatible-7C3AED?style=for-the-badge">
</p>

<p align="center">
  <img alt="Tested on OpenClaw" src="https://img.shields.io/badge/Tested%20on-OpenClaw-0F172A?style=flat-square">
  <img alt="Tested on Hermes" src="https://img.shields.io/badge/Tested%20on-Hermes-0F172A?style=flat-square">
  <img alt="Tested on Codex" src="https://img.shields.io/badge/Tested%20on-Codex-0F172A?style=flat-square">
  <img alt="Tested on Claude Code" src="https://img.shields.io/badge/Tested%20on-Claude%20Code-0F172A?style=flat-square">
</p>

---

## What This Is

**Ecom PDP Skill** is a cross-border ecommerce conversion skill for AI agents.

It helps an agent decide **why a product should sell first**, then turns that diagnosis into:

- English (US) baseline copy
- buyer reason cards
- Amazon / Shopify / TikTok Shop PDP image structures
- hero image stacks
- detail-page image sequences
- short in-image copy
- executable AI image prompts
- optional direct image generation through an OpenAI-compatible Images API

The core idea is simple:

> Pretty images are not enough. Every image must have a job in the conversion path.

---

## Best For

- Amazon listings
- Shopify product detail pages
- TikTok Shop product pages
- Amazon A+ content
- ecommerce hero image stacks
- product ad creatives
- offer / CTA image systems
- PDP conversion audits
- cross-border English copy and localization

It can handle general visual prompts, but its strongest use case is **conversion-first ecommerce product imagery**.

---

## Tested Agent Runtime

This skill is designed to be portable across modern AI coding / agent environments.

| Runtime | Status | Notes |
|---|---:|---|
| OpenClaw | ✅ Tested | Native skill-style workflow |
| Hermes | ✅ Tested | Works as a local agent skill package |
| Codex | ✅ Tested | Works under `~/.codex/skills` |
| Claude Code | ✅ Tested | Works when the skill directory is readable |

The bundled image script only uses the Python standard library, so the runtime mainly needs file access and Python 3.10+.

---

## Install

Ask your AI agent to install this skill:

```text
Please install this skill: https://github.com/coolqoo/1click-ecom-detailpage
```

If your agent uses a local skill directory such as `~/.codex/skills`, you can install it manually from the repository root:

```bash
mkdir -p ~/.codex/skills/ecom-pdp
rsync -a --exclude .git --exclude .env --exclude "generated-images/" ./ ~/.codex/skills/ecom-pdp/
```

Verify the image helper:

```bash
python3 ~/.codex/skills/ecom-pdp/scripts/generate_image.py --help
```

---

## Quick Start

After installation, talk to your agent naturally:

```text
Use ecom-pdp to build an Amazon US PDP image pack for this product.
Output 5 hero images + 8 detail-page images.
Start with prompts. If the local image API is configured, generate the images directly.
```

A stronger input looks like this:

```text
Use ecom-pdp for a portable blender.
Market: Amazon US.
Audience: gym users and commuters.
Key claims: 20-second blending, USB-C charging, leak-resistant design.
Need: 5 main images + 8 PDP detail images.
Output English copy, image sequence, and executable prompts.
```

---

## How It Thinks

The skill starts with **Conversion Driver Diagnosis**.

It classifies the product into one primary selling logic:

### 1. Visual-Driven

For products that sell through appearance, texture, style, giftability, aesthetic upgrade, or obvious before/after contrast.

Focus:

- visual desire
- premium feel
- styling context
- quick benefit scanning

### 2. Pain-Driven

For products that solve repeated frustration, risk, inefficiency, time loss, discomfort, or daily friction.

Focus:

- pain recognition
- mechanism clarity
- proof and trust
- risk reversal
- CTA momentum

### 3. Emotion-Value-Driven

For products that sell identity, self-care, novelty, belonging, social signal, or impulse desire.

Focus:

- emotional hook
- identity bridge
- social meaning
- low-friction purchase motivation

The output is then built around that conversion driver. Decorative sections get removed. Conversion blocks stay.

---

## Core Workflow

1. Resolve the minimum product inputs.
2. Diagnose the primary conversion driver.
3. Build a Buyer Reason Card.
4. Write the English (US) baseline.
5. Define offer, trust, CTA, and risk-reversal logic.
6. Create a Campaign Style Lock for visual consistency.
7. Plan the hero image stack.
8. Plan the PDP detail image sequence.
9. Write short in-image copy first.
10. Generate independent executable prompts for each image.
11. Optionally call the bundled image script.
12. Self-review the pack for conversion clarity.

---

## Minimum Inputs

The skill works best when you provide:

- product name and category
- target market and language
- sales channel: Amazon, Shopify, TikTok Shop, etc.
- audience segment
- price band
- top differentiators
- proof assets: certifications, test results, reviews, warranty, press, etc.
- offer assets: discount, bundle, free shipping, guarantee, bonus
- current funnel problem: CTR, CVR, add-to-cart, trust, AOV, return concern
- output mode: strategy, prompts, image pack, or direct generation

If details are missing, the skill resolves information in this order:

1. user-provided input / attachments / context
2. follow-up questions
3. public web research
4. logical inference
5. explicit assumptions / defaults

When assumptions are used, the final output should say so.

---

## Output Shape

Typical strategy / prompt output includes:

1. Missing Info Questions, only when truly blocking
2. Conversion Driver Diagnosis
3. Buyer Reason Card
4. English Baseline
5. Localization Notes, if needed
6. Offer + CTA Architecture
7. Campaign Style Lock
8. Hero Image Sequence
9. PDP Detail Image Sequence
10. Image Prompts
11. Assumptions / Defaults Used
12. Test Priorities
13. Self-review Scorecard

Generate mode additionally returns generated file paths.

---

## Example Output Skeleton

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

---

## Image API Configuration

Direct image generation is optional.

Create a local `.env` file in the project root:

```dotenv
IMG_BASE_URL=https://api.openai.com/v1
IMG_MODEL=gpt-image-1.5
IMG_API_KEY=your-api-key
```

Compatible aliases are also supported:

- `OPENAI_BASE_URL`
- `OPENAI_API_BASE`
- `OPENAI_IMAGE_MODEL`
- `OPENAI_MODEL`
- `OPENAI_API_KEY`

Keep real API keys local. Do not commit `.env`.

---

## Image Script Usage

Generate from a direct prompt:

```bash
python3 scripts/generate_image.py \
  --prompt "premium Amazon main image for a portable blender, clean white background, large product, concise benefit label" \
  --job-dir generated-images/portable-blender-pack-20260509-120000 \
  --asset-type main \
  --size 1024x1024
```

Generate from a prompt file:

```bash
python3 scripts/generate_image.py \
  --prompt-file prompts/detail-01.txt \
  --job-dir generated-images/portable-blender-pack-20260509-120000 \
  --asset-type detail \
  --size 1024x1536
```

Use a product reference image:

```bash
python3 scripts/generate_image.py \
  --prompt-file prompts/angle-sheet.txt \
  --image product.png \
  --job-dir generated-images/portable-blender-pack-20260509-120000 \
  --asset-type angle-sheet \
  --size 1024x1024
```

Force prompt-only mode:

```bash
python3 scripts/generate_image.py \
  --mode prompt \
  --prompt "clean product hero image, premium studio lighting, white background" \
  --job-dir generated-images/product-pack-20260509-010946 \
  --asset-type main
```

Force image mode:

```bash
python3 scripts/generate_image.py \
  --mode image \
  --prompt-file prompt.txt \
  --job-dir generated-images/product-pack-20260509-010946 \
  --asset-type main \
  --size 1024x1024 \
  --quality high \
  --format png \
  --n 1
```

Use a custom `.env` path:

```bash
python3 scripts/generate_image.py --env-file .env --prompt-file prompt.txt
```

Supported options:

- `--prompt`
- `--prompt-file`
- `--mode`
- `--job-dir`
- `--asset-type`
- `--output-dir`
- `--env-file`
- `--size`
- `--quality`
- `--format`
- `--n`
- `--image`

---

## Output Directory Convention

Each complete image pack should use one unique job directory:

```text
generated-images/<product-slug>-pack-<yyyymmdd-hhmmss>/
  angle-sheet/  temporary product identity reference images
  main/         hero / main images
  detail/       PDP detail-page images
  prompts/      prompt files for each image
  extras/       extra returned variants
  custom/       one-off tests or custom images
```

Use `--job-dir` to point at the task root and `--asset-type` to route outputs:

- `angle-sheet`
- `main`
- `detail`
- `extras`
- `custom`

---

## Default Image Pack Rules

When the user asks for a PDP, detail page, Amazon A+, Shopify product page, product image stack, or full ecommerce image pack, the default output is:

- **5 hero / main images**
  - first-image selling proposition
  - mechanism / function
  - benefit proof
  - comparison or lifestyle scene
  - offer / guarantee

- **7-9 PDP detail images**
  - opening bridge
  - pain or desire amplification
  - mechanism explanation
  - core benefits
  - usage steps
  - scenario coverage
  - comparison / why choose this
  - review or recommendation frame
  - trust / FAQ / risk reversal / CTA

Default sizes:

- main images: `1024x1024`
- detail images: `1024x1536`

Each image gets its own prompt. Do not cram a whole long landing page into one generated image.

---

## Product Reference Flow

For physical products with a reference image, use a temporary **Product Angle Sheet** first.

The angle sheet should capture:

- front view
- left 45-degree view
- right 45-degree view
- side thickness
- back or key structural view
- ports, buttons, LEDs, or important details
- product + packaging combination
- usage angle, if relevant

The angle sheet is only an identity reference. It should not include prices, badges, ratings, CTAs, discounts, or final marketing copy.

Formal image prompts should reference it only like this:

```text
Use the product angle sheet only as product identity reference.
```

---

## Default Campaign Style Lock

```text
Campaign Style Lock: consistent premium cross-border ecommerce visual system across the entire image set; fixed palette of clean off-white background, deep charcoal text, one product-matched accent color, and one soft secondary accent; neutral-cool studio lighting; modern geometric sans-serif headline placeholders only; consistent rounded rectangular info labels; consistent thin-line icon style; clean high-end product photography mixed with minimal infographic elements; stable product scale and placement; generous whitespace; fixed color palette, single font system, stable backgrounds, consistent lighting, matched icon styles.
```

---

## Compliance Behavior

Compliance is ignored by default unless the user explicitly asks for:

- compliance review
- platform compliance
- ad compliance
- category risk review
- Amazon / TikTok / Meta policy checking

Even when compliance mode is off, factual claims such as certifications, test data, sales volume, official endorsements, and brand authorization must come from user-provided or verifiable sources.

Review / testimonial handling:

- If compliance is on: only use real reviews, real recommendation themes, or user-provided testimonial assets.
- If compliance is off: simulated review-style copy can be used, but it must be marked as an assumption.

---

## Recommended Workflow

1. Give the agent product details, channel, market, and reference images.
2. Ask for the Buyer Reason Card and English baseline first.
3. Review the offer, CTA, proof, and trust logic.
4. Generate the full image sequence and prompts.
5. Configure `IMG_*` variables if direct generation is needed.
6. Generate images.
7. A/B test 2-3 core hooks by CTR, add-to-cart, CVR, and AOV.

---

## Limitations

- Supports text-to-image and single reference-image workflows.
- Local mask / inpainting workflows are not included yet.
- Requires an OpenAI-compatible Images API for direct generation.
- Provider support for `size`, `quality`, `format`, and `n` may vary.
- Output quality, speed, and cost depend on the selected model and provider.
- The skill provides conversion strategy and production prompts; actual performance still depends on product, offer, traffic source, price, and testing discipline.

---

## License

Use it, adapt it, and make better product pages.
