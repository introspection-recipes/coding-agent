"""Render every declared case and validate the Recipe it produces.

The template is not a Recipe, so `recipe check` has nothing to run against
here. What matters is the output, for every combination of variables anyone
can ask for rather than the one a maintainer happened to try.
"""

from __future__ import annotations

import sys

import yaml
from introspection_recipe_check import check_template_cases, load_recipe_dir


def main() -> int:
    snapshot = load_recipe_dir(".")
    cases = yaml.safe_load(open("tests/cases.yaml", encoding="utf-8"))["cases"]
    failed = 0
    for result in check_template_cases(snapshot, cases):
        if result.valid:
            print(f"ok   {result.name} ({len(result.rendered['files'])} files)")
            continue
        failed += 1
        print(f"FAIL {result.name}")
        for diagnostic in result.report.diagnostics:
            print(f"       {diagnostic.code} {diagnostic.path}: {diagnostic.message}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
