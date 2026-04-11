---
name: persona-framing
description: >
  Trigger when user types have been identified but not yet deepened into full personas
  — typically after discovery-framing, or whenever stories use generic labels like
  "as a user" or "as a customer." Also trigger when starting any new project or feature
  and no one has specified WHICH user benefits and why, when building empathy maps or
  user profiles, or when reviewing stories that lack a named persona with a clear goal.
  The state that triggers this skill: we know roughly who the users are, but we haven't
  given them names, goals, context, and pain points yet.
---

# Persona Framing

## Overview

"The user" does not exist. There is no single, generic user whose needs you
can design for. There are specific people with specific goals, specific
contexts, and specific frustrations. When you say "the user," you are
designing for no one.

Persona framing, drawn from Jeff Patton's *User Story Mapping*, is the
practice of grounding every product decision in a concrete, named user type.
Not a demographic profile. Not a marketing segment. A **behavioral
archetype** — a person defined by what they are trying to accomplish, the
context they work in, and the pain that gets in their way.

The purpose is not to create elaborate character sheets. The purpose is to
force specificity. When a user story says "As a user, I want to search," it
is vague and unfalsifiable. When it says "As Priya, a new hire who joined
last week, I want to find the company holiday calendar without asking my
manager," it tells you exactly what to build, how to prioritize, and how to
test whether you succeeded.

### Why it matters

- **Different users need the same feature for different reasons.** A power
  user and a first-time user both "need" search — but the power user needs
  speed and filters, while the first-timer needs guidance and forgiveness.
  Building for "the user" forces you to compromise for everyone and optimize
  for no one.
- **Personas drive prioritization.** If you know this release is for Priya
  (the new hire), you can defer features that only matter to Marcus (the IT
  admin). Without personas, every feature seems equally important.
- **"As a user" is a red flag.** It signals that no one has asked who
  specifically will benefit and why. It produces stories that are technically
  correct and practically useless.
- **Personas make trade-offs explicit.** When two needs conflict, knowing
  which persona is primary for this release tells you which need wins.

### What a persona is NOT

A persona is not a demographic profile. "Sarah, 34, lives in Austin, has
two kids, drives a Subaru" tells you nothing about what to build. A persona
is a behavioral archetype: what is this person trying to do, in what
context, and what gets in their way?

---

## When to Use

- You are writing user stories and the word "user" appears without
  qualification.
- You are starting a new project and have not identified who it is for.
- You are prioritizing a backlog and cannot explain which users benefit from
  each item.
- You are building an empathy map or journey map.
- Multiple stakeholders have different ideas about who "the user" is.
- A story map exists but does not indicate which personas each activity
  serves.
- You are designing a feature and realize you are imagining a vague,
  generic person.
- You hear "the user wants..." in a meeting and no one can name which user.
- You are reviewing stories that say "As a user" or "As a customer"
  without further specificity.
- You are planning a release and need to decide whose problems to solve
  first.

---

## When NOT to Use

- **Internal developer tooling with a single, well-understood user type.**
  If every user is literally the same role doing the same job, a persona
  exercise adds overhead without insight. Even here, check whether "the
  same role" actually hides different behavioral patterns (e.g., junior
  vs. senior developers have very different needs).
- **Pure technical infrastructure** with no user-facing surface (e.g.,
  database migration, CI pipeline optimization). Though even here, ask:
  "Who benefits downstream, and how?"
- **Incident response.** Fix the outage first. Identify affected personas
  in the post-mortem.
- **You already have well-established, validated personas** that the team
  uses daily. Do not re-derive them from scratch every sprint. Revisit them
  quarterly or when user research reveals a shift.

---

## Discovery Brief

**Reads**: Section 1 (Framing) — specifically the user types identified
**Writes**: Section 2 (Personas) of `discovery-brief.md`

If `discovery-brief.md` exists, read it first. The user types from framing are your
starting point — deepen each one into a full persona card.

---

## Core Pattern

### Lightweight Persona Cards

Personas should be lightweight enough to fit on an index card. If your
persona document is longer than a page, no one will read it and no one
will use it. Here is the format:

```
┌─────────────────────────────────────────────────┐
│  PERSONA CARD                                   │
│                                                 │
│  Name:           [A real-sounding first name]   │
│  Role:           [What they do, not who they    │
│                   are demographically]          │
│  Primary Goal:   [The #1 thing they are trying  │
│                   to accomplish]                │
│  Key Frustration:[The main thing that gets in   │
│                   their way today]              │
│  Context:        [One sentence about when/where │
│                   /how they interact with your  │
│                   product]                      │
│                                                 │
└─────────────────────────────────────────────────┘
```

That is five fields. Not twenty. Not a multi-page biography. Five fields
that fit on a sticky note. The constraint is the point — it forces you to
distill what actually matters about this user type.

### Example Persona Cards

#### Example: Project Management Tool

```
┌─────────────────────────────────────────────────┐
│  Name:           Priya                          │
│  Role:           New team member (first 90 days)│
│  Primary Goal:   Find where things are and      │
│                  understand team processes       │
│                  without constantly asking       │
│  Key Frustration:Information is scattered across │
│                  wikis, Slack, and shared drives │
│  Context:        Joins calls mid-project, has no│
│                  history, checks the tool 10+   │
│                  times/day looking for answers   │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  Name:           Marcus                         │
│  Role:           Team lead managing 3 projects  │
│  Primary Goal:   Know which projects are at risk│
│                  without chasing people for      │
│                  status updates                  │
│  Key Frustration:Spends 4+ hours/week asking    │
│                  "where are we on X?" in Slack   │
│  Context:        Checks the tool twice a day —  │
│                  morning planning, end-of-day    │
│                  review — from laptop and phone  │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  Name:           Dana                           │
│  Role:           Executive sponsor, 6 teams     │
│  Primary Goal:   Decide which initiatives to    │
│                  fund, pause, or kill            │
│  Key Frustration:Gets 50-slide decks when she   │
│                  needs 3 numbers                 │
│  Context:        Looks at the tool once a week,  │
│                  for 5 minutes, on her phone,    │
│                  between meetings                │
└─────────────────────────────────────────────────┘
```

Notice: no ages, no hobbies, no hometowns. Every field describes behavior
that changes what you build.

### How Personas Change Story Writing

The same feature, written for different personas, produces different
implementations:

#### Feature: "Dashboard"

**Without persona framing (red flag):**
```
As a user, I want a dashboard so that I can see project status.
```

This tells you nothing. What status? How much detail? How often do they
look? What decisions do they make from it? You cannot build this without
guessing.

**For Priya (new team member):**
```
As Priya, a new team member in her first month, I want to see which tasks
are assigned to me and which ones are urgent, so that I know what to work
on today without having to ask my team lead.

Acceptance criteria:
- Shows only MY tasks, not the entire project
- Urgent items are visually distinct
- Each task links to enough context that I can start working without
  asking someone "what does this mean?"
```

**For Marcus (team lead):**
```
As Marcus, a team lead managing 3 active projects, I want to see which
projects have stalled tasks (no updates in 48+ hours) so that I can
unblock my team before standup instead of discovering problems during it.

Acceptance criteria:
- Shows all 3 projects in a single view
- Stalled items (no activity in 48h) are highlighted
- I can drill into a stalled item to see the last update and who owns it
- View loads in under 3 seconds (Marcus checks this between meetings)
```

**For Dana (executive sponsor):**
```
As Dana, an executive sponsor reviewing 6 teams, I want to see which
initiatives are on track vs. at risk, so that I can decide where to
reallocate budget in my weekly portfolio review.

Acceptance criteria:
- One-screen summary of all initiatives with red/yellow/green status
- Each status links to a 2-sentence explanation, not a 50-page report
- Usable on a phone screen in portrait mode (Dana reads this between
  meetings)
- Shows trend (improving/declining), not just current state
```

Three stories for the "same" feature. Three different implementations.
Three different sets of acceptance criteria. This is why "As a user, I
want a dashboard" is useless — it hides three distinct problems behind
one vague sentence.

### How to Derive Personas

Personas must come from reality, not imagination.

**Good sources:**
- Support tickets (who files them? what do they struggle with?)
- User interviews (even 5 interviews reveal behavioral patterns)
- Analytics (what do different user segments actually do in the product?)
- Sales call recordings (what problems do prospects describe?)
- Observation (watch real people use the product for 15 minutes)

**Bad sources:**
- Brainstorming sessions with no user data
- Marketing demographic segments
- Stakeholder assumptions ("our users are probably...")
- Competitor analysis alone (their users are not your users)

If you have zero user research, start with support tickets. They are the
cheapest source of real user pain. Read 50 of them and patterns will
emerge.

### Prioritizing Personas

Not all personas are equal. For any given release, one persona is primary.

1. **Primary persona** — This release is FOR this person. Their needs win
   when trade-offs arise. Every story in the release should serve them.
2. **Secondary persona(s)** — Benefit from the release but do not drive
   decisions. Their needs are accommodated if they do not conflict with
   the primary persona.
3. **Excluded persona(s)** — Explicitly not served by this release. Naming
   who you are NOT building for is as important as naming who you are.

#### Example: Project management tool, Release 1

```
PRIMARY:    Priya (new team member)
            Why: Onboarding is where we lose 40% of trial users.
            Every story in R1 must improve Priya's first-week
            experience.

SECONDARY:  Marcus (team lead)
            Why: Marcus benefits from Priya being self-sufficient.
            We accommodate his needs if they don't conflict with
            Priya's.

EXCLUDED:   Dana (executive sponsor)
            Why: Dana's needs (portfolio-level views, budget
            tracking) require data maturity we don't have yet.
            We will address Dana in Release 3.
```

This makes prioritization mechanical. When someone says "Should we add
portfolio-level views?" the answer is: "That is Dana's need. Dana is
excluded from this release. It goes below the line."

### Linking Personas to the Story Map

On a story map, annotate which personas each activity serves:

```
ACTIVITIES:   Sign Up    Set Up Project    Track Work    Report
PERSONAS:     [Priya]    [Priya, Marcus]   [Marcus]      [Dana]
```

This reveals:
- Which activities serve the primary persona (focus here for this release)
- Which activities only serve excluded personas (defer them)
- Which activities serve multiple personas (design carefully — their needs
  may differ)

---

## Quick Reference

| Principle | How to apply it |
|-----------|----------------|
| **"The user" is a red flag** | Every story must name a specific persona. If you write "As a user," stop and ask: which user? |
| **Behavior over demographics** | Define personas by goals, context, and frustrations — never by age, location, or income. |
| **Keep it to 3-5 personas** | More than 5 means you have not prioritized. Fewer than 2 means you have not looked hard enough. |
| **Derive from data, not imagination** | Support tickets, interviews, analytics, and observation. Never brainstorm personas in a room with no user data. |
| **One primary persona per release** | When needs conflict, the primary persona wins. Name them explicitly. |
| **Name who you exclude** | Stating who this release is NOT for is as important as stating who it is for. It prevents scope creep. |
| **Five fields, fits on a card** | Name, role, primary goal, key frustration, one sentence of context. If your persona doc is longer, no one will use it. |
| **Same feature, different story per persona** | If two personas need "search," write two stories. The acceptance criteria will differ because the underlying needs differ. |
| **Annotate the story map** | Mark which personas each activity serves. This reveals where to focus for a given release. |
| **Revisit, don't rewrite** | Personas evolve as you learn. Update them quarterly based on new data, but do not start from scratch. |

---

## Common Mistakes

| Mistake | Why it is wrong | What to do instead |
|---------|----------------|-------------------|
| **"As a user" stories** | Designing for "the user" means designing for no one. You cannot test, prioritize, or make trade-offs without knowing WHO. | Replace every "As a user" with "As [persona name]" and add their goal in context. |
| **Demographic personas** | "Sarah, 34, Austin, two kids" tells you nothing about what to build. Demographics do not predict behavior. | Define personas by role, goal, frustration, and context. Drop demographics entirely. |
| **Too many personas (6+)** | You cannot meaningfully design for 8 different user types. Having too many is the same as having none — you end up compromising for all of them. | Consolidate to 3-5 behavioral archetypes. Merge personas that have similar goals and contexts. |
| **Fictional personas with no data** | Personas invented in a brainstorming session reflect the team's assumptions, not user reality. They give false confidence. | Ground every persona in at least one real data source: support tickets, interviews, analytics, or observation. |
| **Persona documents no one reads** | A 10-page persona brief gets filed and forgotten. It has zero impact on daily decisions. | Use the index-card format: 5 fields, fits on a sticky note, posted on the team wall or pinned in the team chat. |
| **All personas treated as equally important** | When every persona matters equally, every feature matters equally, and nothing gets prioritized. | Designate one primary persona per release. Secondary personas are accommodated. Excluded personas are explicitly named. |
| **Creating personas once and never updating** | Users evolve. The personas you defined 18 months ago may no longer match reality. | Review personas quarterly. Update them when user research, support trends, or usage data reveal behavioral shifts. |
| **Personas without connection to stories** | Personas exist as a document but stories still say "As a user." The personas had no impact on the actual work. | Enforce a rule: no story enters the backlog without a named persona. Make it a checklist item in story review. |
| **Confusing personas with user roles** | "Admin" and "viewer" are system roles, not personas. Two admins may have completely different goals and frustrations. | Personas cut across roles. Priya might be an admin AND a new hire. Marcus might be an admin AND a team lead. The role is a permission level; the persona is a behavioral pattern. |

---

## Related Skills

- **[discovery-framing](../discovery-framing/SKILL.md)** — Frame the
  problem space before defining personas. You need to understand the
  domain before you can identify meaningful behavioral archetypes.
- **[story-mapping](../story-mapping/SKILL.md)** — The story map
  organizes activities by user journey. Persona framing tells you WHOSE
  journey you are mapping and which activities matter for which users.
- **[outcome-over-output](../outcome-over-output/SKILL.md)** — Outcomes
  are meaningless without a specific persona whose behavior you expect to
  change. "Increase engagement" means nothing. "Priya completes onboarding
  in under 10 minutes" is a real outcome.
- **[shared-understanding](../shared-understanding/SKILL.md)** — Personas
  are a tool for shared understanding. The whole team must agree on who
  the primary persona is, or they will build for different imaginary users
  and the product will be incoherent.
