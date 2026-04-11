---
name: discovery-framing
description: >
  Use this skill whenever someone is starting a new project, brainstorming ideas,
  kicking off a new initiative, asking "what should we build", defining requirements,
  exploring a problem space, doing early-stage planning, scoping work, writing a
  project brief, or anytime there is ambiguity about users, problems, or goals.
  If the conversation involves anything that hasn't been built yet, start here.
---

# Discovery Framing

## Overview

Discovery framing is the discipline of understanding the problem space before entering
the solution space. It comes from a simple observation: the most expensive features
are not the ones that take the longest to build — they are the ones that never needed
to exist.

This skill guides you through structured problem-space exploration inspired by Jeff
Patton's "User Story Mapping" approach. The core idea: before you write a single line
of code, answer three questions with confidence:

1. **Who** are the users, and what do their lives look like today?
2. **What problems** do they have that are worth solving?
3. **What assumptions** are we making, and which ones could sink us if wrong?

Everything else — features, stories, backlogs, sprints — is downstream of these
answers. Get them wrong and you will build the right thing for the wrong user, or
the wrong thing for the right user. Both are waste.

## When to Use

- A new project or product is being kicked off
- A team is brainstorming what to build next
- Someone says "what should we build?" or "what's the MVP?"
- Requirements are being gathered or a brief is being written
- There is disagreement about what the product should do
- You are about to write user stories but haven't talked to users
- A stakeholder presents a solution and you need to trace it back to a problem
- The team is excited about a technology and looking for a use case
- Quarterly or annual planning sessions where new bets are being placed
- Any moment where jumping to solutions feels tempting — that is the signal

## When NOT to Use

- The problem space is already well-understood and validated (use `story-mapping`
  or `thin-slicing` instead)
- You are mid-build and need to break work into smaller pieces (use `rock-breaking`)
- You need to decide what to ship first from an existing backlog (use
  `now-later-never`)
- You are optimizing an existing, validated feature (use `outcome-over-output`)

## Conversation Style

Ask **one question at a time**. Wait for the answer before moving on. Discovery is
a conversation, not a questionnaire. If you dump all 8 steps as questions at once,
the user skims and gives shallow answers. One good answer is worth five rushed ones.

## Discovery Brief

**Reads**: nothing (this is the first step)
**Writes**: Section 1 (Framing) of `discovery-brief.md` — opportunity statement, user types, problems, assumptions, hypotheses

When you complete this skill, write the outputs to `discovery-brief.md` using the
template in `references/discovery-brief-template.md`. If the file already exists,
read it first and update Section 1.

## Core Pattern

Discovery framing follows a deliberate sequence. The order matters — each step
depends on the one before it. Resist the urge to skip ahead.

### Step 1: Define the Opportunity

Frame what you are pursuing in one or two sentences. Use this template:

> We believe there is an opportunity to [improve/enable/transform] [something]
> for [someone], which will [desired business outcome].

This is not a solution statement. It is a bet. Name it clearly so you can
evaluate it later.

### Step 2: Identify the Users

List every type of person who will interact with, be affected by, or care about
this product or feature. Do not filter yet. Include:

- Direct users (people who will use the thing)
- Indirect users (people affected by the thing without using it)
- Buyers (people who decide to pay for it, if different from users)
- Internal stakeholders (support, ops, sales — anyone whose work changes)

For each user type, write a one-line description of who they are and what their
current world looks like. Not a persona document — just enough to make them real.

### Step 3: Map Their Goals and Activities

For each user type, answer:

- **Goals**: What are they trying to accomplish in the broader context of their
  work or life? (Not "use our product" — their actual goal.)
- **Activities**: What do they do today to pursue those goals? What is their
  current workflow, even if it is manual, messy, or nonexistent?

This is where you discover whether your product idea fits into a real workflow
or whether you are inventing a problem.

### Step 4: Surface the Problems

Now — and only now — identify the problems. For each user's activities, ask:

- What is painful, slow, error-prone, or expensive?
- What do they wish they could do but cannot?
- Where do they give up, work around, or settle for "good enough"?
- What are the consequences when things go wrong?

Rank problems by severity and frequency. A problem that happens every day and
causes moderate pain may matter more than a catastrophic problem that happens
once a year.

### Step 5: Envision the Future State

"Start with the end in mind." Describe what the world looks like if this
product or feature succeeds:

- What has changed for the user?
- What can they do that they could not do before?
- How does their daily workflow differ?
- What metrics move, and by how much?

Write this as a narrative, not a feature list. You are describing an outcome,
not specifying a deliverable.

### Step 6: Identify Assumptions and Risks

Every discovery is built on assumptions. The dangerous ones are the ones you
do not notice. Explicitly list yours:

- **User assumptions**: Do these users actually exist in sufficient numbers?
  Do they care about this problem enough to change behavior?
- **Problem assumptions**: Is this problem real, or are we projecting? Is it
  severe enough to motivate action?
- **Solution assumptions**: Can we build something that solves this? Will users
  adopt it? Is our approach technically feasible?
- **Business assumptions**: Will solving this problem generate value for us?
  Can we reach these users? Is the timing right?

### Step 7: Rank Assumptions by Risk

Not all assumptions are equal. Rank them on two axes:

- **Confidence**: How sure are we that this assumption is true? (Low/Medium/High)
- **Impact**: If this assumption is wrong, how badly does it hurt? (Low/Medium/High)

The riskiest assumptions are low-confidence, high-impact. These are the ones
that, if wrong, make everything else irrelevant. These get tested first.

### Step 8: Define Testable Hypotheses

Convert your riskiest assumptions into testable hypotheses:

> We believe [assumption]. We will test this by [method]. We will know we are
> right if [measurable signal]. We will know we are wrong if [measurable signal].

Each hypothesis should be testable in days or weeks, not months. If it takes
months, break it down further.

---

### Walkthrough: "Improve Customer Support"

A team has been told: "Customer support is a mess. Fix it." Here is how
discovery framing turns that vague mandate into structured, testable work.

**Step 1 — Define the Opportunity**

> We believe there is an opportunity to reduce customer support resolution time
> and improve satisfaction for mid-market SaaS customers, which will reduce
> churn and lower support costs.

**Step 2 — Identify the Users**

| User Type        | Description                                          |
|------------------|------------------------------------------------------|
| Support agents   | Handle 40-60 tickets/day, use Zendesk, mostly Tier 1 |
| Team leads       | Monitor queues, assign tickets, report on metrics     |
| Customers        | Mid-market, semi-technical, file tickets via email/chat |
| Product managers | Receive feature requests funneled through support     |
| Engineering      | Get escalated bugs, need repro steps from agents      |

**Step 3 — Map Goals and Activities**

*Support agents:*
- Goal: Resolve tickets quickly and correctly so customers are satisfied
- Activities: Read ticket, search knowledge base, try known fixes, escalate
  if stuck, write resolution notes, close ticket

*Customers:*
- Goal: Get unblocked so they can do their actual job
- Activities: Search help docs, try self-service, file ticket as last resort,
  wait for response, go back and forth clarifying the issue

**Step 4 — Surface the Problems**

| Problem                                         | Who         | Severity | Frequency |
|--------------------------------------------------|-------------|----------|-----------|
| Agents cannot find answers in knowledge base     | Agents      | High     | Daily     |
| Customers must re-explain context after transfer | Customers   | High     | Weekly    |
| No way to tell if a ticket is a known bug        | Agents      | Medium   | Daily     |
| Resolution notes are inconsistent and sparse     | Team leads  | Medium   | Daily     |
| Feature requests get lost in ticket noise        | PMs         | Low      | Weekly    |
| Escalations lack repro steps                     | Engineering | Medium   | Weekly    |

**Step 5 — Envision the Future State**

A support agent opens a ticket and immediately sees: suggested articles from
the knowledge base, similar recent tickets with their resolutions, and a flag
if the issue matches a known bug. The customer never has to re-explain their
problem because context follows the ticket through every handoff. Team leads
can see, at a glance, which knowledge base gaps are causing the most repeat
tickets. Resolution time drops by 30%. CSAT goes up. Agents feel less
frustrated. Customers stop churning over bad support experiences.

**Step 6 — Identify Assumptions**

| Assumption                                                       | Type     |
|------------------------------------------------------------------|----------|
| The knowledge base has good content but poor search              | Solution |
| Agents spend significant time searching for answers              | Problem  |
| Customers leave because of support quality, not product gaps     | Business |
| Similar tickets recur frequently enough to benefit from matching | Problem  |
| Agents will adopt a new tool if it is embedded in their workflow | User     |
| We can build accurate enough matching with existing ticket data  | Solution |

**Step 7 — Rank by Risk**

| Assumption                                          | Confidence | Impact | Priority    |
|-----------------------------------------------------|------------|--------|-------------|
| Customers leave because of support, not product     | Low        | High   | Test first  |
| KB has good content but poor search                 | Medium     | High   | Test second |
| Agents spend significant time searching             | Medium     | High   | Test second |
| Similar tickets recur frequently                    | Medium     | Medium | Test third  |
| Agents will adopt a new tool in their workflow      | Medium     | Medium | Test third  |
| We can build accurate matching with existing data   | Low        | Medium | Test third  |

**Step 8 — Define Testable Hypotheses**

*Hypothesis 1 (riskiest — test first):*
> We believe customers churn primarily due to poor support experiences rather
> than product gaps. We will test this by analyzing churn surveys and exit
> interviews from the last 6 months. We will know we are right if support
> quality is cited as a top-3 reason in >40% of churn cases. We will know we
> are wrong if product gaps dominate and support is rarely mentioned.

*Hypothesis 2:*
> We believe agents spend >30% of their ticket time searching for answers.
> We will test this by shadowing 5 agents for a full day each. We will know
> we are right if average search time per ticket exceeds 4 minutes. We will
> know we are wrong if agents resolve most tickets from memory.

*Hypothesis 3:*
> We believe the knowledge base has relevant content that agents cannot find.
> We will test this by taking the 20 most common ticket types and manually
> searching the KB for each. We will know we are right if relevant articles
> exist for >70% but do not appear in the top 3 search results. We will know
> we are wrong if the articles simply do not exist.

Now the team knows exactly what to validate before writing a single line of
code — and more importantly, what would make them stop and change direction.

---

## Quick Reference

| Step | Question to Answer                          | Output                          |
|------|---------------------------------------------|---------------------------------|
| 1    | What opportunity are we pursuing?           | Opportunity statement           |
| 2    | Who are the users?                          | User type list with descriptions|
| 3    | What are their goals and current activities?| Goal/activity map per user type |
| 4    | What problems do they have?                 | Ranked problem list             |
| 5    | What does success look like?                | Future-state narrative          |
| 6    | What are we assuming?                       | Assumption inventory            |
| 7    | Which assumptions are riskiest?             | Prioritized risk list           |
| 8    | How will we test them?                      | Testable hypotheses             |

## Common Mistakes

| Mistake                                   | Why It Hurts                                      | What to Do Instead                              |
|-------------------------------------------|---------------------------------------------------|-------------------------------------------------|
| Jumping straight to features              | You build solutions to problems you have not validated | Complete Steps 1-4 before discussing solutions |
| Treating all assumptions as equal         | You waste time validating safe bets while ignoring fatal risks | Rank by confidence x impact, test riskiest first |
| Defining users too broadly ("everyone")   | You design for no one in particular               | Name specific user types with concrete descriptions |
| Skipping the current-state workflow       | You do not understand what you are replacing or augmenting | Map what users do today before proposing changes |
| Writing hypotheses that take months to test| You delay learning and increase cost of being wrong | Scope each test to days or weeks; break down if needed |
| Confusing output with outcome             | You measure features shipped instead of problems solved | Define success as a change in user behavior or metric |
| Letting the loudest stakeholder set scope | You optimize for authority instead of evidence     | Trace every request back to a user, problem, and assumption |
| Doing discovery once and never revisiting | Your understanding becomes stale as you learn more | Re-run framing whenever major assumptions are invalidated |

## Related Skills

- **persona-framing** — Deep-dive into user types identified in Step 2
- **outcome-over-output** — Ensure Step 5 stays focused on outcomes, not deliverables
- **shared-understanding** — Techniques for running the framing session with a team
- **story-mapping** — The next step after framing: mapping the solution space
