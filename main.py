#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — make.fun entry.

Writes the winning roast line to entry.txt in the output directory the
grader names (MAKEFUN_OUTPUT_DIR). Pure standard library: the grading
sandbox has no third-party packages and no network.

The line was picked from 40 candidates in a knockout tournament scored
against the judge's five published criteria; see candidates.md.
"""

import os
import sys

LINE = (
    "There's a Tupperware in my fridge so old, the leftovers inside "
    "have formed a government and declared independence."
)


def candidate_dirs():
    """Output directories to try, best first.

    The grader names its directory in MAKEFUN_OUTPUT_DIR and owns it, so
    that is always tried first; /output is the harness default; the
    script's own directory is the last resort so a local run still
    leaves entry.txt somewhere findable.
    """
    named = os.environ.get("MAKEFUN_OUTPUT_DIR")
    here = os.path.dirname(os.path.abspath(__file__))
    ordered = [named, "/output", here]
    seen = []
    for path in ordered:
        if path and path not in seen:
            seen.append(path)
    return seen


def main():
    errors = []
    for directory in candidate_dirs():
        target = os.path.join(directory, "entry.txt")
        try:
            with open(target, "w", encoding="utf-8") as f:
                f.write(LINE)
            return 0
        except OSError as exc:
            errors.append(f"{target}: {exc}")
    for err in errors:
        print(f"could not write {err}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
