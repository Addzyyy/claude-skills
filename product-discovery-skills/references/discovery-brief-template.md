# Discovery Brief Template

This is the shared artifact that accumulates as you work through the discovery pipeline.
Each skill appends its section. Do not overwrite previous sections — build on them.

Write this file to `discovery-brief.md` in the project root (or working directory).

---

## Template

```markdown
# Discovery Brief: [Project Name]

*Last updated: [date]*
*Status: [which pipeline step is current]*

---

## 1. Framing (discovery-framing)

### Opportunity Statement
> We believe there is an opportunity to [improve/enable/transform] [something]
> for [someone], which will [desired business outcome].

### User Types Identified
| User Type | Description | Priority |
|-----------|-------------|----------|
| [Name] | [One-line description] | Primary / Secondary / Excluded |

### Problems Surfaced
| Problem | Who | Severity | Frequency |
|---------|-----|----------|-----------|
| [Problem] | [User type] | High/Med/Low | Daily/Weekly/Rare |

### Assumptions & Risks
| Assumption | Type | Confidence | Impact | Priority |
|------------|------|------------|--------|----------|
| [Assumption] | User/Problem/Solution/Business | Low/Med/High | Low/Med/High | Test first/second/third |

### Testable Hypotheses
> We believe [assumption]. We will test this by [method].
> Right if [signal]. Wrong if [signal].

---

## 2. Personas (persona-framing)

### [Persona Name] — Primary
- **Role**: [What they do]
- **Goal**: [What they're trying to accomplish]
- **Context**: [Their environment, constraints, tools]
- **Pain**: [What's painful about their current situation]
- **Behavior**: [How they currently solve this problem]

### [Persona Name] — Secondary
[Same format]

---

## 3. Story Map (story-mapping)

### Backbone (Activities — left to right)
1. [Activity 1: User's high-level goal]
2. [Activity 2: Next step in the journey]
3. [Activity 3: ...]

### Body (Stories under each activity — top to bottom by priority)

**Activity 1: [Name]**
- [Story 1 — highest priority]
- [Story 2]
- [Story 3 — lowest priority]

**Activity 2: [Name]**
- [Story 1]
- [Story 2]

### Slice Lines
- **Slice 1 (Walking Skeleton)**: [Which stories from each activity]
- **Slice 2**: [Next increment]
- **Slice 3**: [Next increment]

---

## 4. Walking Skeleton (walking-skeleton)

### End-to-End Path
[Describe the thinnest path through the system that a user can walk]

### Integration Points
| Layer | What exists in the skeleton |
|-------|---------------------------|
| UI | [Minimal interface] |
| Logic | [Core flow only] |
| Data | [Simplest storage] |
| External | [Any integrations] |

---

## 5. Thin Slices (thin-slicing)

### Release 1 Scope
[Stories included, rationale for the cut line]

### What's Deferred
[Stories below the line, why they're deferred, not deleted]

---

## 6. MVP Experiment (mvp-as-experiment)

### Hypothesis
> We believe [persona] will [behavior] because [reason].

### Experiment Design
- **What we're building**: [Minimal thing]
- **What we're measuring**: [Specific metric]
- **Success looks like**: [Threshold]
- **Failure looks like**: [Threshold]
- **Timeline**: [How long before we evaluate]

---

## 7. Release Plan (release-planning)

### Release 1: [Theme]
**After this release, users can**: [Complete sentence]
- [Epic/story list]
- **Target**: [Date or sprint]

### Release 2: [Theme]
**After this release, users can**: [Complete sentence]
- [Epic/story list]

---

## Parking Lot

### LATER (explicitly deferred)
- [Item] — Reason: [why not now]

### NEVER (explicitly killed)
- [Item] — Reason: [why never]

---

## Open Questions
- [ ] [Unresolved question or assumption needing validation]
```

---

## How skills use this template

| Skill | Reads sections | Writes section |
|-------|---------------|----------------|
| discovery-framing | (none — starts fresh) | 1. Framing |
| persona-framing | 1. Framing (user types) | 2. Personas |
| story-mapping | 2. Personas, 1. Framing (problems) | 3. Story Map |
| walking-skeleton | 3. Story Map | 4. Walking Skeleton |
| thin-slicing | 3. Story Map, 4. Walking Skeleton | 5. Thin Slices |
| mvp-as-experiment | 5. Thin Slices, 2. Personas | 6. MVP Experiment |
| release-planning | 3. Story Map, 5. Thin Slices | 7. Release Plan |
| now-later-never | Any | Parking Lot |
| outcome-over-output | Any | (Inline — refines success metrics in relevant sections) |
| rock-breaking | 3. Story Map | (Inline — splits stories within Story Map section) |
| shared-understanding | Any | Open Questions |
