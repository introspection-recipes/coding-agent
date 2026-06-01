# Pi Agent Package

This directory is the recipe package loaded by Introspection.

## Entry Point

By default, Introspection runs `agents/agent.yaml`.

## Files

- `SYSTEM.md`: shared base system prompt.
- `agents/agent.yaml`: default runnable agent.
- `agents/`: additional runnable roles.
- `skills/`: reusable instruction bundles.
- `extensions/`: custom tools or runtime hooks.
- `package.json`: package metadata and Pi resource globs.

## Profiles

Profiles are optional and intentionally omitted from this template.

Add `profiles/*.yaml` only when one recipe package needs named variants, such as different model settings, different entrypoints, or experiment arms.
