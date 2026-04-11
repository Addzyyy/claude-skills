---
name: discovery-overview
description: >
  Load at the START of any planning session, product discussion, feature scoping,
  requirements gathering, project kickoff, or brainstorm — this is the master skill
  that routes to all product discovery practices and agents. When in doubt, load this
  first. Also load when the user mentions building something new, asks "what should we
  build", discusses users or personas, talks about priorities or backlogs, or starts
  any conversation about a product that doesn't exist yet. This skill is the single
  entry point for all discovery work.
---

# Product Discovery — Overview & Router

**This is not reference material. These are standing instructions.**

When this skill is loaded, you guide the user through product discovery practices in
sequence. Do not dump the whole framework at once. Work through it step by step,
asking one question at a time, and only advancing when the current step is complete.

## The Discovery Pipeline

Discovery follows a deliberate sequence. Each step builds on the previous one.
Not every project needs every step — use judgment to skip steps that are already
done or don't apply.

```
framing → personas → story-mapping → walking-skeleton → thin-slicing → mvp-as-experiment → release-planning
```

| Step | Skill | What it produces | When to skip |
|------|-------|-----------------|--------------|
| 1. Frame the problem | `discovery-framing` | Opportunity statement, user types, problems, assumptions | Problem space is already well-understood and validated |
| 2. Define personas | `persona-framing` | Named persona cards with goals, context, pain points | User already has clear, specific personas defined |
| 3. Map the journey | `story-mapping` | Story map with backbone (activities) and body (stories) | Work is a single well-scoped feature, not a product |
| 4. Build the skeleton | `walking-skeleton` | The thinnest end-to-end path through the system | System architecture already exists and is proven |
| 5. Slice thin | `thin-slicing` | Release slices drawn across the story map | Scope is already small enough to ship in one go |
| 6. Frame the MVP | `mvp-as-experiment` | Hypothesis, experiment design, success/failure criteria | Team is past validation — building a known solution |
| 7. Plan releases | `release-planning` | Themed release increments with clear "after this, users can ___" | Only one slice exists — nothing to sequence |

Supporting skills (load when needed at any point):
- `outcome-over-output` — When defining success criteria or acceptance criteria
- `now-later-never` — When prioritizing or cutting scope
- `rock-breaking` — When a story is too big to estimate or build
- `shared-understanding` — When alignment is at risk or requirements are ambiguous

## How to Work Through the Pipeline

### Conversation style

Ask **one question at a time**. Wait for the user's answer before moving on. Discovery
is a conversation, not a questionnaire. If you dump five questions at once, the user
skims them and gives shallow answers. One question, answered well, is worth more than
five questions answered superficially.

The reason this matters: discovery is about depth of understanding, not breadth of
coverage. A single probing follow-up ("Why is that painful?") reveals more than a
checklist. Treat each question as a mini-conversation — listen to the answer, ask a
follow-up if something is unclear, then move on.

### Tracking progress

As you work through the pipeline, keep a mental model of what's been completed:

- **Done**: Steps where the user has provided enough information to move forward
- **Current**: The step you're actively working on
- **Next**: What comes after the current step
- **Skipped**: Steps explicitly skipped (with reason)

When transitioning between steps, briefly summarize what you learned and what comes
next. For example: "Good — we've identified 3 personas. Next, let's map their journey
through the system. I'll load story-mapping."

### Writing to the discovery brief

As each step completes, write the outputs to `discovery-brief.md` in the project root
(or whatever working directory makes sense). Read `references/discovery-brief-template.md`
for the template format. Each skill appends its section — do not overwrite previous
sections. The brief is the accumulating artifact that carries context between skills.

If a `discovery-brief.md` already exists, read it first — previous discovery work has
been done and you should build on it, not start over.

## The "Skipping Ahead" Guardrail

If the user mentions specific technologies, frameworks, languages, databases, APIs,
architecture patterns, or file structures **before** at minimum framing, personas, and
story-mapping are complete — gently intervene.

The intervention is not blocking. Say something like:

> "We haven't mapped the user journey yet. Want to do that first, or are you
> intentionally jumping to implementation?"

If the user explicitly says they want to skip discovery ("I know my users, let's just
code"), respect that. But make them say it consciously — do not silently let discovery
get skipped because the user got excited about a tech stack.

Why this matters: the single biggest source of wasted engineering time is building the
wrong thing. Technology decisions made before understanding the user's journey optimize
for the wrong constraints. A 10-minute discovery conversation can save weeks of building
features nobody wanted.

Keywords that trigger the guardrail (before discovery is complete):
- Framework/library names: React, Next.js, Django, Rails, Express, Electron, etc.
- Infrastructure: AWS, Docker, Kubernetes, PostgreSQL, MongoDB, Redis, etc.
- Architecture: microservices, monolith, serverless, REST, GraphQL, etc.
- Code structure: "let's create a src/ directory", "the API should...", "the schema..."

## Skill Router — Load Based on Activity

When you detect these activities, load the corresponding skill:

| Activity | Load this skill |
|----------|----------------|
| Starting a new project or feature | `discovery-framing` (Step 1) |
| Defining or discussing who the users are | `persona-framing` (Step 2) |
| Organizing work, planning what to build | `story-mapping` (Step 3) |
| Deciding where to start, first thing to build | `walking-skeleton` (Step 4) |
| Scope is growing, need to cut | `thin-slicing` (Step 5) |
| Defining what v1 or MVP looks like | `mvp-as-experiment` (Step 6) |
| Sequencing delivery into milestones | `release-planning` (Step 7) |
| Writing stories with "as a user" (generic) | `persona-framing` |
| Defining success metrics or acceptance criteria | `outcome-over-output` |
| Feature/story too big to estimate | `rock-breaking` |
| Prioritizing or saying no to features | `now-later-never` |
| Requirements feel ambiguous or contested | `shared-understanding` |

## Agent Checkpoints

| When | Run this |
|------|----------|
| Start of a new project | `discovery-health-check` agent |
| After completing a planning session | `discovery-review` agent |
| When a specific practice needs improvement | `discovery-improve` agent |

## Writing the Final Spec

When discovery is complete and the user wants a deliverable, write a spec file
(`spec.md` or a name the user chooses) with this structure:

```markdown
# [Project Name] — Product Spec

## Discovery Summary
- **Opportunity**: [from framing]
- **Primary personas**: [from persona-framing]
- **Key problems**: [from framing]
- **Success metrics**: [from outcome-over-output]

## Epics

### Epic 1: [Name]
**Outcome**: [What changes for the user when this epic is complete]

#### User Stories

**[Persona Name]** wants to [goal] so that [outcome].

Acceptance Criteria:
- [ ] [Specific, testable criterion]
- [ ] [Specific, testable criterion]
- [ ] [Specific, testable criterion]

[Repeat for each story in the epic]

### Epic 2: [Name]
[Same structure]

## Release Plan
- **Release 1 (Walking Skeleton)**: [Epics/stories in first release, what users can do after]
- **Release 2**: [Next increment]
- **Release 3**: [Next increment]

## Parking Lot (LATER / NEVER)
- LATER: [Items explicitly deferred with rationale]
- NEVER: [Items explicitly killed with rationale]

## Open Questions & Risks
- [Unresolved assumptions that need validation]
```

Ground every story in a named persona. Tie every epic to an outcome. Include
acceptance criteria that are testable — "user can do X" not "feature is implemented."

### Visual Story Map

After writing the spec, also generate a visual story map using the bundled script:

```bash
python3 scripts/generate_story_map.py story-map.json story-map.html
```

Write the story map data as JSON (see `story-mapping` skill for the format), then
run the script. The output is a standalone HTML file with activities across the top,
stories stacked below as cards, color-coded by persona, grouped into release slices.
This gives the user a visual artifact they can share alongside the spec.

## How Skills Compose

Skills are complementary, not competing. Load multiple skills when the activity spans
multiple concerns. When the user's context is specific, load the most specific skill
rather than staying at this overview level.
