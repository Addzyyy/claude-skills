---
name: shared-understanding
description: >
  Trigger this skill whenever you are writing specs, defining requirements,
  kicking off new work, planning a feature, or any time there is a risk of
  misalignment between what was asked and what gets built. Also trigger when
  requirements feel vague, when multiple interpretations of a request are
  possible, when translating business language into technical tasks, when
  starting a conversation that will end in code, or when you notice yourself
  making assumptions about what the user wants. If in doubt, trigger it —
  the cost of a short alignment conversation is always less than the cost
  of rework.
---

# Shared Understanding

> "Shared documents are not shared understanding."
> — Jeff Patton, *User Story Mapping*

## Overview

The most valuable output of any planning session is not the document — it is
the shared understanding that the participants built together through
conversation. Story maps, cards, specs, and backlogs are the *residue* of
good discussions. They are reminders of what was agreed, not substitutes for
the agreement itself.

Two people can read the same spec and build different things. This happens
constantly, and it is the single largest source of preventable rework in
software projects. The antidote is not a better spec. The antidote is a
better conversation *before* anyone starts building.

When working with Claude, you are in a conversation — use it. Do not just
list requirements. Walk through the user journey. Discuss edge cases. Debate
tradeoffs. Challenge your own assumptions out loud. The goal is to reach
alignment on **WHY** before **WHAT**, and on **WHAT** before **HOW**.

### The Core Insight

If you skip the conversation and go straight to building, you are building
on assumptions you have not validated. Every unvalidated assumption is a coin
flip between "it happens to be right" and "expensive rework later."


## When to Use

- **Starting any new feature or project.** Before the first line of code,
  verify that everyone (including you and the AI) agrees on what "done"
  looks like.
- **Writing or reviewing a spec.** A spec is a starting point for
  conversation, not a finished artifact. Read it, then talk through it.
- **Requirements feel vague or hand-wavy.** "Make it user-friendly" is not
  a requirement. It is an invitation to have the conversation that produces
  real requirements.
- **Multiple interpretations are possible.** If you can read a sentence two
  ways, the person who wrote it probably meant a third way.
- **Translating between domains.** Business stakeholders and engineers use
  different mental models. Shared understanding bridges the gap.
- **After a long break or context switch.** Understanding decays. Re-sync
  before resuming work.
- **Any time you catch yourself saying "I assume..."** Stop and verify.


## When NOT to Use

- **Well-understood, mechanical tasks.** If you are fixing a typo or
  bumping a version number, you do not need a discovery conversation.
- **Established patterns with strong conventions.** If the team has built
  the same kind of endpoint 50 times and the pattern is clear, the shared
  understanding already exists.
- **Solo exploration or prototyping.** When you are explicitly spiking to
  learn (not to ship), conversation overhead can slow you down. But
  re-engage this skill before you turn the spike into production code.


## Core Pattern

Shared understanding is built through a repeating cycle:

```
TELL  -->  DISCUSS  -->  CONFIRM  -->  BUILD
  ^                                      |
  |______________________________________|
              (feedback loop)
```

### Step 1: Tell the Story (don't just state requirements)

Bad (documentation-first):
```
Requirements:
- User can reset password
- System sends email with reset link
- Link expires after 24 hours
```

Good (story-first):
```
"Imagine a user who forgot their password on a Friday evening.
They're trying to buy a last-minute gift. They click 'Forgot
password,' get an email, click the link, set a new password,
and finish their purchase. What needs to be true for that to
work smoothly?"
```

The story version surfaces questions that the bullet-point version hides:
How fast does the email arrive? What if it lands in spam? What happens if
they click the link on a different device? What if they remember their
password halfway through — can they abort?

### Step 2: Discuss and Challenge

Ask these questions relentlessly:

- **"What could go wrong?"** — surfaces error cases and edge cases.
- **"What are we assuming?"** — makes implicit assumptions explicit.
- **"Tell me this back in your own words."** — the fastest way to detect
  misalignment.
- **"What would a confused user do here?"** — tests whether the happy path
  is actually happy.
- **"Why this and not that?"** — uncovers the reasoning behind decisions,
  which matters more than the decisions themselves.

### Step 3: Confirm Alignment

Before building, state what you are going to build and why. Be specific
enough that someone could disagree with a concrete detail.

Bad confirmation:
```
"OK, I'll build the password reset feature."
```

Good confirmation:
```
"Here's what I'm going to build:

1. A 'Forgot password' link on the login page that asks for
   an email address.
2. On submit, we send a reset email with a single-use token
   that expires in 1 hour (not 24 — we agreed the security
   risk outweighs the convenience).
3. The reset page lets them set a new password with the same
   validation rules as registration.
4. After resetting, they're automatically logged in and
   redirected to wherever they were trying to go.
5. If the token is expired, we show a message with a link to
   request a new one — no dead ends.

Does this match your understanding?"
```

### Step 4: Build, Then Loop Back

Build in small increments and check back frequently. Shared understanding
is not a one-time event — it is maintained through continuous conversation.

---

### Example: How Shared Understanding Fails

```
Product Manager writes spec:
  "Users should be able to export their data."

Engineer reads spec, builds:
  - CSV export of the user's profile fields

Product Manager expected:
  - Full data export (profile, activity history, uploaded files)
    in a format suitable for GDPR compliance

Result:
  - 2 weeks of rework
  - Missed deadline
  - Frustration on both sides

Root cause:
  - The spec was "shared" but understanding was not
  - Neither party talked through what "their data" meant
  - Neither asked "why does the user want to export?"
```

### Example: How Shared Understanding Succeeds

```
Product Manager says:
  "Users should be able to export their data."

Engineer asks:
  "What's driving this? Is it a GDPR requirement, a user
  request, or something else?"

PM: "GDPR. We need to comply with data portability."

Engineer: "OK, so we need everything we store about them —
  profile, activity logs, uploaded files, payment history.
  Probably JSON or machine-readable format, not CSV.
  Does it need to include data from third-party integrations?"

PM: "Good question — let me check with legal. Also, we need
  it delivered within 30 days per the regulation, but ideally
  same-day."

Engineer: "Same-day for large accounts could be expensive.
  Let me sketch the async approach and we can discuss tradeoffs."

Result:
  - Correct scope on the first build
  - No rework
  - Edge cases (large accounts, third-party data) identified
    before code was written
```

The difference is not talent or documentation quality. The difference is
a 10-minute conversation.


## Quick Reference

| Situation | Action |
|---|---|
| You receive a spec or requirements list | Read it, then **talk through it** — do not treat it as final |
| You are about to start building | State what you will build and why; ask for confirmation |
| A requirement uses vague language ("intuitive," "fast," "flexible") | Ask for a concrete scenario that illustrates what the word means |
| You realize you are making an assumption | Say it out loud and ask if it is correct |
| Someone says "that's not what I meant" | Treat it as a process success, not a failure — you caught it before code |
| You finished a piece of work | Walk through what you built and check it against shared understanding |
| The conversation is going in circles | Write down the two (or more) interpretations explicitly and pick one together |
| You are working with Claude on a feature | Walk through the user journey step by step; do not just provide a bullet list |
| Multiple team members will implement parts | Each person restates their piece and how it connects to the others |


## Common Mistakes

| Mistake | Why It Happens | What to Do Instead |
|---|---|---|
| Treating the spec as the source of truth | Specs feel authoritative and complete | Treat the spec as a conversation starter, not a conversation ender |
| Skipping the "tell it back" step | Feels redundant when you think you understood | Do it anyway — misalignment hides in the gap between "I think I understood" and "I actually understood" |
| Having the conversation but not recording the outcome | The discussion was great but nobody wrote down what was agreed | Capture decisions as lightweight artifacts (cards, notes, updated acceptance criteria) |
| Recording the outcome but losing the reasoning | You wrote WHAT was decided but not WHY | Always capture the "why" — future-you will need to know whether the decision still applies |
| Building first, asking questions later | Pressure to show progress | A 10-minute conversation saves days of rework; "going fast" in the wrong direction is going backwards |
| Assuming silence means agreement | Nobody objected, so it must be fine | Explicitly ask each person to confirm or raise concerns; silence often means confusion or disengagement |
| Over-documenting instead of talking | Writing a 20-page spec feels productive | Long documents create an illusion of thoroughness; prefer short docs + rich conversation |
| One-way communication (presenting, not discussing) | Meetings default to presentation mode | Structure sessions around questions, not slides; the audience should talk more than the presenter |
| Confusing "I said it" with "they heard it" | Saying something out loud feels like communicating it | Communication is only complete when the other party can act correctly on what was said |


## Related Skills

- **[discovery-framing](../discovery-framing/SKILL.md)** — Frame the problem
  space before jumping to solutions. Shared understanding starts with
  agreeing on what problem you are solving.
- **[story-mapping](../story-mapping/SKILL.md)** — The story map is a tool
  for building shared understanding visually. The map is the residue; the
  mapping session is where understanding happens.
- **[persona-framing](../persona-framing/SKILL.md)** — Personas give the
  team a shared vocabulary for talking about users. Without shared
  understanding of *who* you are building for, you cannot align on *what*
  to build.
