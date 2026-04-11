---
name: rock-breaking
description: >
  Decompose epics, large features, and vague stories into smaller, independently
  valuable user stories without losing the narrative thread. Use this skill whenever
  work feels too big, too vague, or too hard to estimate — during backlog grooming,
  story refinement, sprint planning, epic breakdown, estimation discussions, or any
  time someone says "this story is huge" or "where do we even start?"
---

# Rock Breaking: Decomposing Stories Without Losing the Narrative

## Overview

Big stories are like rocks. You need to break them down to ship them, but **how**
you break them matters enormously.

Most teams instinctively split stories along technical boundaries — frontend,
backend, database. This feels logical but produces pieces that cannot be
demonstrated to a user independently. You end up with a backend that has no UI
and a frontend that has no data. Neither is shippable. Neither tells a story.

The right way to break a rock is to split it so that **every piece still
contains all the layers needed to deliver user value**. Think of it like cutting
a cake: don't slice horizontally (just frosting, then just sponge, then just
filling). Slice vertically so that every piece has frosting, sponge, and filling.
Every slice is a complete experience, just a smaller one.

This idea comes from Jeff Patton's *User Story Mapping*: stories are
placeholders for conversations about user needs, and when you split them, each
piece must still represent a conversation worth having with a user.

## When to Use

- An epic or feature feels too big to estimate or fit in a sprint
- A story has been sitting in the backlog for weeks because nobody knows where to start
- Estimation discussions produce wildly different numbers (a sign the scope is unclear)
- Backlog grooming or refinement sessions
- Sprint planning when a story won't fit
- Any time someone says "we need to break this down"
- When a story has more than 3-4 acceptance criteria (it's probably multiple stories)
- When the team can't agree on what "done" means for a story
- Release planning where you need to sequence delivery of a large feature

## When NOT to Use

- The story is already small, clear, and independently demonstrable
- You're splitting a story that's already been estimated at 1-3 points
- The work is genuinely atomic (e.g., "change button color from blue to green")
- You're in discovery mode and don't yet understand the problem space — use
  `discovery-framing` first to understand what you're building before
  decomposing how to build it
- The team needs to see the big picture first — use `story-mapping` to lay out
  the whole narrative before breaking individual rocks

## Core Pattern

### The Anti-Pattern: Horizontal (Technical Layer) Splitting

Splitting by technical layer creates stories that cannot be demonstrated to users.

**Before — a big rock:**

```
EPIC: User Payment System
"As a customer, I want to pay for my order so I can receive my purchase."
```

**Bad split — horizontal slices by technical layer:**

```
Story 1: Set up payment database tables and models
Story 2: Build payment processing API endpoints
Story 3: Create payment form UI components
Story 4: Integrate Stripe SDK on the backend
Story 5: Connect frontend to backend payment API
Story 6: Add payment confirmation email service
```

Why this is wrong:
- Story 1 (database tables) cannot be demonstrated to any user
- Story 3 (UI components) has no backend — you can't actually pay
- Story 5 is pure integration glue — it produces nothing new
- None of these are independently shippable
- A stakeholder cannot look at story 2 and understand what user value it delivers
- If you ship stories 1-3 and the project gets paused, you have delivered zero value

### The Pattern: Vertical (User Behavior) Splitting

Split so each piece delivers a thin but complete path through all layers.

**Good split — vertical slices by user behavior:**

```
Story 1: Customer pays for an order with a credit card (happy path)
  → Includes: minimal UI form, one API endpoint, one DB table, Stripe call,
    confirmation page. No email yet. Only Visa. No error handling.

Story 2: Customer sees clear error messages when payment fails
  → Includes: card declined, expired card, network timeout — UI, API,
    and error logging for each.

Story 3: Customer pays with PayPal as an alternative
  → Includes: PayPal button on UI, PayPal API integration, DB storage.

Story 4: Customer receives email confirmation after successful payment
  → Includes: email template, sending service, delivery tracking.

Story 5: Customer can view past payment history
  → Includes: history UI, query endpoint, date filtering.
```

Why this is right:
- Story 1 alone lets a real user pay with a real card and see confirmation
- Story 2 alone improves the experience for users whose payments fail
- Each story can be demoed to a stakeholder in a review
- If the project gets paused after story 1, you have a working payment system
- Each story is independently estimable because the scope is clear

### Second Example

**Before — a big rock:**

```
EPIC: Admin Dashboard
"As an admin, I want a dashboard to manage all aspects of the platform."
```

**Bad split — by UI section:**

```
Story 1: Build the dashboard layout and navigation sidebar
Story 2: Create the user management data grid
Story 3: Build the analytics charts backend
Story 4: Design the settings page UI
Story 5: Implement role-based access control
```

Problems: Story 1 is a shell with no functionality. Story 3 has no UI.
Story 5 is cross-cutting infrastructure that doesn't map to a user need on its own.

**Good split — by user behavior / workflow:**

```
Story 1: Admin can view a list of all registered users and search by name
  → Full vertical slice: page, API, query, search box.

Story 2: Admin can disable a user account (with confirmation dialog)
  → Includes the action button, confirmation UX, API call, and DB update.

Story 3: Admin can see a chart of signups over the last 30 days
  → Includes chart component, data aggregation endpoint, and date query.

Story 4: Admin can update platform settings (site name, support email)
  → Settings form, save endpoint, validation, success feedback.

Story 5: Admin can invite a new team member by email with a specific role
  → Invite form, role picker, email sending, pending invite state.
```

Each of these can be built, tested, demoed, and shipped independently.

## Splitting Strategies: Quick Reference

| # | Strategy | Split by... | Example |
|---|----------|------------|---------|
| 1 | **Workflow step** | Sequential steps in a user's journey | Registration -> Login -> Profile setup -> Settings (each is a story) |
| 2 | **Data variation** | Different inputs or data types the system handles | Pay by credit card -> then PayPal -> then crypto -> then bank transfer |
| 3 | **Business rule** | Rules that add complexity incrementally | Basic price calc -> add tax rules -> add discount codes -> add bulk pricing |
| 4 | **User role** | Different personas interacting with the feature | Admin manages users -> regular user manages own profile -> guest views public info |
| 5 | **Happy path vs. edge case** | Optimistic path first, then failures and exceptions | Successful upload -> then handle file-too-large -> then handle wrong format -> then retry on network failure |
| 6 | **CRUD operations** | Create, Read, Update, Delete as separate stories | Create a report -> View report list -> Edit a report -> Archive a report |
| 7 | **Performance / scale** | Start with "it works" then optimize | Search returns results -> then add pagination -> then add caching -> then add full-text indexing |
| 8 | **Platform / channel** | Different surfaces where the feature appears | Feature works on web -> then mobile web -> then native iOS -> then native Android |

### How to Choose a Strategy

1. Ask: "What is the simplest version of this that a user could actually use?"
   That is your first story (usually the happy path).
2. Ask: "What are the most common variations?" Each variation is a candidate story.
3. Ask: "Can each piece be demoed?" If not, combine pieces or re-split.

## The Demo Test

**Every story that comes out of a split must pass this test:**

> "Can I put this in front of a user (or stakeholder) and show them something
> that works, end to end, even if it's small?"

If the answer is no, the story is split wrong. Regroup and try a different
splitting strategy.

Examples that **fail** the demo test:
- "Set up the database schema" — nothing to show a user
- "Write unit tests for the payment module" — valuable work but not a user story
- "Refactor the API layer" — no visible change for users
- "Build the frontend components" — components without data are empty shells

These are valid **tasks** (things developers do), but they are not **stories**
(things that deliver user value). They belong inside a story, not as standalone items.

## Common Mistakes

| Mistake | Why it happens | What to do instead |
|---------|---------------|-------------------|
| Splitting by technical layer | It matches how developers think about architecture | Split by user behavior — every slice crosses all layers |
| Creating stories that need other stories to be useful | Dependencies feel unavoidable for complex features | Each story must deliver standalone value — if it can't, it's not a story yet |
| Splitting too small | Over-correcting from "too big" | If a story takes less than half a day, it's probably a task, not a story — merge it back |
| Splitting too uniformly | Treating all stories as the same size | Some stories are naturally larger — split the big ones, leave the small ones alone |
| Losing the narrative | After splitting, nobody remembers the overall goal | Keep the epic visible as a container — use `story-mapping` to maintain the big picture |
| Confusing tasks with stories | "Research payment providers" sounds like a story | Stories deliver user-facing value. Research, spikes, and setup are tasks within stories or separate investigation timeboxes |
| Splitting before understanding | Breaking down work that isn't well understood yet | Use `discovery-framing` first. You can't split a rock you haven't examined |
| Making every story the same pattern | Always using CRUD or always using workflow steps | Match the splitting strategy to the nature of the feature. Try multiple strategies and pick the one that produces the most independently valuable pieces |

## Worked Example: Applying Multiple Strategies

Starting rock:

```
EPIC: Notification System
"As a user, I want to receive notifications about important events
so I don't miss anything."
```

**Round 1 — Split by workflow step:**

```
Story A: User receives in-app notifications for new messages
Story B: User can view notification history
Story C: User can mark notifications as read
Story D: User can configure notification preferences
```

**Round 2 — Story A is still large. Split by data variation:**

```
Story A1: User receives in-app notification when they get a direct message
Story A2: User receives in-app notification when someone comments on their post
Story A3: User receives in-app notification when they are mentioned
```

**Round 3 — Story D is still large. Split by business rule:**

```
Story D1: User can turn notifications on/off globally
Story D2: User can choose which event types trigger notifications
Story D3: User can set quiet hours (no notifications between 10pm-8am)
```

Now every story is small, clear, independently demonstrable, and still
connected to the original epic's narrative.

## Checklist Before You're Done Splitting

- [ ] Can each story be demoed to a user or stakeholder?
- [ ] Does each story deliver value on its own, without depending on another story from this split?
- [ ] Is each story small enough to complete in a single sprint (ideally 1-3 days)?
- [ ] Does each story still connect to the original epic's user goal?
- [ ] Are there no "infrastructure only" stories that lack user-facing value?
- [ ] Can the team estimate each story with reasonable confidence?
- [ ] If the project were paused after any single story, would something useful have been delivered?

## Related Skills

- **story-mapping** — Lay out the full user journey before breaking individual stories. Story mapping gives you the big picture; rock-breaking gives you the small pieces.
- **thin-slicing** — Closely related. Thin-slicing focuses on finding the thinnest possible end-to-end slice; rock-breaking focuses on the strategies for decomposing larger chunks. Use them together.
- **release-planning** — After breaking rocks, use release-planning to sequence the pieces into coherent releases that deliver incremental value to users.
