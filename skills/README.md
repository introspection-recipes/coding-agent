# Skills

Skills are reusable instruction bundles that the agent can load when a task needs specific behavior.

Add a skill as a directory with a `SKILL.md` file:

```text
skills/
  api-review/
    SKILL.md
```

Then reference it from `agents/agent.yaml` when the agent should be allowed to use it.
