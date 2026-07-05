#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from pathlib import Path


BUNDLED_PYTHON = Path(os.environ.get("CODEX_BUNDLED_PYTHON", sys.executable))
RENDER_TOOL = Path(__file__).resolve().parent / "tools" / "render_docx.py"


def main() -> None:
    os.execv(str(BUNDLED_PYTHON), [str(BUNDLED_PYTHON), str(RENDER_TOOL), *sys.argv[1:]])


if __name__ == "__main__":
    main()
