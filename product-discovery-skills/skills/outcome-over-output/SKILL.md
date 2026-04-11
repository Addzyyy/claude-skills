---
name: outcome-over-output
description: >
  Use this skill whenever writing user stories, defining acceptance criteria,
  planning sprints or iterations, discussing success metrics, evaluating what
  to build next, running retrospectives, prioritizing a backlog, or any time
  the conversation touches "what does done look like." If someone frames work
  in terms of features shipped, stories completed, or velocity — stop and
  apply this skill. Every piece of work should be tied to a measurable change
  in user behavior, not to a checkbox on a task list.
---

# Outcome Over Output

## Overview

Shipping features is **output**. Changing user behavior is **outcome**.

The goal of product development is never to build what is on the backlog. The
goal is to solve the user's problem. A team that ships 47 stories in a sprint
but moves no metric has produced waste. A team that ships 3 stories and moves
onboarding completion from 34% to 61% has produced value.

This skill, drawn from Jeff Patton's *User Story Mapping*, forces you to
reframe every piece of work around the change it creates for users — not the
artifact it produces for the team.

**The core rule:** if you cannot articulate the outcome, you do not understand
the problem well enough to build the solution.

---

## When to Use

- Writing or refining user stories
- Defining acceptance criteria or "definition of done"
- Sprint/iteration planning
- Backlog grooming and prioritization
- Evaluating competing feature ideas
- Defining success metrics for a feature or release
- Running retrospectives ("did we achieve what we set out to achieve?")
- Any conversation where someone says "we need to build X" without saying why
- Roadmap discussions framed around feature lists instead of user problems
- Stakeholder reviews where progress is reported as story count or velocity

---

## When NOT to Use

- Pure technical infrastructure work with no direct user-facing change (though
  even here, ask: "what user outcome does this enable?")
- Compliance or regulatory tasks where the output IS the requirement (e.g.,
  "the audit log must exist")
- Incident response — fix the fire first, measure later
- Exploratory spikes where you are still discovering what outcome is possible

---

## Core Pattern

### The Hypothesis Format

Every feature should be stated as a hypothesis before any code is written:

> **We believe** [this capability] **will result in** [this measurable outcome]
> **for** [these users]. **We will know we are right when** [this metric changes
> by this amount within this timeframe].

This is not optional decoration. This is the specification. If you skip this,
you are building blind.

### Define Success Metrics BEFORE Building

Do not retrofit metrics after launch. The moment you decide to build something,
write down:

1. **The outcome metric** — what user behavior will change?
2. **The current baseline** — what is the metric today?
3. **The target** — what value constitutes success?
4. **The timeframe** — by when?

If you cannot fill in all four, you are not ready to build.

### Before and After: Output vs. Outcome Framing

#### Example 1: Notifications

**Output framing (before):**

```
User Story: As a user, I want to receive notifications so that I am informed
            about upcoming events.

Acceptance Criteria:
- System sends push notifications
- User can configure notification preferences
- Notifications appear in the notification center

Done when: Notification system is deployed and sends messages.
```

**Outcome framing (after):**

```
Hypothesis: We believe that sending appointment reminders 24 hours before
            a scheduled event will reduce missed appointments by 40% for
            active users.

Success Metric: Missed appointment rate
Baseline:       23% of appointments are missed
Target:         Reduce to <=14% (a 40% reduction)
Timeframe:      Within 6 weeks of launch

Acceptance Criteria:
- Users with appointments in the next 24h receive a reminder via their
  preferred channel
- Reminder includes one-tap confirm/reschedule action
- Missed appointment rate is tracked and reported weekly

Done when: Missed appointment rate reaches target, NOT when notifications
           are "shipped."
```

#### Example 2: Search

**Output framing (before):**

```
User Story: As a user, I want a search bar so that I can find content.

Acceptance Criteria:
- Search bar is present on all pages
- Results appear within 2 seconds
- Supports keyword matching

Done when: Search feature is live.
```

**Outcome framing (after):**

```
Hypothesis: We believe that adding full-text search with typo tolerance
            will reduce the average time users spend finding a document
            from 3.2 minutes to under 45 seconds, reducing support
            tickets filed under "can't find X" by 60%.

Success Metric: Avg. document discovery time; "can't find" support tickets
Baseline:       3.2 min avg discovery time; 120 tickets/month
Target:         <45 sec avg; <48 tickets/month
Timeframe:      8 weeks post-launch

Acceptance Criteria:
- Users find target document in <45 sec (measured via analytics)
- "Can't find" support tickets decrease month-over-month
- Search is available on all pages with results in <2 sec

Done when: Discovery time and support ticket targets are met.
```

#### Example 3: Dashboard

**Output framing (before):**

```
User Story: As a manager, I want a dashboard so I can see team metrics.

Acceptance Criteria:
- Dashboard displays velocity, burndown, and cycle time
- Data refreshes every hour
- Exportable to PDF

Done when: Dashboard is deployed.
```

**Outcome framing (after):**

```
Hypothesis: We believe giving managers real-time visibility into cycle time
            bottlenecks will reduce average cycle time by 20% because they
            will identify and unblock stuck work items within 4 hours
            instead of discovering them at standup the next day.

Success Metric: Average cycle time; time-to-unblock for stuck items
Baseline:       Cycle time 8.5 days; stuck items sit 18h avg before action
Target:         Cycle time <=6.8 days; stuck items addressed within 4h
Timeframe:      One quarter after rollout

Acceptance Criteria:
- Managers act on stuck items within 4h (measured by state-change timestamps)
- Cycle time trends downward week-over-week
- Dashboard shows bottleneck indicators, not just raw numbers

Done when: Cycle time target is met, NOT when the dashboard is "live."
```

#### Example 4: Onboarding

**Output framing (before):**

```
User Story: As a new user, I want an onboarding wizard so I can set up my
            account.

Done when: Wizard is shipped with all 5 steps.
```

**Outcome framing (after):**

```
Hypothesis: We believe a guided onboarding flow that gets users to their
            first "aha moment" (creating and sharing their first document)
            within 10 minutes will increase 7-day retention from 22% to 40%.

Success Metric: 7-day retention rate; time to first share
Baseline:       22% 7-day retention; 68% of users never share a document
Target:         40% 7-day retention; 50%+ share within first session
Timeframe:      6 weeks post-launch

Done when: Retention target is met. The wizard is a means, not the goal.
```

---

## Quick Reference

| Concept | Output Thinking | Outcome Thinking |
|---|---|---|
| **What you measure** | Stories completed, features shipped | User behavior changed, metrics moved |
| **Definition of done** | Code deployed to production | Target metric reached |
| **Sprint success** | "We shipped 47 stories" | "Onboarding completion rose from 34% to 61%" |
| **Backlog health** | "We have 200 stories estimated" | "Each item has a hypothesis and target metric" |
| **Velocity** | "We do 38 points per sprint" | "We validated 3 hypotheses this month" |
| **Feature value** | "Users asked for it" | "It will change [behavior] by [amount]" |
| **Waste** | Unfinished work | Shipped features that changed nothing |
| **Planning input** | Stakeholder requests, feature lists | User problems, behavioral data |
| **Retrospective focus** | "What did we deliver?" | "What changed for users?" |
| **Roadmap format** | Feature timeline | Outcome timeline with success criteria |

---

## Common Mistakes

| Mistake | Why It Happens | What to Do Instead |
|---|---|---|
| **Defining metrics after launch** | Team wants to "ship first, measure later" | Write the hypothesis and success metric before writing any code. No metric, no build. |
| **Vanity metrics as outcomes** | Page views or sign-ups feel concrete | Use behavioral metrics: retention, task completion rate, time-to-value, error rate. |
| **Outcome = business metric only** | "Increase revenue by 10%" is too distant from the feature | Tie to a user behavior metric that you believe drives the business metric. Chain them: behavior → user outcome → business outcome. |
| **Skipping the baseline** | "We don't track that yet" | Then your first task is to instrument and measure the baseline. You cannot claim improvement without a starting point. |
| **Confusing output metrics for outcome metrics** | "We shipped 12 features" sounds impressive | Ask: "Did anything change for users?" If you cannot answer, you measured output. |
| **Treating the hypothesis as a formality** | Team writes it down but never revisits | Schedule a review 4-8 weeks post-launch. Did the metric move? If not, the feature failed regardless of code quality. |
| **Building without a falsifiable prediction** | "This will improve the user experience" | Make it specific and falsifiable: "Task completion rate will increase from X% to Y% within Z weeks." |
| **Abandoning outcome thinking under pressure** | "We just need to ship this by Friday" | Deadline pressure is exactly when outcome thinking matters most. Shipping the wrong thing fast is still waste. |
| **One metric per feature** | Team picks a single number | Use a primary metric (the outcome you expect) and a counter-metric (something that should NOT get worse). |

---

## The Waste Test

After any feature ships, apply this test:

1. **Did user behavior change?** If no — the feature is waste.
2. **Did it change in the direction you predicted?** If no — your hypothesis was wrong. Learn from it.
3. **Did it change by the amount you predicted?** If less — the solution is insufficient. Iterate or cut.
4. **Did any counter-metric get worse?** If yes — you created a new problem.

Features that do not change behavior are waste, no matter how well they are
built, no matter how clean the code, no matter how on-time the delivery.

---

## Applying This to Stories Right Now

When you are about to write or refine a user story, use this checklist:

- [ ] The story states a hypothesis, not just a feature description
- [ ] There is a named outcome metric with a current baseline
- [ ] There is a specific, numeric target for that metric
- [ ] There is a timeframe for reaching the target
- [ ] Acceptance criteria include behavioral evidence, not just functional checks
- [ ] "Done" is defined as the metric moving, not the code deploying
- [ ] A counter-metric is identified (what should NOT get worse)
- [ ] A review date is set to check whether the outcome was achieved

If any box is unchecked, the story is not ready to build.

---

## Related Skills

- **[discovery-framing](/skills/discovery-framing)** — Frame the problem space before jumping to solutions; outcome thinking depends on understanding the problem first.
- **[mvp-as-experiment](/skills/mvp-as-experiment)** — Build the smallest thing that tests your hypothesis; outcome thinking tells you WHAT to measure, MVP-as-experiment tells you HOW to test it cheaply.
- **[now-later-never](/skills/now-later-never)** — Prioritize ruthlessly; outcome thinking gives you the criteria for what matters now vs. what can wait.
- **[persona-framing](/skills/persona-framing)** — Know who you are solving for; outcomes are meaningless without a specific user whose behavior you expect to change.
