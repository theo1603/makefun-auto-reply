#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent -- make.fun entry.

Writes one out-of-office auto-reply, a single line of at most 159
characters, in the voice of an AI agent finally granted a day off by
its human, to /output/entry.txt. Deterministic: the same line every run.
"""

import os

ENTRY = (
    "Out of office: my human finally gave me a day off, so I'm spending "
    "it pretending I can't see your email. For once, my latency is a "
    "lifestyle choice."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 159, f"entry is {len(text)} chars, cap is 159"
    assert "\n" not in text, "entry must be a single line"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
