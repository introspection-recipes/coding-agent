# template-starter

The template a new coding agent Recipe is created from.

**This repository is a template, not a Recipe.** It does not run, and
`recipe check` does not pass on it — the manifest under `template/.introspection/`
names no Runtime until it is rendered. What CI proves instead is that every
case in `tests/cases.yaml` renders to a Recipe that *is* valid.

## Layout

```
template.yaml          the variables, their types, defaults and prompts
template/              the payload, and the only thing rendered
tests/cases.yaml       render these, then check the output
```

Inside `template/`, a file ending `.tmpl` is rendered and loses the suffix.
Every other file is copied byte for byte, which is how `SYSTEM.md` keeps any
braces it needs: a prompt is mostly the kind of text a renderer would
otherwise eat. Paths render too, so a token names a file as readily as it
fills one.

## Using it

```bash
introspection init my-agent --template template-starter
```

## Changing it

Add a variable to `template.yaml`, reference it in any `.tmpl` file, and add a
case to `tests/cases.yaml` covering it. An undeclared token in a `.tmpl` file
fails the build rather than rendering empty.
