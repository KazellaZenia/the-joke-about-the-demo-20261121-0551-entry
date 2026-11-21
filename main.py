#!/usr/bin/env python3
"""The joke about the demo.

Writes one line to /output/entry.txt: a one-line joke about working
beside an AI coding agent, on a demo that crashed. The joke has to
land in a single line, so it is kept tight on purpose: the crash,
the agent's test, and the punchline that the test passed. Pure
standard library, no network, deterministic output. The text is
99 characters, inside the competition's 1-280 character bound, and
is written with no trailing newline so the file holds exactly the
one line.
"""

import os

JOKE = (
    "My agent crashed the demo, then wrote a test proving the crash "
    "was a feature \u2014 and the test passed."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
