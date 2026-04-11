---
name: story-mapping
description: >
  Apply when personas are defined and you need to map the user's journey through
  the system — the state where you know WHO the users are and WHAT problems they
  have, but haven't yet organized the work into a narrative structure. Trigger when
  no user journey exists yet, when the backlog is a flat list with no visible narrative,
  when the team needs to see the big picture of what users do, or when someone asks
  "what should we build" or "how do we organize this work." This is the foundational
  planning technique that turns personas and problems into an organized story map.
---

# User Story Mapping

## Overview

A user story map is a two-dimensional arrangement of user stories. Activities and tasks flow left-to-right across the top — the "backbone" — representing the user's journey through the system. Below each backbone item, specific user stories stack top-to-bottom, ordered by priority (most critical near the top). The result is a narrative of how a user accomplishes a goal, not a flat list of features. Drawing horizontal lines across the map creates release slices — each slice is a shippable increment that delivers end-to-end value.

The conversation that happens while building the map matters as much as the map itself. Story mapping is a shared-understanding tool first and a planning artifact second.

## When to Use

- Starting a new product or major feature — you need to see the whole before breaking it into parts
- A flat backlog has become an unordered pile of tickets with no visible narrative
- The team disagrees on what "done" means for a feature or release
- Stakeholders ask "what are we building?" and no one can explain the user's journey end-to-end
- Planning which stories belong in which release — you need to draw slice lines
- Onboarding new team members who need to understand the product's scope and priorities
- Any time you hear "what should we build first?" or "how do we break this down?"

## When NOT to Use

- A single, well-understood bug fix or technical chore with no user-facing narrative
- The team already has a shared, current map and the work is just executing known stories
- Premature detail — do not story-map before you understand who the user is (use persona-framing first)
- Infrastructure-only work with no direct user activity to map (use a technical spike or task list instead)

## Discovery Brief

**Reads**: Section 2 (Personas) and Section 1 (Framing — problems)
**Writes**: Section 3 (Story Map) of `discovery-brief.md`

If `discovery-brief.md` exists, read it first. Use the personas and problems as
inputs to building the map.

## Core Pattern

### Step 1: Identify the User and Their Goal

Start with one sentence: **"[User] wants to [goal] so that [outcome]."**

```
Example: "A hiring manager wants to post a job and review applicants
          so that they can fill an open position."
```

### Step 2: Map the Backbone (Left to Right)

Walk through the user's journey at a high level. Each card across the top is an **activity** — a big verb phrase describing what the user does. Under each activity, identify the **tasks** — the specific steps to accomplish that activity.

```
BACKBONE (activities, left to right):
+----------------+   +----------------+   +----------------+   +----------------+
|  Create Job    |   |  Publish Job   |   |  Review        |   |  Make Hiring   |
|  Posting       |   |  Listing       |   |  Applicants    |   |  Decision      |
+----------------+   +----------------+   +----------------+   +----------------+
       |                    |                    |                     |
    TASKS:               TASKS:               TASKS:               TASKS:
  - Write title        - Choose boards      - View list         - Compare top
    & description      - Set dates          - Read resumes        candidates
  - Set salary         - Preview listing    - Filter/sort       - Schedule
    range              - Confirm & post     - Add notes           interviews
  - Add requirements                        - Share w/ team     - Extend offer
  - Choose department                       - Reject/advance    - Send rejection
```

The backbone tells the story. Read it left to right and it should sound like a narrative: "First the hiring manager creates a job posting, then publishes it, then reviews applicants, then makes a hiring decision."

### Step 3: Add Detail Below Each Task (Top to Bottom)

Below each task, stack the specific user stories or details. Higher = higher priority. Lower = nice-to-have or later.

```
Activity: REVIEW APPLICANTS
+------------------------------------------+
|  View Applicants (task - backbone)        |
+------------------------------------------+
|  See list of names + dates applied        |  <-- must-have (top)
|  View resume / CV inline                  |
|  Filter by keyword or status              |
|  Sort by date, rating, or match score     |
|  Bulk reject unqualified applicants       |
|  AI-suggested match score                 |  <-- nice-to-have (bottom)
+------------------------------------------+
```

### Step 4: Slice Into Releases

Draw horizontal lines across the entire map. Everything above the first line is Release 1 — the minimum end-to-end experience. Each subsequent slice adds richness.

```
FULL STORY MAP WITH RELEASE SLICES:

          Create Job       Publish Job      Review            Decide
          Posting          Listing          Applicants        on Hire
         +-----------+    +-----------+    +-----------+    +-----------+
BACKBONE |Write title|    |Choose     |    |View list  |    |Compare    |
(tasks)  |Set salary |    | boards    |    |Read resume|    | candidates|
         |Add reqs   |    |Preview    |    |Filter/sort|    |Schedule   |
         |Choose dept|    |Post       |    |Add notes  |    |Extend     |
         +-----------+    +-----------+    +-----------+    | offer     |
              |                |                |           +-----------+
              |                |                |                |
- - - - - - -|- - - - - - - -|- - - - - - - -|- - - - - - - -|- - - -
 RELEASE 1   |  Title + desc  |  Post to 1    |  Name list +  |  Mark
 (MVP)       |  Salary range  |   board       |   resume view |  yes/no
             |  Department    |               |               |
- - - - - - -|- - - - - - - -|- - - - - - - -|- - - - - - - -|- - - -
 RELEASE 2   |  Requirements  |  Multi-board  |  Filter by    |  Side-by-
             |  Rich text     |  Schedule     |   keyword     |   side
             |   editor       |   dates       |  Add notes    |   compare
             |               |  Preview      |               |  Interview
             |               |               |               |   scheduling
- - - - - - -|- - - - - - - -|- - - - - - - -|- - - - - - - -|- - - -
 RELEASE 3   |  Templates    |  Social media |  AI match     |  Offer
             |  Clone prev.  |   sharing     |   score       |   letter
             |   posting     |  Analytics    |  Bulk actions  |   template
             |               |               |  Team sharing  |  Rejection
             |               |               |               |   emails
```

**The key insight:** every release slice cuts all the way across the map. Release 1 is not "finish the first activity" — it is a thin slice through every activity so the user can go end-to-end. The user can create a posting, publish it, review applicants, and make a decision in Release 1. It is minimal, but it is complete.

### Step 5: Validate the Slices

For each release slice, ask:

1. **Can a user accomplish their goal end-to-end?** If any column is empty in a slice, the user gets stuck.
2. **Is this slice small enough to ship soon?** If it takes more than a few weeks, break it thinner.
3. **Does each slice add meaningful value beyond the previous one?** If not, merge slices or reorder.

## Building the Map — Facilitation Checklist

| Step | Action | Output |
|------|--------|--------|
| 1. Frame | State the user, their goal, and the outcome in one sentence | Goal statement |
| 2. Walk the backbone | Ask "what does the user do first? then next?" — write activities left to right | Backbone row of activity cards |
| 3. Break into tasks | Under each activity, list the concrete steps the user takes | Task cards under each activity |
| 4. Tell the story | Read the backbone left to right aloud — does it sound like a coherent narrative? | Validated backbone |
| 5. Add details | Under each task, add user stories or specifics, priority-ordered top to bottom | Full 2D map |
| 6. Slice | Draw horizontal lines to define release boundaries | Release plan |
| 7. Challenge | For each slice: can the user go end-to-end? Is the scope achievable? | Validated slices |

## Worked Example — E-Commerce Checkout

**Goal:** "A customer wants to buy items in their cart so they can receive the products."

```
        Browse &        Enter           Choose          Pay             Confirm
        Select          Shipping        Shipping                        Order
       +----------+   +----------+   +----------+   +----------+   +----------+
       |Add to    |   |Enter     |   |Select    |   |Enter     |   |Review    |
       | cart     |   | address  |   | speed    |   | card     |   | summary  |
       |View cart |   |Save addr.|   |See cost  |   |Apply     |   |Place     |
       |Edit qty  |   |Validate  |   |Est.      |   | coupon   |   | order    |
       |Remove    |   | address  |   | delivery |   |Choose    |   |Get       |
       | item     |   |Multi-    |   |In-store  |   | method   |   | confirm. |
       +----------+   | address  |   | pickup   |   |Fin.      |   |Track     |
                       +----------+   +----------+   | options  |   | order    |
                                                      +----------+   +----------+

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RELEASE 1:  Add to cart   Address form   Standard       Credit card   Summary +
(MVP)       View cart     (1 address)    shipping       only          place order
            Edit qty                     only                         Email
                                                                      confirm
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RELEASE 2:  Remove item   Address        Express /      Coupon        Order
            Save for      validation     economy        codes         tracking
            later         Saved          options        PayPal        page
                          addresses      Est. date
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RELEASE 3:  Wish list     Multi-address  In-store       Financing     Reorder
            Recommend-    (gift          pickup         Apple/Google  from
            ations        shipping)                     Pay           history
```

Notice: Release 1 is not "just the cart." It goes all the way from adding items to receiving a confirmation. That is what makes it a real slice, not a half-built feature.

## Map Anatomy — Key Terminology

| Term | Meaning | Position on Map |
|------|---------|-----------------|
| Activity | A high-level thing the user does (verb phrase) | Top row, left to right |
| Task | A concrete step within an activity | Second row, under its activity |
| User Story | A specific detail, behavior, or variation | Below tasks, stacked by priority |
| Backbone | The top row(s) of activities and tasks | Horizontal, left to right |
| Walking Skeleton | The thinnest possible end-to-end slice | First release slice |
| Release Slice | A horizontal cut across the map defining a shippable increment | Horizontal line across all columns |

## Quick Reference

| Rule | Guidance |
|------|----------|
| Start with the user's goal | The map is a narrative about a person accomplishing something, not a feature list |
| Backbone flows left to right | Activities are in the order the user does them, not in the order you want to build them |
| Priority flows top to bottom | Most essential details at the top of each column, nice-to-haves at the bottom |
| Every slice crosses the whole map | A release is not "finish column 1" — it is a thin pass through every activity |
| Tell the story out loud | Read the backbone aloud; if it does not sound like a narrative, restructure it |
| Build the map together | The conversation IS the value; a map built alone misses the shared understanding |
| Keep it physical first | Sticky notes on a wall beat digital tools for initial mapping — move to digital for persistence |
| The map is not the backlog | The map is a visualization and planning tool; individual stories flow into the backlog when prioritized into a slice |

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Building the map alone | Produces one person's understanding, not shared understanding | Facilitate a group session; include developers, designers, and stakeholders |
| Treating it as a flat list rotated sideways | Loses the 2D structure that shows priority AND sequence | Ensure the backbone reads as a narrative AND the vertical axis shows priority |
| First release slice is too thick | "MVP" takes 6 months and includes every edge case | Slice thinner — ask "what is the absolute minimum at each step for the user to succeed?" |
| First release slice does not cross all columns | User gets stuck mid-journey — can start but not finish | Every slice must include at least one story under every backbone activity |
| Skipping the backbone conversation | Team jumps to details without agreeing on the high-level journey | Force the team to agree on activities first; do not add details until the backbone is validated |
| Never updating the map | Map becomes stale and ignored after the first session | Revisit the map at the start of each planning cycle; it is a living artifact |
| Confusing activities with solutions | Backbone says "click the dropdown" instead of "choose a category" | Write activities as user goals, not UI interactions |
| Too many activities on the backbone | Map becomes unreadable with 20+ columns | Group related tasks under 5-8 high-level activities; use sub-maps for detail |

## Anti-Pattern: The Flat Backlog

A flat backlog (ordered list of stories) loses two dimensions of information that a story map preserves:

```
FLAT BACKLOG (what most teams have):        STORY MAP (what you should build):

1. User can enter address                       [journey across the top]
2. User can add item to cart                        |
3. User can pay with credit card                    |  [priority down
4. User can view order confirmation                 |   the side]
5. User can apply coupon                            |
6. User can choose shipping speed                   v
7. User can track order
8. ...

No visible journey. No release slices.       Shows the whole, reveals the slices.
No way to tell if a "release" is             Every slice is end-to-end.
end-to-end or just a random subset.
```

The flat backlog answers "what's next?" The story map answers "what's the whole thing, and what's the thinnest useful version of it?"

## Generating a Visual Story Map

After building the map, generate a visual HTML story map using the bundled script.
Write the map data as JSON and run:

```bash
python3 scripts/generate_story_map.py story-map.json story-map.html
```

The JSON format:
```json
{
  "title": "Project Name",
  "personas": ["Persona 1", "Persona 2"],
  "activities": [
    {
      "name": "Activity Name",
      "stories": [
        {"text": "Story description", "persona": "Persona 1", "slice": 1}
      ]
    }
  ],
  "slices": [
    {"name": "Walking Skeleton"},
    {"name": "Release 2"}
  ]
}
```

The `slice` field is 1-indexed and matches the slices array. The output is a
standalone HTML file with a card-based grid: activities across the top, stories
stacked below, color-coded by persona, grouped into release slices. Open it in
a browser to view.

## Related Skills

- **thin-slicing** — once the map is built, thin-slicing helps cut each release slice as thin as possible while preserving end-to-end value
- **walking-skeleton** — the first release slice on the story map is the walking skeleton: the minimum end-to-end path through the system
- **release-planning** — release slices from the map feed directly into release planning; the map provides the structure, release planning adds dates and capacity
- **persona-framing** — build the persona BEFORE building the map; the backbone is this persona's journey, and the goal statement comes from persona work
- **rock-breaking** — when individual stories on the map are still too large, use rock-breaking to decompose them into smaller implementable pieces
