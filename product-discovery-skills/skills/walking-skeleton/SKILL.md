---
name: walking-skeleton
description: >
  Use when starting a new project, planning architecture, defining MVP scope,
  deciding what to build first, prioritizing a backlog, or any time someone asks
  "where do we begin?" Build the thinnest possible end-to-end flow before
  adding depth to any single feature. If you are about to build a feature in
  isolation without a working end-to-end path, STOP and apply this skill first.
---

# Walking Skeleton

## Overview

A walking skeleton is the thinnest possible slice through the entire system that
connects every integration point end to end. It is the top row of a story map
brought to life as running, deployable, production-quality code.

The skeleton is not a prototype. It is not throwaway. It is the permanent
scaffolding onto which every future feature is layered. Think of it as the
spine of the product: bare, but structurally complete.

The concept comes from Alistair Cockburn and is central to Jeff Patton's
*User Story Mapping*. The walking skeleton answers one question:

> "Can a user get from start to finish, even if the experience is bare-bones?"

If the answer is no, nothing else matters yet.

### Why it works

- **Integration is the hardest problem.** Connecting components is where most
  projects stall. The skeleton forces you to solve those problems on day one,
  when the cost of change is lowest.
- **It produces a deployable artifact immediately.** You get a real feedback
  loop from real environments before you have invested weeks in isolated
  features.
- **It eliminates "big bang" integration.** Teams that build features in
  silos discover on merge day that nothing fits together. The skeleton makes
  that impossible because the end-to-end path exists from the start.
- **It exposes architectural assumptions early.** You cannot hand-wave the
  data flow between services when you have to make the skeleton walk.

---

## When to Use

- You are starting a new product, service, or major subsystem.
- You are planning architecture and need to validate that the pieces connect.
- You are defining MVP scope and need a principled way to decide what comes
  first.
- A team is debating which feature to build next but has no working
  end-to-end path yet.
- You have a story map and need to decide what the first release looks like.
- You are migrating or rewriting a system and need to prove the new
  architecture works before porting features.

---

## Discovery Brief

**Reads**: Section 3 (Story Map)
**Writes**: Section 4 (Walking Skeleton) of `discovery-brief.md`

If `discovery-brief.md` exists, read it first. The story map tells you which
activities exist — the skeleton is the thinnest path through all of them.

## When NOT to Use

- The end-to-end path already exists and works. At that point you are adding
  flesh to the skeleton -- use **thin-slicing** instead.
- You are doing a small enhancement or bug fix inside an existing, working
  flow.
- The work is a standalone script, utility, or library with no multi-component
  integration to prove out.
- You are in a research spike where the goal is to learn, not to ship. A
  spike can *inform* the skeleton, but the spike itself is not the skeleton.

---

## Core Pattern

### The anti-pattern: building features in isolation

Teams often start by picking the most interesting or best-understood feature
and building it to completion before touching anything else. Each feature is
developed in its own silo. Integration happens "later."

#### Before -- isolated feature development

```
Sprint 1-2:  Build complete search with filters, autocomplete, facets
Sprint 3-4:  Build product detail page with reviews, ratings, Q&A
Sprint 5:    Build cart with saved items, quantity editing
Sprint 6-7:  Build checkout with 3 payment methods, address validation
Sprint 8:    Build order confirmation and email notifications
Sprint 9:    Try to connect everything together  <-- here be dragons
```

What happens at Sprint 9:

- The search results return data in a format the product page does not expect.
- The cart was built assuming a different authentication model than checkout.
- The email service cannot reach the order database.
- "Integration sprint" stretches into three sprints of rework.

#### After -- walking skeleton first

```
Week 1:      Walk the skeleton
             Browse ONE product (hardcoded) ->
             Add to cart ->
             Checkout with ONE payment method ->
             Receive confirmation page
             Deploy it. It works end to end.

Week 2-3:    Layer: real product data, basic search (no filters yet)
Week 4:      Layer: second payment method, order confirmation email
Week 5-6:    Layer: search filters, product reviews
Week 7+:     Layer: autocomplete, saved items, ratings, Q&A, etc.
```

What happens here:

- By the end of week 1, every service talks to every other service.
- Integration bugs surface when there is almost no code to debug.
- Every subsequent feature is added to a system that already works, so you
  can deploy and test continuously.
- If funding is cut at week 4, you still have a working product.

### How to identify your walking skeleton

1. **Start from the story map.** The top row of activities (left to right)
   is the user's journey. The skeleton is one task under each activity --
   the simplest one that still makes the journey complete.

2. **Trace the data.** For each step, ask: "What is the minimum data that
   must flow from here to the next step?" Cut everything else.

3. **Include every integration point.** If the final product will have a
   frontend, an API, a database, and a third-party payment gateway, the
   skeleton must touch all four. Skipping one defeats the purpose.

4. **Keep the UI ugly.** The skeleton does not need styling, responsive
   layouts, or animations. It needs to function.

5. **Keep business logic minimal.** One product, one payment method, one
   user role, one happy path. No edge cases yet.

6. **Deploy it for real.** The skeleton must run in a real environment (at
   minimum staging). If it only works on localhost, you have not proven the
   architecture.

### Another example: internal reporting tool

**Before (isolated):**
```
Module 1:  Build a rich chart library with 8 chart types
Module 2:  Build a data pipeline that cleans and aggregates logs
Module 3:  Build a role-based access control system
Module 4:  Build an export-to-PDF feature
Month 3:   Try to wire chart library to pipeline output
           Discover the pipeline outputs rows, but charts expect
           pre-aggregated time series. Rework pipeline or charts.
```

**After (walking skeleton):**
```
Week 1:    Raw query hits the database ->
           Returns rows ->
           Renders ONE bar chart ->
           Displayed on a page behind basic auth ->
           Deployed to staging
Week 2:    Add a second chart type, begin data pipeline
Week 3:    Pipeline feeds charts instead of raw query
Week 4:    Add export-to-CSV (not PDF yet), add role checks
```

### Another example: mobile app with backend

**Before (isolated):**
```
Team A builds polished onboarding flow (no backend calls)
Team B builds API endpoints (tested with Postman, never with real app)
Team C builds push notification service (standalone)
Month 2: App cannot talk to API (auth token format mismatch)
Month 3: Push notifications require a user ID format the API doesn't use
```

**After (walking skeleton):**
```
Week 1:    App launches ->
           Hits real API for login (email + password, no OAuth yet) ->
           Fetches one piece of data ->
           Displays it on one screen ->
           Receives one push notification ->
           Deployed to TestFlight / internal track
Week 2+:   Layer onboarding, more screens, OAuth, rich notifications
```

---

## Quick Reference

| Step | Action | Key question |
|------|--------|-------------|
| 1 | Identify the user's end-to-end journey | What does "start to finish" mean for this product? |
| 2 | Pick the simplest task at each step | What is the least I can do here and still reach the next step? |
| 3 | List every integration point | Which systems, services, or APIs must connect? |
| 4 | Build the thinnest path through all of them | Can a user (or test) traverse the entire flow? |
| 5 | Deploy to a real environment | Does it work outside localhost? |
| 6 | Prove it walks | Run it end to end. If any step is faked or missing, it is not a skeleton yet. |
| 7 | Layer features onto the skeleton | What is the next thinnest slice that adds real value? |

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|-------------|-----|
| Skipping an integration point | "We'll add the payment gateway later." Now the skeleton does not prove the architecture where it matters most. | Include every boundary, even if the implementation behind it is trivial. |
| Making it too thick | Adding search filters, multiple user roles, or error handling to the skeleton. It stops being thin and fast. | One product, one user, one happy path. Period. |
| Treating it as a prototype | Building the skeleton with the intent to throw it away. This leads to sloppy code that never gets replaced. | The skeleton is production code. It is the foundation everything else is built on. Write it accordingly. |
| Confusing skeleton with MVP | The MVP is a product you ship to real users to test a hypothesis. The skeleton is an engineering milestone that may or may not be user-facing. | The skeleton proves the architecture. The MVP proves the value proposition. They overlap but are not the same. |
| Building features before the skeleton walks | "Let me just finish this one feature first, then I'll connect things." This is how you end up with isolated silos. | Nothing gets depth until the skeleton walks. No exceptions. |
| Not deploying it | The skeleton "works" on a developer's laptop but has never been deployed. Half the integration problems are environment-related. | Deploy the skeleton to at least a staging environment before declaring it done. |
| Goldplating the UI | Spending days on CSS and responsive design for the skeleton. | The skeleton can be ugly. It just has to work. Style it later. |

---

## Related Skills

- **story-mapping** -- The walking skeleton is the top row of the story map
  made real. Build the map first, then identify the skeleton from it.
- **thin-slicing** -- Once the skeleton walks, use thin slicing to add
  incremental depth to each part of the journey.
- **mvp-as-experiment** -- The skeleton proves the architecture; the MVP
  proves the value proposition. The skeleton is often the foundation of the
  MVP, but they serve different purposes.
