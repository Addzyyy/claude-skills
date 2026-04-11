---
name: mvp-as-experiment
description: >
  Trigger when thin slices exist and the team needs to frame the first release as
  a learning experiment, not "phase 1 of everything" — the state where you know
  what to build first but haven't defined what you're trying to learn from it.
  Also trigger when anyone mentions "MVP", "minimum viable product", "v1 scope",
  "validate an idea", "proof of concept", or "how do we know this will work."
  This skill reframes the MVP as the smallest thing you can build to test your
  riskiest assumption, not a feature-reduced product.
---

# MVP as Experiment

## Overview

An MVP is **not** "version 1 with fewer features."
An MVP is the **smallest thing you can build to learn whether you are solving the right problem.**

The word "product" in "Minimum Viable Product" is misleading. It makes teams think the goal is to ship something usable. The real goal is to **test a hypothesis as cheaply as possible** and decide what to do next based on evidence.

Every MVP should answer one question:

> **"What is the cheapest way to learn if this idea works?"**

If you are not embarrassed by your MVP, you spent too long building it.

---

## Discovery Brief

**Reads**: Section 5 (Thin Slices) and Section 2 (Personas)
**Writes**: Section 6 (MVP Experiment) of `discovery-brief.md`

If `discovery-brief.md` exists, read it first. The thin slice tells you what
you're building — this skill frames it as an experiment to learn from.

## When to Use

- You have an idea but no evidence that real users want it.
- The team is debating which features belong in "v1."
- Someone says "let's just build a simple version and see."
- You are about to invest weeks of engineering effort on an unvalidated assumption.
- Stakeholders are asking for a roadmap but you haven't confirmed the problem exists.
- You are choosing between multiple possible solutions and need data to decide.
- A feature request sounds reasonable but nobody has talked to users about it.

## When NOT to Use

- The problem and solution are already validated (you have real usage data). Move to thin-slicing and incremental delivery instead.
- You are building for regulatory or compliance requirements where the need is not in question.
- The "experiment" would take longer than just building the real thing (e.g., a simple config change).
- You are in execution mode on a validated backlog — use walking-skeleton or thin-slicing.
- The team is calling a fully scoped release "an MVP" to avoid commitment. That is not an experiment; that is a small waterfall.

---

## Core Pattern

### Step 1: Write the Hypothesis

Before building anything, state what you believe and how you will test it.

Use this template:

```
We believe [target users]
have [this problem / unmet need].

We will test this by building [specific MVP].

We will know we are right if [metric]
reaches [threshold] within [timeframe].
```

If you cannot fill in every field, you are not ready to build. Go talk to users first.

### Step 2: Choose the Cheapest Experiment Type

Pick the experiment type that gives you the answer with the **least effort**:

| Experiment Type | What It Is | Effort | Best For |
|---|---|---|---|
| **Landing page test** | A page describing the product that does not exist yet. Measure sign-ups or clicks. | Hours | Demand validation ("do people want this?") |
| **Wizard of Oz** | The user sees a working product, but a human is doing the work behind the scenes. | Days | Feasibility + desirability testing |
| **Concierge** | You manually deliver the service to a handful of users, one-on-one. | Days | Understanding the workflow before automating |
| **Single-feature prototype** | Build exactly one feature — the riskiest assumption — and ship it. | Days–1 week | Solution validation ("does this approach work?") |
| **A/B test** | Show two variants to real users and measure which performs better. | Days | Optimization of an existing flow |
| **Paper prototype / clickable mockup** | Screens that look real but have no backend. Walk users through them. | Hours | Usability and comprehension testing |
| **Data / log analysis** | Analyze existing product data to validate or invalidate the assumption. | Hours | When the signal might already exist |

**Rule of thumb:** Start at the top of this table. Only move down if the cheaper option genuinely cannot answer your question.

### Step 3: Build It (and Nothing More)

- Timebox the build. If the experiment takes more than **one week** to build, you are over-engineering it.
- Do **not** add error handling, analytics infrastructure, internationalization, or "nice-to-haves." This is a throwaway.
- Hardcode things. Use spreadsheets as databases. Deploy to a personal Heroku instance. Cut every corner that does not invalidate the experiment.
- If you are not uncomfortable with the quality, you spent too long.

### Step 4: Measure, Learn, Decide

After the experiment runs for the agreed timeframe, look at the results and pick one of three paths:

```
┌─────────────────────────────────────────────┐
│            EXPERIMENT RESULTS               │
├─────────────────────────────────────────────┤
│                                             │
│   Metrics met threshold?                    │
│                                             │
│   YES ──────► PERSEVERE                     │
│               Invest in building the real   │
│               thing. Use thin-slicing and   │
│               walking-skeleton to deliver   │
│               incrementally.                │
│                                             │
│   CLOSE BUT UNCLEAR ──► PIVOT               │
│               The problem is real but the   │
│               solution is wrong. Reframe    │
│               the hypothesis and run a new  │
│               experiment.                   │
│                                             │
│   NO / NO ENGAGEMENT ──► KILL               │
│               Stop. Do not build this.      │
│               Move on to the next highest-  │
│               value hypothesis.             │
│                                             │
└─────────────────────────────────────────────┘
```

**Killing an idea is a successful experiment.** You learned something and saved weeks or months of wasted effort.

---

### Example: MVP Experiment Card

Here is a concrete example of a filled-in experiment card.

```
╔══════════════════════════════════════════════════════════════╗
║  MVP EXPERIMENT CARD                                        ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  HYPOTHESIS                                                  ║
║  We believe freelance designers                              ║
║  struggle to find fair-priced stock photography.             ║
║                                                              ║
║  EXPERIMENT                                                  ║
║  Type: Landing page test                                     ║
║  Build: A single landing page describing a curated,          ║
║         designer-focused stock photo subscription at         ║
║         $9/month. Include an email sign-up form.             ║
║  Traffic source: Post in 3 designer Slack communities        ║
║                  and 2 subreddits.                            ║
║  Timeframe: 2 weeks                                          ║
║  Build effort: 4 hours                                       ║
║                                                              ║
║  SUCCESS CRITERIA                                            ║
║  - 200+ unique visitors                                      ║
║  - 5% or higher email sign-up rate (>= 10 sign-ups)         ║
║  - At least 3 sign-ups reply to a follow-up survey           ║
║                                                              ║
║  DECISION FRAMEWORK                                          ║
║  >= 5% sign-up rate ──────────► Persevere.                   ║
║     Run concierge MVP: manually curate 50 photos/week        ║
║     for the first 10 subscribers to test retention.           ║
║                                                              ║
║  2-5% sign-up rate ──────────► Pivot.                        ║
║     Interest exists but positioning is off. Interview         ║
║     sign-ups to learn what they actually need.                ║
║                                                              ║
║  < 2% sign-up rate ──────────► Kill.                         ║
║     Demand is insufficient. Archive and move on.             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### Example: Wizard of Oz Experiment

```
╔══════════════════════════════════════════════════════════════╗
║  MVP EXPERIMENT CARD                                        ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  HYPOTHESIS                                                  ║
║  We believe mid-size e-commerce teams                        ║
║  want AI-generated product descriptions from a bullet-       ║
║  point input.                                                ║
║                                                              ║
║  EXPERIMENT                                                  ║
║  Type: Wizard of Oz                                          ║
║  Build: A simple form where users paste bullet points        ║
║         and receive polished product descriptions within     ║
║         2 hours via email. Behind the scenes, a team         ║
║         member writes them manually.                         ║
║  Recruit: DM 20 Shopify store owners from a forum.           ║
║  Timeframe: 1 week                                           ║
║  Build effort: 1 day (form + email template)                 ║
║                                                              ║
║  SUCCESS CRITERIA                                            ║
║  - 8+ of 20 contacted users try the tool                     ║
║  - 50%+ of those users submit a second request               ║
║  - 3+ users ask "how much does this cost?" (buying intent)   ║
║                                                              ║
║  DECISION FRAMEWORK                                          ║
║  Criteria met ──────────► Persevere.                         ║
║     Build single-feature prototype with real AI backend.     ║
║                                                              ║
║  Users try it once but don't return ──► Pivot.               ║
║     Quality or turnaround time may be wrong. Interview.      ║
║                                                              ║
║  Few users try it ──────────► Kill.                          ║
║     Problem is not painful enough to act on.                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Quick Reference

| Question | Answer |
|---|---|
| What is an MVP? | The smallest experiment that tests your riskiest assumption. |
| What is an MVP NOT? | A stripped-down product you intend to ship and iterate on. |
| How long should it take to build? | Hours to days. One week maximum. If it takes longer, you are building too much. |
| What should it test? | One hypothesis. One assumption. Not "will users like the product." |
| Who sees it? | A small, targeted group — not "everyone." |
| What happens after? | Measure results. Decide: persevere, pivot, or kill. |
| Should I write clean code? | No. Most MVPs are throwaway. Optimize for speed of learning. |
| What if stakeholders want more polish? | Explain that polish costs time, and time spent polishing is time not spent learning. The goal is evidence, not impressiveness. |
| What if the MVP succeeds? | Throw it away and build the real thing properly, using walking-skeleton and thin-slicing. Do not ship the experiment. |
| How do I pick success criteria? | Ask: "What number would make us confident enough to invest real engineering time?" Set the bar there. |

---

## Common Mistakes

| Mistake | Why It Hurts | What to Do Instead |
|---|---|---|
| Treating the MVP as the foundation of the real product | You over-engineer the experiment, spend weeks instead of days, and lose the courage to throw it away. | Decide up front: this is disposable. Write it in a separate repo or branch you plan to delete. |
| No hypothesis — "let's just see what happens" | Without a hypothesis, you cannot interpret the results. Any data will feel ambiguous. | Write the hypothesis and success criteria before writing a single line of code. |
| Success criteria set after the experiment | Confirmation bias kicks in. You will find a way to declare victory regardless. | Lock criteria before launch. Share them with the team so nobody moves the goalposts. |
| Building multiple features to "be fair to the idea" | Every added feature increases cost and muddies the signal. You will not know which feature drove the result. | Test one thing. One feature. One assumption. |
| Running the experiment too long | If you let it run indefinitely, you will never kill it. Sunk cost takes over. | Set the timeframe in advance. When it ends, decide. No extensions. |
| Skipping the "kill" option | Teams treat "kill" as failure. So they always pivot, even when the evidence says stop. | Normalize killing ideas. Celebrate what you learned. A killed experiment saves months of wasted work. |
| Making the MVP too polished | If users love it, you will feel pressure to ship the experiment as-is. Now you have tech debt as your foundation. | Keep it rough. If it succeeds, build the real version from scratch with proper architecture. |
| Not talking to users before or after | The MVP gives you quantitative signal. You still need qualitative understanding of why. | Interview users before (to form the hypothesis) and after (to interpret the data). |

---

## Related Skills

- **thin-slicing** — After an MVP validates the idea, use thin slicing to deliver the real product in small, valuable increments.
- **outcome-over-output** — MVPs are outcome-driven by definition. Use outcome-over-output to keep the team focused on results, not features shipped.
- **walking-skeleton** — When you move from experiment to real product, walking-skeleton gives you the architectural approach to build incrementally end-to-end.
- **now-later-never** — Use now-later-never to prioritize which hypotheses to test first and which to defer or discard.
