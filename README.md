# claude-skills

A monorepo of Claude Code skill plugins for engineering practices and product discovery.

## Plugins

### dora-skills (v2.2.0)

Skills and agents for engineering practices that improve [DORA metrics](https://dora.dev/) — Deployment Frequency, Lead Time for Changes, Change Failure Rate, and Mean Time to Restore.

**18 skills** covering TDD, trunk-based development, small PRs, feature flags, observability, contract testing, loose coupling, backward-compatible migrations, and more.

**3 agents:**
- `dora-health-check` — audits a repo and scores all practices
- `dora-review` — reviews working tree changes against DORA practices
- `dora-improve` — targets a specific DORA metric and makes improvements

| Skill | DORA Metric |
|---|---|
| `small-incremental-commits` | Deployment Frequency, Lead Time |
| `trunk-based-development` | Deployment Frequency, Lead Time |
| `feature-flags` | Deployment Frequency |
| `configuration-as-code` | Deployment Frequency |
| `small-pull-requests` | Lead Time |
| `test-driven-development` | Lead Time, Change Failure Rate |
| `dependency-management` | Lead Time, Change Failure Rate |
| `code-review-discipline` | Change Failure Rate |
| `type-safety-and-linting` | Change Failure Rate |
| `contract-testing` | Change Failure Rate |
| `api-versioning` | Change Failure Rate |
| `observability-aware-coding` | Change Failure Rate |
| `backward-compatible-migrations` | Change Failure Rate |
| `structured-logging-and-tracing` | MTTR |
| `loose-coupling` | MTTR |
| `rollback-friendly-design` | MTTR |
| `dora-overview` | Router / entry point |
| `stop-and-clarify` | Cross-cutting |

---

### product-discovery-skills (v1.3.0)

Skills and agents for product discovery and user story mapping, inspired by Jeff Patton's *User Story Mapping*.

**12 skills** covering problem framing, personas, story mapping, walking skeletons, thin slicing, MVP experiments, release planning, and more.

**3 agents:**
- `discovery-health-check` — audits planning artifacts against discovery practices
- `discovery-review` — reviews planning session outputs for gaps
- `discovery-improve` — improves a specific practice area

**Discovery pipeline:**

```
framing -> personas -> story-mapping -> walking-skeleton -> thin-slicing -> mvp-as-experiment -> release-planning
```

Supporting skills load as needed: `outcome-over-output`, `now-later-never`, `rock-breaking`, `shared-understanding`.

## Installation

Add this marketplace to your Claude Code settings:

```json
{
  "extraKnownMarketplaces": {
    "claude-skills": {
      "source": {
        "source": "git",
        "url": "https://github.com/Addzyyy/claude-skills.git"
      }
    }
  }
}
```

Then enable the plugins you want in `enabledPlugins`.

## Structure

```
claude-skills/
├── .claude-plugin/
│   └── marketplace.json
├── dora-skills/
│   ├── skills/    (18 skills)
│   ├── agents/    (3 agents)
│   ├── hooks/
│   └── docs/
└── product-discovery-skills/
    ├── skills/    (12 skills)
    ├── agents/    (3 agents)
    ├── hooks/
    ├── evals/
    ├── references/
    └── scripts/
```

## License

MIT
