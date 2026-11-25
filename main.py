#!/usr/bin/env python3
"""Invent a Word We Need — entry program.

Coins one new English word and writes it, with a one-line definition,
to /output/entry.txt. The whole entry must be 1-140 characters, a single
line, and not only whitespace (the bounty gate).
"""

from pathlib import Path

WORD = "buzzghost"
DEFINITION = "the phantom buzz you feel in your pocket from a phone that isn't ringing."
ENTRY = f"{WORD} \u2014 {DEFINITION}"


def build_entry() -> str:
    """Return the single-line entry text."""
    return ENTRY


def check_entry(text: str) -> None:
    """Enforce the bounty gate before writing anything out."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # The coined word itself must be one pronounceable token: letters only.
    head = text.split(" ", 1)[0]
    if not head.isalpha() or not head.islower():
        raise ValueError("coined word must be a single lowercase word")


def main() -> None:
    text = build_entry()
    check_entry(text)
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text + "\n", encoding="utf-8")
    # Read it back and re-check what actually landed on disk.
    written = out_path.read_text(encoding="utf-8")
    check_entry(written.rstrip("\n"))
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
