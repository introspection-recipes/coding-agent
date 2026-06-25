# Coding Agent Recipe

A Git-backed Introspection recipe for running a customizable Pi coding agent.

Use this repository as a GitHub template when you want to create a new managed runtime recipe. The template starts with one default agent and no additional variants, so the first run is easy to understand and customize.

## What This Is

An Introspection recipe is a package of possible runtime behavior. This repository contains:

- `.introspection/coding-agent.yaml`: the GitOps manifest Introspection discovers.
- `package.json`: the recipe package metadata and Pi resource globs.
- `agents/agent.yaml`: the default runnable agent.
- `SYSTEM.md`: the base system prompt shared by the agent.

When you create a runtime from this repo, Introspection reads the manifest, pins the selected git commit, and launches the default agent from the recipe package.

## Quickstart

1. Click **Use this template** in GitHub.
2. Create a repo in your GitHub account or organization.
3. Open Introspection and choose **New runtime**.
4. Select **From existing recipe**.
5. Pick your new repo and branch.
6. Select `.introspection/coding-agent.yaml`.
7. Create the runtime and open **Preview Agent**.

## Repository Layout

```text
.introspection/
  coding-agent.yaml
README.md
SYSTEM.md
package.json
agents/
  README.md
  agent.yaml
skills/
  README.md
extensions/
  README.md
```

## How It Works

The manifest at `.introspection/coding-agent.yaml` is the registry entry:

```yaml
name: coding-agent
runtime_name: coding-agent
path: .
description: Customizable Pi coding agent
runtime:
  kind: byor
  llm_mode: managed
  allow_hot_swap: false
```

The `path` field points at the recipe package. Inside that package, `agents/agent.yaml` is the default entrypoint.

Add additional `agents/*.yaml` files when you need named variants for experiments, model changes, or alternate entrypoints. Use `from: agent` when a variant should inherit the default agent's shared settings.

## Customize

Edit these files first:

- `SYSTEM.md` for shared behavior and operating rules.
- `agents/agent.yaml` for model, tools, skills, subagents, and role instructions.
- `skills/` for reusable instruction bundles.
- `extensions/` for custom tools or runtime hooks.

## Monorepos

You can keep multiple recipes in one repo. Each manifest in `.introspection/` points at its own package path:

```text
.introspection/
  coding-agent.yaml
  customer-support.yaml
apps/
  coding-agent/
  customer-support/
```

Example manifest:

```yaml
name: customer-support
runtime_name: customer-support
path: apps/customer-support
description: Customer support agent
runtime:
  kind: byor
  llm_mode: managed
```
