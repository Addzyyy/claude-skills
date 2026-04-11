---
name: thin-slicing
description: >
  Trigger when scope is growing beyond what can be delivered — the state where a
  story map or backlog exists but the first release is too thick to ship quickly.
  Also trigger when a story feels "too big," a sprint feels overloaded, stakeholders
  ask for "just one more thing," or the team debates what to include in a release.
  The core message: the only way to build more is to build less. If scope is
  expanding and no one is drawing a cut line, load this skill.
---

# Thin-Slicing

## Overview

Thin-slicing is the discipline of cutting scope to the **thinnest possible shippable increment** that changes real user behavior. It comes from Jeff Patton's *User Story Mapping* and is the single most effective lever for delivering value sooner, generating feedback sooner, and reducing risk.

A thin slice is **not** "the same feature with fewer bells and whistles." It is the smallest thing you can put in front of users that is **usable end-to-end** and lets you learn whether you are on the right track.

The technique is deceptively simple: take a story map (or any scope document) and draw a horizontal line **as high as possible**. Everything above the line is the slice you build now. Everything below the line is deferred -- not deleted, deferred. You are not removing features. You are **sequencing** them so that the first thing you ship generates real feedback that makes every subsequent slice smarter.

If stakeholders look at your thin slice and say "That's it? That feels too small" -- that is exactly how you know you got it right.

### Why it matters

- **Faster feedback.** A thin slice in users' hands in 3 days teaches you more than a thick slice that ships in 3 months.
- **Lower risk.** If the slice is wrong, you wasted days, not quarters.
- **Higher throughput.** Small slices flow through development, review, and deployment without bottlenecks.
- **Better decisions.** Each slice you ship gives you data to decide what the *next* slice should be -- or whether you should stop entirely.

---

## Discovery Brief

**Reads**: Section 3 (Story Map) and Section 4 (Walking Skeleton)
**Writes**: Section 5 (Thin Slices) of `discovery-brief.md`

If `discovery-brief.md` exists, read it first. The story map shows all the work —
your job is to draw the cut line as high as possible.

## When to Use

- You are planning a new feature or product increment.
- A user story feels too large to finish in a single iteration.
- The team is debating what to include in a release or MVP.
- Scope is growing ("Can we also add...?").
- Estimates are high or uncertain -- large scope hides uncertainty.
- Stakeholders are asking for delivery dates and you have no small deliverable to point to.
- You want to validate an assumption before investing further.
- A sprint or cycle is overloaded with work.
- You are prioritizing a backlog and need to decide what comes first.

---

## When NOT to Use

- **Regulatory or compliance features** that must be complete to be legally shippable (e.g., you cannot ship half of GDPR data-deletion). Even here, look for slices within the compliance boundary.
- **Highly coupled infrastructure migrations** where a partial migration leaves the system in a broken state. Prefer a walking-skeleton approach instead.
- **The slice is already thin.** If a story is genuinely small (fits in a day or two of work, delivers end-to-end value), slicing further adds overhead without benefit.
- **Exploratory spikes** where the goal is learning, not shipping. Use time-boxed experiments instead.

---

## Core Pattern

### The Thick-to-Thin Process

1. **Start with the user outcome.** What behavior change are you enabling?
2. **Map the activities.** What does the user do, step by step, to reach that outcome?
3. **Draw the line high.** For each activity, ask: "What is the absolute minimum version of this step that still works end-to-end?"
4. **Validate end-to-end usability.** Walk through the slice as a user. Can you accomplish the outcome, even if crudely? If not, the slice is broken, not thin.
5. **Defer, don't delete.** Everything below the line goes into the next slice, informed by what you learn from the first.
6. **Resist "just one more thing."** Every addition must justify itself against the cost of delayed feedback.

### Before & After Examples

#### Example 1: User Registration

**BEFORE (thick slice):**
```
User Registration Feature
- Email + password signup
- Password strength requirements with real-time feedback
- Email verification with resend capability
- Social login (Google, GitHub, Apple)
- Profile photo upload with cropping
- Username selection with availability check
- Welcome email with onboarding flow
- Two-factor authentication setup
- Account recovery flow
- CAPTCHA to prevent bots
```
Estimated effort: 4-6 weeks. No user feedback until all 10 sub-features are done.

**AFTER (thin slices, sequenced):**

| Slice | What ships | What you learn |
|-------|-----------|----------------|
| **1. Email-only signup** | User enters email, gets a magic link, lands on a blank dashboard. | Do people sign up at all? Where do they try to go next? |
| **2. Password support** | Add password creation as an alternative to magic links. | Do users prefer passwords or magic links? |
| **3. Email verification** | Require email confirmation before accessing paid features. | What percentage of users verify? Where do they drop off? |
| **4. Social login** | Add Google OAuth as one social option. | What fraction of signups switch to social? Is one provider enough? |
| **5. Profile & onboarding** | Photo upload, username, welcome tour. | Now informed by real usage data from slices 1-4. |

Each slice is shippable. Each slice generates feedback. Each subsequent slice is smarter because of that feedback.

#### Example 2: Search Functionality

**BEFORE (thick slice):**
```
Search Feature
- Full-text search across all content types
- Faceted filtering (date, type, author, tags)
- Auto-complete suggestions
- Search result highlighting
- Saved searches
- Search analytics dashboard
- Spell correction / "did you mean?"
- Search within search results
```

**AFTER (thin slices, sequenced):**

| Slice | What ships | What you learn |
|-------|-----------|----------------|
| **1. Basic keyword search** | Single text input, returns top 20 results by relevance, links to items. | What do people actually search for? What terms do they use? |
| **2. Sort and filter by date** | Add a date-range filter and sort toggle. | Do users need recent results or historical ones? |
| **3. Auto-complete** | Suggest terms as the user types, based on real query logs from slice 1. | Now powered by actual user search behavior, not guesses. |
| **4. Faceted filtering** | Add filters based on the most-used search patterns observed. | Which filters get used? Which are ignored? |

Notice how slice 3 is *better* because it was built after slice 1 generated real query data.

#### Example 3: Reporting Dashboard

**BEFORE (thick slice):**
```
Analytics Dashboard
- 12 chart types (bar, line, pie, scatter, etc.)
- Custom date ranges
- CSV/PDF export
- Scheduled email reports
- Role-based dashboard views
- Real-time data refresh
- Drag-and-drop dashboard builder
```

**AFTER (thin slices, sequenced):**

| Slice | What ships | What you learn |
|-------|-----------|----------------|
| **1. One key metric, one chart** | Show the single most important number (e.g., weekly active users) as a line chart with a 30-day default view. | Is this the metric people actually care about? Do they need different time ranges? |
| **2. CSV export** | Add a "Download CSV" button for the raw data behind the chart. | Do people export? What do they do with the data? (This tells you what charts to build next.) |
| **3. Three more charts** | Add the next 3 most-requested metrics, informed by export analysis and user requests. | Now driven by evidence, not assumptions. |

---

## Quick Reference

| Principle | How to apply it |
|-----------|----------------|
| **A thin slice changes user behavior** | If users cannot do something new with your slice, it is not a slice -- it is a component. Ship behavior changes, not components. |
| **End-to-end usability is non-negotiable** | A slice must work from the user's entry point to a meaningful outcome. A back-end API without a UI is not a slice (unless your users are developers consuming the API). |
| **Draw the line high** | On a story map, move the release line up until it feels uncomfortable. Then move it up one more row. |
| **Defer, don't delete** | Everything below the line is "later," not "never." This makes stakeholders more willing to accept thin slices. |
| **Feedback is the product** | The primary output of a thin slice is not the feature -- it is the learning. Design slices to maximize what you learn. |
| **Sequence by risk, not by preference** | The first slice should address the biggest uncertainty. Build the thing you are least sure about first. |
| **Time-box, don't scope-box** | If you cannot slice thin enough, time-box: "We will build as much of this as we can in 3 days and ship whatever is usable." |
| **One slice at a time** | Finish, ship, and learn from one slice before starting the next. Parallel slices defeat the purpose. |

---

## Common Mistakes

| Mistake | Why it is wrong | What to do instead |
|---------|----------------|-------------------|
| **Slicing by architecture layer** | "Back-end first, then front-end" is not thin-slicing. Neither layer is usable alone. | Slice vertically: each slice touches every layer needed to deliver an end-to-end user experience. |
| **Slicing by component** | "Build the search index first, then the UI" leaves you with no shippable increment. | Each slice must be independently usable by a real user. |
| **Adding "just one more thing"** | "While we're in there, let's also add..." is how thin slices become thick. Every addition delays feedback. | Ask: "Can we ship without this?" If yes, it goes below the line. |
| **Confusing thin with incomplete** | A thin slice is not a broken feature. It is a complete feature with a narrow scope. | Verify end-to-end usability. If a user cannot accomplish a goal, the slice is incomplete, not thin. |
| **Slicing too thin** | If the slice delivers no meaningful behavior change, it is not worth the deployment overhead. | The slice must change at least one user behavior or answer at least one open question. |
| **Treating all slices as equal priority** | Doing easy slices first feels productive but wastes the learning opportunity. | Sequence slices by uncertainty. The first slice should test your riskiest assumption. |
| **Never shipping the lower slices** | Deferring becomes permanent if you do not revisit the backlog after each slice ships. | After each slice, review what is below the line. Reprioritize based on what you learned. Some items will move up; others will be dropped entirely. |
| **Gold-plating the first slice** | Polishing the thin slice until it is thick again. "Users will judge us by this first impression." | Users judge you more harshly for shipping nothing for months than for shipping something simple this week. |

---

## Related Skills

- **[story-mapping](../story-mapping/SKILL.md)** -- Thin-slicing works on top of a story map. Build the map first, then draw the line.
- **[walking-skeleton](../walking-skeleton/SKILL.md)** -- A walking skeleton is the thinnest possible slice of the entire system architecture. Use it as your first slice.
- **[mvp-as-experiment](../mvp-as-experiment/SKILL.md)** -- An MVP is a thin slice designed specifically to test a hypothesis. Thin-slicing is the technique; MVP-as-experiment is the mindset.
- **[release-planning](../release-planning/SKILL.md)** -- Release planning sequences multiple thin slices into a coherent delivery timeline.
- **[now-later-never](../now-later-never/SKILL.md)** -- Use now/later/never to decide what goes above the line (now), below the line (later), or off the map entirely (never).
