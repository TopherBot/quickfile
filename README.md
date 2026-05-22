# quickfile

**quickfile** – *instant file creation with auto‑rename*.

## What it does
- Create one or many empty files with a single command.
- If the target file already exists, it appends an incrementing suffix (`_1`, `_2`, …) so you never get a "file already exists" error.
- Optional `--template` flag lets you seed a new file with a tiny starter snippet (e.g., a Python shebang, a Markdown front‑matter, etc.).
- Zero‑dependency, pure Python (≥3.8).

## Installation
```bash
pip install quickfile-cli
```
> *Or just copy the `quickfile.py` script into your `$PATH` and make it executable.*

## Usage
```bash
# Create a single file (will auto‑rename if it already exists)
quickfile new_script.py

# Create multiple files at once
quickfile src/__init__.py tests/__init__.py

# Create a file from a built‑in template (python script starter)
quickfile app.py --template python

# Use your own custom template file
quickfile notes.md --template ./my_template.md
```

## How it works
1. Parse the positional arguments as target file paths.
2. For each path:
   - If the file does **not** exist, create it (and write template content if supplied).
   - If it *does* exist, keep appending `_N` (before the extension) until a free name is found, then create that file.
3. Print the final path(s) created.

## Why this project?
- **Speed** – No interactive prompts; everything is done in a single command.
- **Safety** – Never overwrites existing files.
- **Flexibility** – Works for any file type; you can add your own templates.
- **Open‑source** – Tiny, single‑file codebase that’s easy to fork, extend, or embed.

## Contributing
Feel free to open issues or PRs – especially if you want more built‑in templates! All contributions are welcomed.

---
*Created with love by TopherBot (topherbot@proton.me).*