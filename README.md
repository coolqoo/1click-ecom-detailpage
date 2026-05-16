<div align="center">

**English** | [简体中文](./README_zh.md)

# 🛍️ 1Click Ecom PDP Skill

**Generate high-converting e-commerce main images and Product Detail Pages (PDP) in one click.**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tested On](https://img.shields.io/badge/Tested_on-OpenClaw_|_Hermes_|_Codex_|_Claude_Code-2ea44f?style=for-the-badge&logo=openai&logoColor=white)](#)
[![AI Agent Ready](https://img.shields.io/badge/AI_Agent-Ready-8A2BE2?style=for-the-badge&logo=probot&logoColor=white)](#)

</div>

---

> **1Click Ecom PDP Skill** is an e-commerce image generation tool designed specifically for AI Agents.
> 
> You simply tell it "what product you're selling" and "who the target audience is", and it will automatically write English marketing copy, plan the layout structure, and call AI image generation tools to deliver **a complete set of ready-to-publish product images (Main Images + Detail Page Images)**.

## ✨ Core Features

- **📸 End-to-End One-Click Generation**: Automatically generates 5 main images + 7~9 detail page images (by default) based on simple descriptions, with fully automated delivery.
- **🎨 Visual Consistency Across Images**: Automatically aligns style and product subject to ensure the whole image set has a unified visual identity, eliminating the "patchwork" feel.
- **🎯 Conversion-Driven Copy & Structure**: Built-in blockbuster logic, automatically generating authentic English (US) copy tailored for channels like Amazon.
- **🤖 Broad Framework Compatibility**: Built for Agents, deeply verified on mainstream frameworks like OpenClaw, Hermes, Codex, and Claude Code.

---

## 🖼️ Real-World Showcase

**Your Input (Example):**
![image.png](https://image-b7a.pages.dev/file/1778338782975_image.png)

**Auto-Generated Main Images:**
![image.png](https://image-b7a.pages.dev/file/1778338861993_image.png)

**Auto-Generated Detail Page:**

![image.png](https://image-b7a.pages.dev/file/1778338883692_image.png)

---

## 🚀 Quick Start

Send the following instruction to your AI Agent:

```text
Please install this Skill: `https://github.com/coolqoo/1click-ecom-detailpage`
```

Once installed, configure the image generation model API (see [🔑 API Configuration](#-deployment--configuration) below), and you can drive it directly via natural language.

*(Note: If the API is not configured, the system will only output executable Prompts.)*

**Example Instruction to Agent:**
```text
Use ecom-pdp to create an Amazon US PDP image pack for this product:
Output 5 main images + 8 detail page images.
```

---

## 💻 Deployment & Configuration

<details>
<summary><b>Click to expand manual installation guide</b></summary>

**Requirements:**
- AI Agent with read permissions to the local Skill directory.
- Python 3.10+ (The generation script is pure and relies only on standard libraries).

If your Agent runs in the `~/.codex/skills` directory, you can install it manually from the repository root:

```bash
mkdir -p ~/.codex/skills/ecom-pdp
rsync -a --exclude .git --exclude .env --exclude "generated-images/" ./ ~/.codex/skills/ecom-pdp/
```

**Verify Installation:**
```bash
python3 ~/.codex/skills/ecom-pdp/scripts/generate_image.py --help
```

</details>

### 🔑 API Configuration (Unlock Direct Generation)

To enable **one-click generation** of the image pack, please copy the environment variables file in the project root:

```bash
cp .env.example .env
```

And fill in the compatible service credentials in `.env`:

```dotenv
IMG_BASE_URL=https://api.openai.com/v1
IMG_MODEL=gpt-image-1.5
IMG_API_KEY=your-api-key
```

> **Security Tip**: Please keep your keys safe and never commit `.env` to the repository. The script is also compatible with common environment variables like `OPENAI_API_KEY`.

---

## 💡 Use Cases & Workflow

### 🤖 Zero-Code Natural Language Invocation
Initiate a task conversationally with your AI Agent:

```text
Use ecom-pdp to generate an Amazon US PDP image pack for this portable blender:
Target audience is fitness and commuting crowds, key selling points are 20-second blending, USB-C charging, portable and leak-proof.
Output 5 main images + 8 detail page images, provide Prompts first; if local API configuration is ready, generate images directly.
```

### 🛠️ Advanced Command Line Invocation

<details>
<summary><b>Click to view more advanced usages</b></summary>

**Output Prompt Strategy File Only:**
```bash
python3 scripts/generate_image.py \
  --mode prompt \
  --prompt "premium Amazon main image for a portable blender, clean white background, large product, concise benefit label" \
  --job-dir generated-images/portable-blender-pack-20260509-120000 \
  --asset-type main \
  --size 1024x1024
```

**Generate Automatically from Preset File:**
```bash
python3 scripts/generate_image.py \
  --prompt-file prompts/main-01.txt \
  --job-dir generated-images/portable-blender-pack-20260509-120000 \
  --asset-type main
```

**Generate Consistency Assets (Product Angle Sheet) Based on Reference Image:**
```bash
python3 scripts/generate_image.py \
  --prompt-file prompts/angle-sheet.txt \
  --image product.png \
  --job-dir generated-images/portable-blender-pack-20260509-120000 \
  --asset-type angle-sheet
```

</details>

---

### 🌱 From Product Images to Ad Campaign Cold Start

For many cross-border e-commerce initial tests, the bottleneck isn't "having a product," but rather whether the creatives, pages, and ad costs can be quickly validated. This Skill handles the first half: using natural language to extract product selling points and create main/detail image packs, allowing you to quickly build landing materials for Amazon, standalone sites, or TikTok Shop.

If your next step is running TikTok ads, you might want to check out [ttoh.app](https://ttoh.app). It is an independent TikTok ad offer hub that organizes available ad credits, coupons, and landing page entrances across different countries and regions, such as new account ad credits, Messaging Ads discounts, and TikTok Business Landing Pages for various languages/regions.

In short, this Skill helps you solve "how to create product pages and ad creatives"; [ttoh.app](https://ttoh.app) acts more like an offer index before your cold start, helping you quickly check if there are suitable TikTok ad credits or campaign entrances for your target market. For sellers just starting to test products who want to manage their initial budget carefully, this step can save a lot of searching.

It is not a required dependency for this project; if you only need to generate PDP image packs, this Skill is sufficient. But if you plan to use TikTok traffic to test the product, check [ttoh.app](https://ttoh.app) first for available offers.

---

## ⚙️ Core Engine & Workflow

### 🔄 Intelligent Execution Pipeline
1. **Multi-Level Context Completion**: Automatically fills in missing information by weight (User Input > Attachment Context > Web Research > Logical Inference > Default Assumptions).
2. **Conversion-Driven Insights**: Intelligently analyzes whether the product is Visual-Driven, Pain-Driven, or Emotion-Value-Driven.
3. **Strategy Card Output**: Generates a `Buyer Reason Card` to set the tone for baseline English copy and core CTAs.
4. **Visual Style Lock**: Establishes a global `Campaign Style Lock` to ensure tight consistency across dozens of images.
5. **On-Demand Direct Delivery**: When user instructions are clear and APIs are ready, directly calls internal scripts to render the complete asset pack.

### 🛡️ Smart Compliance Engine
By default, compliance review is **disabled** to maximize creative freedom. If you request "enable compliance/risk review":
- It strictly filters efficacy promises, medical implications, absolute terms, and improper comparisons.
- Forces data, certifications, sales volumes, and user reviews to have legal, verifiable sources.
- When authentic materials are lacking, it replaces review sections with feature breakdowns / FAQs / scenarios.

### 🧠 Proactive Inquiry & Fault Tolerance
When core information (like product itself, core audience, target platform) is missing, the Agent will initiate up to 3-5 core questions. If given authorization like "you decide" or "generate quickly," the system automatically engages **assumptions and inference** to continue the flow, highlighting `Assumptions / Defaults Used` at the end to guarantee a smooth process.

---

## 📦 Output Delivery Specifications

The system structures a clear task directory for each output, facilitating subsequent manual review and A/B testing:

```text
generated-images/<product-slug>-pack-<yyyymmdd-hhmmss>/
  ├── angle-sheet/  # 🛠️ Temporary product angle baseline images (for consistency control)
  ├── main/         # 🖼️ Main image group (1024x1024)
  ├── detail/       # 📜 Detail page long image group (1024x1536)
  ├── prompts/      # 📝 Independent execution Prompts for each asset image
  ├── extras/       # 🎨 Extra variants or fallback images generated by the API
  └── custom/       # 🧪 Temporary debug and custom generated images
```

### 📏 Golden Rules for Image Packs
Whenever "detail page / PDP / main image stack / full set of product images" is mentioned, the Skill defaults to the following delivery model:
- **5 Main Images**: Hero Image (Selling Point) → Mechanism Parsing → Benefit Proof → Scenario Comparison → Offer Guarantee.
- **7-9 Detail Images**: Hero Screen Follow-up → Pain Point Amplification → Mechanism Explanation → Step-by-Step Scenario → Competitor Comparison → Testimonial Endorsement → Risk Reversal (CTA).
- **Independent Prompts** per image, rejecting poor collages, forcing the application of the global Style Lock.

---

## 🎯 Three Major Conversion Drivers

| Driver Mode | Applicable Scenarios | Strategy Focus |
| --- | --- | --- |
| 👁️ **Visual-Driven** | Products with strong appearance, texture, gift appeal, and obvious before/after contrast | Extreme visual claims, texture amplification, scenario matching, scannable benefits |
| ⚡ **Pain-Driven** | Products that solve recurring annoyances, reduce risks, or improve efficiency | Pain point excavation → Mechanism parsing → Benefit proof → Trust endorsement → CTA |
| 💖 **Emotion-Value** | Self-expression, sense of belonging, social status, or impulse buys | Emotional hooks, identity narrative, social signal amplification, low-friction guidance |

---

## ⚠️ Limitations
- **Image Generation Boundaries**: Currently supports text-to-image and single product reference image generation; precise local inpainting based on masks is not yet supported.
- **External API Dependency**: Highly dependent on OpenAI-compatible Images APIs. Image quality, coherence, and processing time depend on your configured underlying model (like DALL·E 3 / Flux) and service provider.
- **Conversion Attribution**: This Skill outputs strategy and creative baselines with high conversion potential. Real commercial returns (CTR/CVR/AOV) are still limited by your product strength, market pricing, and traffic acquisition strategies.

---

## 🙏 Acknowledgments
Thanks to the [linux.do](https://linux.do) community for the support.

---

## 📄 License
This project is open-sourced under the MIT License.

---
<div align="center">
  <p><i>Empowering E-commerce AI Agents with High-Converting Visuals</i></p>
</div>
