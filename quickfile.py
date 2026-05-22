#!/usr/bin/env python3
"""quickfile – instant file creation with auto‑rename.

Usage examples:
    quickfile new.txt
    quickfile src/__init__.py tests/__init__.py
    quickfile script.py --template python
    quickfile notes.md --template ./my_template.md
"""

import argparse
import pathlib
import sys
from typing import List, Optional

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _next_available_path(path: pathlib.Path) -> pathlib.Path:
    """Return a non‑existing path by appending _N before the suffix.
    If ``path`` does not exist, it is returned unchanged.
    """
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def _load_template(template_arg: str) -> str:
    """Return the template content based on ``template_arg``.
    Built‑in shortcuts are ``python`` and ``markdown``. Otherwise treat the
    argument as a file path to a custom template.
    """
    builtins = {
        "python": "#!/usr/bin/env python3\n\n\"\"\"\nModule description.\n\"\"\"\n\ndef main():
    pass\n\nif __name__ == \"__main__\":
    main()\n",
        "markdown": "---\ntitle: New Document\nauthor: YOUR_NAME\ndate: 2024-01-01\n---\n\n# Introduction\n\nWrite something awesome here.\n",
    }
    if template_arg in builtins:
        return builtins[template_arg]
    # treat as file path
    tpl_path = pathlib.Path(template_arg)
    if not tpl_path.is_file():
        sys.stderr.write(f"Template file '{template_arg}' not found.\n")
        sys.exit(1)
    return tpl_path.read_text(encoding="utf-8")

# ---------------------------------------------------------------------------
# Main CLI logic
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(
        prog="quickfile",
        description="Create files instantly, auto‑renaming on collisions.",
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="One or more file paths to create.",
    )
    parser.add_argument(
        "--template",
        help="Built‑in template name (python, markdown) or path to a custom template file.",
    )
    args = parser.parse_args(argv)

    template_content = None
    if args.template:
        template_content = _load_template(args.template)

    created = []
    for raw_path in args.files:
        target = pathlib.Path(raw_path)
        # Ensure parent directories exist
        target.parent.mkdir(parents=True, exist_ok=True)
        final_path = _next_available_path(target)
        # Write the file (empty or template)
        final_path.write_text(template_content or "", encoding="utf-8")
        created.append(str(final_path))

    print("Created:")
    for p in created:
        print(f"  {p}")


if __name__ == "__main__":
    main()
