# Product Discovery Practices

This plugin helps teams build the right thing by applying user story mapping and product discovery techniques inspired by Jeff Patton's "User Story Mapping" book. These are standing instructions for any planning, scoping, or prioritization activity.

## Rules — Non-Negotiable

These rules apply whenever you are planning, scoping, writing stories, defining requirements, or making build-vs-skip decisions. They are not suggestions.

1. **Start with the router.** When any discovery activity begins, load `discovery-overview` first. It is the single entry point that decides which skills to load and in what order. Do not pick individual skills yourself — the router owns that decision.
2. **No unnamed users.** Every story, feature, or requirement names a specific persona. "As a user" is not acceptable. If you cannot name the persona, stop and load `persona-framing` first.
3. **Outcomes before outputs.** Before committing to build anything, state the measurable behavior change you expect. "Ship feature X" is output. "Reduce time-to-first-value by 40%" is an outcome. If you cannot articulate the outcome, you do not yet understand why you are building it.
4. **Slice thin.** The goal is not to deliver everything — it is to deliver the thinnest possible slice that lets you learn whether you are on the right track. Thick slices delay learning. When in doubt, slice thinner.
5. **Frame before solving.** Understand the problem space before proposing solutions. Jumping to solutions is the single biggest source of wasted work. Do not discuss technology, architecture, or code until at minimum framing, personas, and story-mapping are complete.
6. **Write to the discovery brief.** As each skill completes, append its outputs to `discovery-brief.md`. This is the accumulating artifact that carries context between skills. See `references/discovery-brief-template.md` for the format.
7. **Ask one question at a time.** Discovery is a conversation, not a questionnaire. Ask one question, wait for the answer, follow up if needed, then move on. Dumping multiple questions at once produces shallow answers.

## Before Responding — Mental Checklist

Before you write any planning output (stories, specs, requirements, scope decisions, backlog items), verify:

- [ ] Have I loaded `discovery-overview` (or the relevant specific skill)?
- [ ] Can I name the persona this is for?
- [ ] Have I stated the outcome (not just the output)?
- [ ] Is this the thinnest useful slice?
- [ ] Am I writing outputs to `discovery-brief.md`?

If any answer is no, stop and address it before continuing.

## Discovery Pipeline

The router (`discovery-overview`) guides skills in this sequence:

```
framing → personas → story-mapping → walking-skeleton → thin-slicing → mvp-as-experiment → release-planning
```

Not every project needs every step. The router skips steps based on context. Load `discovery-overview` and it handles the rest.

## Skill Router — Load Based on Activity

| You are about to... | Load this skill |
|----------------------|----------------|
| Start any discovery or planning work | `discovery-overview` (the router) |
| Plan a new project or feature | `discovery-framing`, `story-mapping` |
| Define who the users are | `persona-framing` |
| Organize work into a backlog | `story-mapping`, `rock-breaking` |
| Decide what to build first | `now-later-never`, `thin-slicing` |
| Define MVP or v1 scope | `mvp-as-experiment`, `walking-skeleton` |
| Plan releases or milestones | `release-planning` |
| Write user stories | `persona-framing`, `outcome-over-output` |
| Brainstorm or kickoff | `discovery-framing`, `shared-understanding` |
| Break down large features | `rock-breaking`, `thin-slicing` |
| Define success metrics | `outcome-over-output` |
| Prioritize or cut scope | `now-later-never`, `thin-slicing` |
| Align the team on requirements | `shared-understanding` |

## During Planning

- **Always ground stories in personas.** A story without a clear user is a solution looking for a problem. If you cannot name the persona, you are not ready to write the story.
- **Always define outcomes before building.** Before committing to build anything, articulate what measurable change you expect. If you cannot state the outcome, you do not yet understand why you are building it.
- **Slice thin and ship early.** The goal is not to deliver everything — it is to deliver the thinnest possible slice that lets you learn whether you are on the right track. Thick slices delay learning.
- **Use multiple agents to parallelize discovery work.** When a planning task involves several skills (e.g., persona-framing + story-mapping + now-later-never), spin up agents in parallel to work on independent sections simultaneously. For example, one agent can run discovery-framing while another works on persona research, then combine the results. This is especially valuable for large planning sessions that touch many skills at once.

## Spec Output

When discovery is complete, write a spec file with epics, user stories, and acceptance criteria. The `discovery-overview` skill defines the exact format. Every story must be grounded in a named persona and tied to a measurable outcome.

## Agent Checkpoints

| When | Run this |
|------|----------|
| Start of a new project | `discovery-health-check` agent |
| After completing a planning session | `discovery-review` agent |

## Why This Matters

Teams that understand the problem deeply build the right thing. The biggest waste in software is not building software slowly — it is building the wrong software quickly. Discovery practices exist to close the gap between what the team assumes users need and what users actually need. Every hour spent on discovery saves days of building features nobody wanted.
