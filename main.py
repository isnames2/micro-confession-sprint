#!/usr/bin/env python3
"""Write the unsent micro-confession to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is exactly two parts: a To: line naming who it was meant for,
and the unsent message itself, one line written exactly as it was typed,
with no explanation after it. The whole entry must be 1-260 characters
(the gate for this competition).
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "To: my ex-roommate\n"
    "I still pay for the streaming account we shared "
    "because cancelling it feels like deleting you"
)


def main() -> int:
    # Gate: the whole entry must be 1-260 characters of UTF-8 text.
    assert 1 <= len(ENTRY) <= 260, f"entry is {len(ENTRY)} chars"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
