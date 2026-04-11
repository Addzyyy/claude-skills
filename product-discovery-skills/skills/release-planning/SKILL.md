---
name: release-planning
description: >
  Trigger when thin slices exist and you need to sequence them into shippable releases —
  the state where the story map has been sliced but there's no release timeline or
  milestone structure yet. Also trigger when roadmapping, deciding what goes into
  v1/v2/v3, discussing milestones, or when you see a prioritized list that lacks
  release boundaries. This skill sequences delivery into themed increments where each
  release tells a story: "after this release, users can ___."
---

# Release Planning

## Overview

Release planning is the practice of slicing a story map horizontally into shippable increments.
Each horizontal slice represents a release — a version of the product that real users can use
end-to-end. The key insight from Jeff Patton's "User Story Mapping" is that a release is NOT a
collection of half-built features. It is a thin, complete pass across the activities in the map
that delivers a coherent experience.

The story map's left-to-right axis shows the user's journey (activities and tasks). Release
planning adds a top-to-bottom axis: what we build first (top) vs. what we build later (bottom).
Drawing a horizontal line across the map creates a release boundary. Everything above the line
ships in this release. Everything below the line ships later.

This is fundamentally different from a prioritized backlog. A backlog is a vertical list. A
release slice is a horizontal cut that guarantees breadth — every critical activity is
represented, even if only in its simplest form.

## Discovery Brief

**Reads**: Section 3 (Story Map) and Section 5 (Thin Slices)
**Writes**: Section 7 (Release Plan) of `discovery-brief.md`

If `discovery-brief.md` exists, read it first. The story map and thin slices
provide the raw material — this skill sequences them into themed releases.

## When to Use

- You have a story map and need to decide what to ship first.
- The team is planning what goes into v1, v2, or v3.
- Someone asks "What's in the next release?" or "When will feature X ship?"
- You are roadmapping across multiple quarters or milestones.
- Sprint planning feels disconnected from the bigger picture.
- A stakeholder wants to know what the MVP looks like.
- The backlog has grown large and needs release boundaries.
- You need to communicate a delivery plan visually.
- The team is debating scope and needs a framework for the conversation.

## When NOT to Use

- You don't have a story map yet. Build the map first (see: `story-mapping`).
- You are breaking down a single story into smaller pieces. That is `thin-slicing`.
- You are deciding whether to build something at all. That is `now-later-never`.
- You are designing the walking skeleton from scratch. Start with `walking-skeleton`, then
  come back here to plan what goes above and below the line.
- You are deep in implementation details for a single sprint's work.

## Core Pattern

### Step 1: Establish the story map

Before you can slice, you need the map. The top row is **activities** (big things users do).
Below each activity are **tasks** (the steps within that activity), ordered top-to-bottom by
priority or necessity.

### Step 2: Draw the first line — Release 1 (The Walking Skeleton)

Draw a horizontal line across the entire map. Everything above this line is Release 1. This
release must:

- Include at least one task under every essential activity.
- Be usable end-to-end, even if minimal.
- Have a clear theme or goal stated in one sentence.
- Be the smallest thing that makes the product actually useful to a real user.

Release 1 is the walking skeleton. It proves the system works across the full journey. It is
NOT a prototype or demo — it is real, shippable software.

### Step 3: Draw the second line — Release 2

Below the first line, draw a second. Everything between the two lines is Release 2. This
release:

- Adds depth to activities that were too thin in Release 1.
- May add breadth by including optional activities that were omitted from Release 1.
- Is informed by feedback from Release 1 users.
- Has its own theme or goal.

### Step 4: Identify Release 3 (but hold it loosely)

You may sketch a third release, but do not plan in detail beyond that. Releases 3+ will
change based on what you learn from Releases 1 and 2.

### Step 5: Validate each slice

For every release slice, ask:

1. **Is it complete?** Can a user accomplish their goal end-to-end?
2. **Is it coherent?** Does it have a clear theme, or is it a grab-bag?
3. **Is it small enough?** If it takes more than a few weeks, it is probably too big.
4. **Are there gaps?** Is any essential activity completely missing from this slice?
5. **Is it learnable?** Will shipping this teach us something that changes the next slice?

---

### Concrete Example: Online Marketplace

Here is a story map for an online marketplace, sliced into three releases.

**Activities (left to right across the map):**

```
BROWSE CATALOG  |  SEARCH & FILTER  |  VIEW PRODUCT  |  ADD TO CART  |  CHECKOUT  |  TRACK ORDER
```

**Full task breakdown under each activity:**

```
BROWSE CATALOG    SEARCH & FILTER    VIEW PRODUCT     ADD TO CART      CHECKOUT         TRACK ORDER
--------------    ---------------    ------------     -----------      --------         -----------
See categories    Keyword search     See name/price   Add item         Enter address    See order status
See product list  Filter by price    See photos       Change qty       Choose shipping  Get email updates
See featured      Filter by category See description  Remove item      Enter payment    See delivery date
Pagination        Sort results       See reviews      Save for later   Apply coupon     Contact support
Infinite scroll   Autocomplete       See related      View cart page   Order summary    Return/refund
                  Saved searches     360-degree view   Wish list       Guest checkout   Rate the seller
                  Search history     Size guide                        Saved payment
```

#### Release 1 — "Users can complete a basic purchase"

**Theme:** A user can find a product, add it to a cart, and buy it. The core loop works.

**Line drawn above row 3 in most columns:**

```
BROWSE CATALOG    SEARCH & FILTER    VIEW PRODUCT     ADD TO CART      CHECKOUT         TRACK ORDER
--------------    ---------------    ------------     -----------      --------         -----------
See categories    Keyword search     See name/price   Add item         Enter address    See order status
See product list                     See photos       Change qty       Enter payment
                                     See description  Remove item      Order summary
─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ RELEASE 1 LINE ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
```

Notice:
- **SEARCH & FILTER** has only keyword search. No filters, no sorting. Enough to find things.
- **TRACK ORDER** has only order status. No email updates yet. But it IS present — the user
  is not left wondering "did my order go through?"
- Every activity is represented. The journey is complete, even if thin.
- No activity is deep. This is a walking skeleton.

#### Release 2 — "Users can find what they want efficiently"

**Theme:** Search and discovery become powerful. Informed by Release 1 feedback showing users
struggled to find products.

```
See featured      Filter by price    See reviews      Save for later   Choose shipping  Get email updates
Pagination        Filter by category See related      View cart page   Apply coupon     See delivery date
                  Sort results
─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ RELEASE 2 LINE ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
```

Notice:
- **SEARCH & FILTER** gets much deeper — three new tasks. This was the pain point from Release 1.
- **VIEW PRODUCT** adds reviews and related products — depth that helps conversion.
- **CHECKOUT** adds shipping options and coupons — responding to user requests.
- **TRACK ORDER** adds email updates and delivery dates — reducing support tickets.
- This is not just "more stuff." It has a theme: findability and confidence.

#### Release 3 — "Power users and repeat buyers" (held loosely)

**Theme:** Retention and efficiency for returning users.

```
Infinite scroll   Autocomplete       360-degree view  Wish list        Guest checkout   Contact support
                  Saved searches     Size guide                        Saved payment    Return/refund
                  Search history                                                        Rate the seller
─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ RELEASE 3 LINE ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
```

Notice:
- This release is sketched, not committed. By the time Release 2 ships, user feedback may
  completely rearrange these priorities.
- The theme is about repeat buyers — wish lists, saved payments, search history.
- Some tasks may get cut entirely. "360-degree view" might never be worth the investment.

---

### What makes this different from a prioritized backlog?

A prioritized backlog might put "Keyword search," "Filter by price," "Filter by category,"
and "Sort results" as items 1-4 because search is the top priority. That gives you an amazing
search experience... for a product you can't buy (because checkout wasn't built yet).

Release planning on a story map forces you to go wide first, then deep. Release 1 touches
every activity. No user is left stranded mid-journey.

## Quick Reference

| Principle | Do This | Not This |
|---|---|---|
| Slice direction | Horizontal across the map | Vertical (one feature deep) |
| Release 1 | Walking skeleton — thin but complete | The "most important feature" built fully |
| Release scope | End-to-end user journey | A collection of unrelated stories |
| Release theme | One sentence goal ("Users can X") | A long list of features |
| Number of releases planned | 2-3 at most | A 12-month detailed roadmap |
| What's above the line | What ships in THIS release | Everything we'd like to have |
| What's below the line | What ships LATER (or never) | Things we forgot about |
| Planning horizon | Detailed for next release only | Equally detailed for all releases |
| Gaps in a slice | A red flag — every activity needs coverage | Acceptable if "that feature isn't ready" |
| Feedback loops | Each release informs the next | All releases planned up front, never revised |
| Slice size | Small enough to ship in weeks | So large it takes months with no feedback |
| Stakeholder communication | "Release 1 lets users do X" | "We'll ship 47 stories by March" |

## Common Mistakes

| Mistake | Why It Hurts | Fix |
|---|---|---|
| Building one feature completely before starting the next | Users get a deep experience in one area but can't complete their journey | Slice horizontally — go wide first, then deep |
| Release 1 is too big | It takes months, you get no feedback, and half of it was wrong | Cut until it hurts. If it's usable, ship it |
| Release 1 is missing an essential activity | Users hit a dead end mid-journey | Check every activity column — each must have at least one task above the line |
| Planning 5+ releases in detail | You're guessing. Releases 4 and 5 will look nothing like this | Plan 2-3 releases. Sketch anything beyond that |
| No theme for the release | The release is a grab-bag of unrelated improvements | State the goal in one sentence. If you can't, the release lacks focus |
| Treating the release plan as fixed | You ignore what users tell you after Release 1 | Revise the plan after every release based on real feedback |
| Confusing a release with a sprint | Sprints are execution units; releases are value units | A release may span multiple sprints. Plan releases first, then break into sprints |
| Every task at the same priority | You can't draw a meaningful line if nothing is ranked | Force-rank tasks within each activity column before slicing |
| Skipping the story map | You try to do release planning on a flat backlog | Build the map first. You can't slice what you haven't mapped |
| Release is a wish list, not a plan | 200 stories "in" a release means nothing is really planned | If a release has more stories than a team can ship in a few weeks, it's too big |

## Related Skills

- **story-mapping** — Build the map before you slice it. Release planning without a story map is just backlog ordering.
- **thin-slicing** — How to break individual stories into smaller pieces within a release slice.
- **walking-skeleton** — The pattern for Release 1. The thinnest possible end-to-end slice.
- **now-later-never** — A complementary prioritization technique for deciding what makes it onto the map at all.
