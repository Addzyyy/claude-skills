---
name: now-later-never
description: >
  Trigger when the backlog has more items than capacity and no one is saying "no" —
  the state where everything is "high priority" and nothing has been explicitly killed.
  Also trigger when scope creep is happening, when someone says "can we also add,"
  "wouldn't it be nice if," or "let's put it on the backlog." The core message: a
  backlog is not a plan — if you cannot say NEVER to anything, you are saying yes to
  everything, and yes to everything is a strategy for delivering nothing well. This
  skill forces explicit NEVER decisions, not just prioritization.
---

# Now / Later / Never

## Overview

Now/Later/Never is an explicit prioritization technique from Jeff Patton's *User Story Mapping*. Every feature, story, or idea gets placed into exactly one of three buckets:

- **NOW** -- we are building this in the current release or iteration.
- **LATER** -- we are deliberately deferring this to a future release, and we know *why*.
- **NEVER** -- we are not doing this. It is out of scope for this product.

The most valuable bucket is **NEVER**.

Every time you say NEVER to a feature, you permanently remove it from the team's cognitive load. You stop estimating it, stop discussing it, stop feeling guilty about it. You free attention and energy for the things that actually matter.

Teams resist the NEVER conversation because it feels harsh -- like killing someone's idea. So instead of saying NEVER, they say LATER. The item sits in the backlog for months, untouched, gathering dust, silently consuming mental overhead every time someone scrolls past it. A backlog of 200 stories is not a plan. It is a guilt list. It is a graveyard of good intentions that actively harms the team's ability to focus.

The discipline of Now/Later/Never forces the conversation that teams avoid: **what are we deliberately choosing NOT to do?** That conversation is more important than deciding what to build, because focus is not about what you add -- it is about what you remove.

### Why it matters

- **Focus.** Fewer things done well beat many things done poorly. Every NEVER sharpens the product.
- **Honesty.** Calling something NEVER is more respectful than letting it rot as LATER. The person who requested it deserves a clear answer.
- **Backlog health.** A small, curated backlog is a planning tool. A massive, ungroomed backlog is a liability.
- **Speed.** Every item you remove from consideration is time you do not spend estimating, discussing, or re-prioritizing it.
- **Morale.** Teams drowning in an infinite backlog feel like they are always behind. Pruning the backlog makes progress visible.

---

## When to Use

- You have just built a story map and need to decide what goes into the first release.
- The backlog has grown beyond what the team can reason about (a good threshold: if you cannot read every item in 10 minutes, it is too big).
- A stakeholder or customer submits a feature request.
- Someone in a meeting says "can we also add..." or "wouldn't it be nice if..."
- You are grooming or refining the backlog.
- Scope creep is happening -- more items are entering the backlog than leaving it.
- The team feels overwhelmed by the volume of planned work.
- LATER items have been sitting untouched for more than one planning cycle.
- You are planning a release and need to draw the line between what is in and what is out.

---

## When NOT to Use

- **You are in a divergent brainstorming phase.** During ideation (e.g., story mapping, design sprints), the goal is to generate ideas freely. Premature NEVER kills creativity. Categorize *after* the brainstorming is done.
- **You do not have enough context to decide.** If the team has not yet validated the problem space, forcing NOW/LATER/NEVER on solutions is premature. Do discovery first.
- **The decision is not yours to make.** If a regulatory body or contractual obligation requires a feature, it is not a candidate for NEVER. It is NOW or LATER, and you negotiate timing, not existence.
- **The item is already in progress.** Stopping mid-build has its own costs. Use this technique at planning boundaries, not mid-sprint.

---

## Core Pattern

### The Now/Later/Never Process

1. **Lay out the candidates.** Gather the full list of features, stories, or ideas -- ideally from a story map, but a flat backlog works too.
2. **Start with NEVER.** Go through the list and ask: "If we never built this, would the product still succeed?" If yes, mark it NEVER. This is the hardest step and the most important one.
3. **Separate NOW from LATER.** For everything that survived, ask: "Does this need to be in the next release to achieve our outcome?" If yes, it is NOW. If not, it is LATER.
4. **Challenge every LATER.** For each LATER item, ask: "Why later? What would have to change for this to become NOW?" If you cannot answer that question, it is probably NEVER.
5. **Thin-slice the NOWs.** For each NOW item, ask: "What is the thinnest version we can ship?" (See the thin-slicing skill.)
6. **Communicate the NEVERs.** Tell stakeholders what was cut and why. Reframe as "out of scope for this product" or "not this version" if NEVER feels too final.
7. **Schedule regular reviews.** Every 2-4 weeks, review the LATER list. If an item has been LATER for 3+ months with no movement toward NOW, it is NEVER.

### Example: E-Commerce Product Launch

A team is building an online store. After story mapping, they have 34 features. Here is how the categorization conversation goes:

**NOW (this release -- 8 items):**

| Feature | Reasoning |
|---------|-----------|
| Product catalog with search | Cannot sell without browsable products. |
| Shopping cart | Core purchase flow. |
| Checkout with credit card | Minimum viable payment. Must ship to generate revenue. |
| Order confirmation email | Users need proof of purchase. Legal requirement in some jurisdictions. |
| Basic inventory tracking | Must prevent overselling. |
| Mobile-responsive layout | 60% of target users are on mobile (validated in research). |
| Admin: add/edit products | Store owner must be able to manage catalog without developer help. |
| Admin: view orders | Store owner must be able to fulfill orders. |

**LATER (next release -- 6 items):**

| Feature | Reasoning | What would make it NOW? |
|---------|-----------|------------------------|
| Wishlist | Nice for engagement, but not required for first purchase. | If conversion data shows users browse but do not buy, a wishlist could help. |
| Discount codes | Sales driver, but store needs baseline sales data first. | After 30 days of sales data to measure impact. |
| PayPal support | Some users prefer it, but credit card covers the majority. | If checkout abandonment data shows payment method as a drop-off reason. |
| Product reviews | Social proof helps, but needs a base of purchases first. | After 50+ orders -- no reviews to show before then anyway. |
| Order tracking page | Users can check email for now. | If support tickets about "where's my order?" exceed 10/week. |
| Multi-language support | Target market is English-only at launch. | If international traffic exceeds 15% of total. |

**NEVER (20 items, including):**

| Feature | Reasoning |
|---------|-----------|
| Social login (Google/Facebook) | Email + password is fine. Social login adds complexity and privacy concerns for marginal convenience. |
| Loyalty points program | We are a small store, not a rewards platform. This is a different product. |
| In-app chat with support | Email support is sufficient at our scale. Chat requires staffing we do not have. |
| AI-powered product recommendations | Requires significant data we do not have yet and ML infrastructure we cannot maintain. If we ever need this, we buy it, not build it. |
| Subscription/recurring orders | Our products are not consumables. No evidence of repeat-purchase behavior to justify this. |
| Augmented reality "try it on" | Cool idea, wrong product. We sell electronics, not clothing. |
| Cryptocurrency payments | Fewer than 1% of our target market would use this. Not worth the integration cost. |
| Multi-vendor marketplace | We are one store, not a marketplace. This is a different business model entirely. |
| Gamification (badges, streaks) | We are a store, not a game. This does not serve the core job-to-be-done. |
| Built-in blog/CMS | Use a separate blogging tool. Do not build a CMS inside an e-commerce app. |

Notice: 20 out of 34 features were NEVER. That is not unusual. That is healthy. The team went from 34 features to 8 for launch. That is focus.

### Example: Backlog Triage

A team has a backlog of 147 items. Many have been there for 6+ months. The product owner runs a Now/Later/Never session:

```
Before:
  147 backlog items
  Average age: 4.2 months
  Items older than 6 months: 63
  Items with no activity in 90 days: 89

After Now/Later/Never triage:
  NOW:   12 items (current sprint + next sprint)
  LATER: 28 items (with documented triggers for promotion to NOW)
  NEVER: 107 items (archived with brief rationale)

Result:
  Backlog reduced from 147 to 40 active items.
  Planning meetings shortened from 90 minutes to 30.
  Team reported feeling "lighter" and "more focused."
```

The key insight: **107 items were NEVER.** They had been silently living as LATER, consuming attention in every grooming session, making the real priorities harder to see.

### The "LATER Audit" Checklist

For every item marked LATER, write down:

1. **Why not NOW?** (What is missing -- data, dependency, capacity?)
2. **What trigger promotes it to NOW?** (A specific metric, event, or customer signal.)
3. **Review date.** (When will you re-evaluate? Default: 4 weeks.)

If you cannot fill in all three fields, the item is NEVER. Be honest about it.

---

## Quick Reference

| Principle | How to apply it |
|-----------|----------------|
| **Start with NEVER** | It is easier to move a NEVER to LATER than to demote a LATER to NEVER. Begin by removing scope, then add back only what is justified. |
| **NEVER is not "never ever"** | NEVER means "not this product / not this version / not with current evidence." If conditions change dramatically, you can revisit. But the default is out. |
| **LATER needs a trigger** | Every LATER item must have a documented condition that would promote it to NOW. "We might want this someday" is not a trigger -- it is a wish. |
| **NOW needs a constraint** | Everything in NOW should be thin-sliced. Ask: "What is the thinnest version of this we can ship?" (See thin-slicing.) |
| **A big backlog is a symptom** | If your backlog keeps growing, you are not saying NEVER enough. The backlog should stay roughly constant: items enter, items leave (as NOW or NEVER). |
| **NEVER is a gift** | Every NEVER gives the team back time, attention, and energy. Celebrate NEVERs as much as you celebrate shipped features. |
| **Review LATER regularly** | Any LATER item untouched for 3 months is a NEVER in disguise. Demote it. |
| **Communicate NEVER with empathy** | Do not say "that's a bad idea." Say "that's out of scope for this product" or "we're choosing not to do this so we can focus on X." |
| **The ratio matters** | In a healthy prioritization session, at least 50% of candidates should be NEVER. If you are not cutting that aggressively, you are not focusing. |

---

## Common Mistakes

| Mistake | Why it is wrong | What to do instead |
|---------|----------------|-------------------|
| **Using LATER as a polite NEVER** | Items pile up in LATER with no intention of ever building them. The backlog grows. Grooming sessions become painful. | Be honest. If you cannot articulate a trigger that promotes it to NOW, call it NEVER. |
| **Avoiding NEVER to spare feelings** | Stakeholders feel heard because their idea is "on the backlog." But it will never be built, and they will eventually realize that. A delayed no is worse than an immediate no. | Say NEVER early and explain why. "We're choosing to focus on X because it serves our outcome of Y. This feature doesn't contribute to Y." |
| **Treating the backlog as a promise** | Every item in the backlog feels like a commitment. A 200-item backlog feels like 200 promises. That is unsustainable. | The backlog is a menu of options, not a list of promises. Items can and should be removed. |
| **Categorizing without conversation** | The product owner quietly assigns NOW/LATER/NEVER without team input. The team has no shared understanding of *why*. | Do the categorization as a group exercise. Walk through each item. Let people argue. The conversation is more valuable than the categories. |
| **Making NOW too big** | Everything feels important, so NOW has 30 items. That is not prioritization -- it is capitulation. | NOW should be small enough to finish in one release cycle. If it is not, you have not made real choices yet. |
| **Never reviewing LATER** | LATER items sit untouched for months. Nobody looks at them. They become stale. | Schedule a LATER review every 2-4 weeks. Promote, demote, or kill each item. |
| **Treating NEVER as permanent and irreversible** | Teams resist NEVER because it feels absolute. "What if we need it later?" | Reframe: NEVER means "not with current evidence." Archive the item with a rationale. If the world changes, you can revisit. But the default is out. |
| **Skipping the NEVER conversation entirely** | The team only debates NOW vs. LATER. Nothing ever leaves the backlog. | Explicitly force the question: "What are we choosing NOT to do?" Make NEVER a required output of every prioritization session. |

---

## Related Skills

- **[thin-slicing](../thin-slicing/SKILL.md)** -- Once you mark something NOW, thin-slice it to the smallest shippable increment. Now/Later/Never decides *what* to build; thin-slicing decides *how much* to build first.
- **[release-planning](../release-planning/SKILL.md)** -- Release planning sequences the NOW items into a coherent delivery plan. Now/Later/Never feeds into release planning by defining the boundary of each release.
- **[story-mapping](../story-mapping/SKILL.md)** -- Story mapping gives you the full picture of user activities and tasks. Now/Later/Never is the prioritization pass you do *after* the map is built -- walking each column and asking "is this NOW, LATER, or NEVER?"
- **[outcome-over-output](../outcome-over-output/SKILL.md)** -- The reason you say NEVER is that the feature does not serve the target outcome. Outcome-over-output gives you the lens for making that judgment.
