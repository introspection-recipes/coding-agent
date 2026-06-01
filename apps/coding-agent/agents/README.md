# Agents

Agents are runnable role configs.

`agent.yaml` is the default entrypoint. Add more YAML files when this recipe needs separate roles, such as `reviewer.yaml`, `researcher.yaml`, or `support.yaml`.

Common fields:

- `name`
- `description`
- `model`
- `tools`
- `skills`
- `subagents`
- `requires.extensions`
- `system_instructions`

Use `system_instructions.mode: append` for normal customization. Use `replace` only when the agent should ignore `SYSTEM.md`.
