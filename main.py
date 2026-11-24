#!/usr/bin/env python3
"""Loading Screen Gold: writes one loading-screen tip to /output/entry.txt.

The tip is a single line for stressed developers and AI coding agents:
the agent fixes the bug fast, nobody knows how, and the only sane move
is to ship it before it changes its mind.
"""
import os

TIP = "Tip: the agent fixed your bug in 40 seconds. Don't ask how, it doesn't know either. Ship it before it changes its mind."


def main():
    assert 1 <= len(TIP) <= 200, "tip must be 1-200 characters"
    assert TIP == TIP.strip(), "tip must not start or end with whitespace"
    assert "\n" not in TIP, "tip must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
