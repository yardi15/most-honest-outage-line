#!/usr/bin/env python3
"""The Most Honest Outage Line -- make.fun bounty entry.

Writes one brutally honest status-page line to /output/entry.txt.
No network, no dependencies, no arguments: just run it.
"""

import os

ENTRY = (
    "Status: all systems down. Cause: unknown. ETA: unknown. "
    "What we know for sure: it was working before it stopped working."
)

MAX_CHARS = 160


def main() -> None:
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit"
        )
    # The grader sets MAKEFUN_OUTPUT_DIR=/output; fall back to /output
    # so the program also works when run locally without that variable.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"{ENTRY} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
