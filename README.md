# Cross-Border PDP Conversion Strategy Skill

A conversion-first strategy skill for cross-border ecommerce product detail pages (PDP) and hero-image planning.

This skill does **not** generate final images. It diagnoses what actually drives purchase behavior, then produces a structured visual brief + copy strategy that designers, marketers, or image models can execute.

## Why this exists

Most PDP and hero creative misses because teams start from layouts or aesthetics before deciding the persuasion job.

This skill exists to:
- identify the primary conversion mechanism for a product and audience,
- map that mechanism into a clear hero/PDP narrative flow,
- output executable copy and visual direction in English baseline first,
- optionally localize without breaking conversion intent.

## What it does

Given product and market context, the skill delivers:
- conversion driver diagnosis,
- 5-frame hero image plan,
- PDP module structure,
- concise copy lines (headline/subhead/proof/CTA),
- offer + CTA architecture,
- optional localization notes,
- assumptions and test priorities.

Think of it as a **conversion strategy engine** for PDP/hero assets—not an automated image renderer.

## The 3 conversion drivers

### 1) Visual-Driven (Sell with seeing)
Use when decisions depend on look, style fit, finish, texture, or visible transformation.

Focus:
- visual hierarchy and fast comprehension,
- close-up proof of quality/details,
- scenario fit and aesthetic payoff.

### 2) Pain-Driven (Sell with urgency + relief)
Use when buyers face recurring frustration, risk, inefficiency, or loss.

Focus:
- clear pain/consequence framing,
- mechanism of resolution,
- trust proof,
- decisive offer + CTA.

### 3) Emotion-Value-Driven (Sell with identity/aspiration)
Use when buying is tied to confidence, belonging, status, care, or self-expression.

Focus:
- emotional hook,
- identity/value narrative,
- social validation and low-friction action.

## Workflow

1. Collect minimum required inputs.
2. Diagnose one primary conversion driver (optional secondary).
3. Build conversion hypothesis and evidence plan.
4. Produce English (US) baseline strategy + copy.
5. Apply optional localization layer (intent-preserving adaptation).
6. Run conversion QA before finalizing.

## Localization layer (optional)

Localization is an adaptation layer, not a rewrite of strategy.

Principles:
- lock persuasion intent in English baseline first,
- adapt wording, units, and context by market,
- preserve hook/belief-shift/action cue,
- avoid literal translation if it weakens conversion.

## Example input

```text
Product: Self-heating eye mask
Category: Sleep & wellness
Price band: USD 19–29
Audience: Stressed office workers (US + DE markets)
Differentiators: 40-minute heat duration, unscented option, skin-safe material
Proof assets: 4.7★ reviews, dermatology-tested report, 30-day guarantee
Channel: Amazon PDP + main image stack
Current weak points: decent clicks, low add-to-cart
Goal: improve CVR and trust perception
Localization needed: German
```

## Example output shape

```text
1) Conversion Driver Diagnosis
   - Primary: Pain-Driven
   - Why: high recurring discomfort + clear relief mechanism

2) Hero Image Plan (5 Frames)
   - Frame 1: problem snapshot
   - Frame 2: mechanism and relief
   - Frame 3: benefit proof
   - Frame 4: trust signals
   - Frame 5: offer + CTA

3) PDP Structure
   - Problem severity → failed alternatives → solution mechanism
   - Benefit stack → trust stack → offer architecture → CTA close

4) Core Copy Lines (English baseline)
   - Headline / subhead / proof bullets / CTA options

5) Offer + CTA Architecture
   - Bundle logic, risk reversal, urgency style

6) Localization Notes
   - DE adaptation guidance preserving persuasion intent

7) Assumptions + Test Priorities
   - Key unknowns and A/B test sequence
```

> Optional: You may also request an **execution image prompt** for a design or image model workflow. This is a production brief, not final image generation.

## Installation / Usage

### In OpenClaw / Codex
1. Make sure this skill is installed and discoverable by your agent runtime.
2. Trigger with requests like:
   - “Build a conversion strategy for my Amazon PDP hero images.”
   - “Diagnose whether this product should be visual-driven or pain-driven.”
   - “Create English baseline and then localize for Japan.”

### Recommended prompt pattern
Provide:
- product/category/price band,
- audience and purchase context,
- differentiators + proof assets,
- channel constraints,
- current funnel weak points,
- localization target (if needed).

## Limitations

- Does not produce final design files or finished images.
- Output quality depends on input quality (proof assets and clear audience matter).
- Provides strategic copy/brief direction, not guaranteed performance.
- Localization guidance is persuasion-focused; legal/compliance review is still required per market.

## Recommended next steps

After receiving the strategy output:
1. Hand off hero-frame brief to design team or image model workflow.
2. Build 2–3 variant creatives based on primary/secondary hooks.
3. Run structured A/B tests (CTR, add-to-cart, CVR, AOV).
4. Feed performance back into the next strategy iteration.

---

If your goal is “better-looking images only,” this skill may be overkill. If your goal is **higher conversion with clearer persuasion logic**, this is exactly what it is for.
