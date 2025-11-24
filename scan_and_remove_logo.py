#!/usr/bin/env python3
r"""
scan_and_remove_logo.py

Scan .ipynb notebooks for any occurrences of 'pierian', 'pieriandata' or
'Pierian_Data_Logo.png' in MARKDOWN cells and report context.

Safe workflow:
  1) Run without --remove to inspect matches (recommended).
  2) Run with --remove --backup-dir <dir> to delete matches and keep backups.

Example:
  python scan_and_remove_logo.py "D:\SkyNetix\GenAI\Data Science Bootcamp"
  python scan_and_remove_logo.py "D:\SkyNetix\GenAI\Data Science Bootcamp" --remove --backup-dir "D:\SkyNetix\GenAI\Backups"
"""
import os
import re
import argparse
import shutil
import nbformat
from datetime import datetime
from textwrap import shorten

DEFAULT_FOLDER = r"D:\SkyNetix\GenAI\Data Science Bootcamp"

# A permissive pattern to find anything mentioning pierian / pieriandata or the logo filename
SEARCH_PAT = re.compile(r"(pierian|pieriandata|pierian_data_logo\.png)", re.IGNORECASE)

def normalize_source(src):
    if src is None:
        return ""
    if isinstance(src, list):
        return "".join(src)
    return str(src)

def find_matches_in_notebook(path, pattern):
    """Return list of (cell_index, match_span, snippet) for matches in markdown cells."""
    try:
        nb = nbformat.read(path, as_version=4)
    except Exception as e:
        return None, f"ERROR reading notebook: {e}"

    matches = []
    for idx, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "markdown":
            continue
        src = normalize_source(cell.get("source"))
        for m in pattern.finditer(src):
            start, end = m.span()
            # snippet: a short context around match
            left = max(0, start - 40)
            right = min(len(src), end + 40)
            snippet = src[left:right].replace("\n", " ")
            snippet = shorten(snippet, width=200, placeholder="...")
            matches.append((idx, start, end, snippet))
    return matches, None

def remove_matches_in_notebook(path, pattern, backup_dir=None, verbose=False):
    """Remove all occurrences of pattern from markdown cells. Return count removed."""
    try:
        nb = nbformat.read(path, as_version=4)
    except Exception as e:
        return None, f"ERROR reading notebook: {e}"

    removed_count = 0
    changed = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = normalize_source(cell.get("source"))
        new_src, n = pattern.subn("", src)
        if n > 0:
            cell["source"] = new_src
            removed_count += n
            changed = True

    if not changed:
        return 0, None

    # backup
    if backup_dir is not None:
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = os.path.basename(path) + f".{timestamp}.bak"
        backup_path = os.path.join(backup_dir, backup_name)
    else:
        backup_path = path + ".bak"

    try:
        shutil.copy2(path, backup_path)
    except Exception as e:
        return None, f"WARNING: could not create backup {backup_path}: {e}"

    # write notebook
    try:
        nbformat.write(nb, path)
    except Exception as e:
        return None, f"ERROR writing notebook: {e}"

    return removed_count, None

def main():
    p = argparse.ArgumentParser(description="Scan and optionally remove PierianData logo/text from notebooks.")
    p.add_argument("folder", nargs="?", default=DEFAULT_FOLDER, help="Folder to scan (default provided).")
    p.add_argument("--remove", action="store_true", help="If set, remove matches (after creating backups).")
    p.add_argument("--backup-dir", default=None, help="Folder to store backups (if not set, per-file .bak files next to notebooks).")
    p.add_argument("--ext", default=".ipynb", help="File extension to scan (default .ipynb).")
    p.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = p.parse_args()

    folder = args.folder
    if not os.path.isdir(folder):
        print(f"[ERROR] folder not found: {folder}")
        return 2

    total_files = 0
    files_with_matches = 0
    total_matches = 0
    print(f"Scanning folder: {folder}\n(remove mode = {args.remove})\n")

    for root, dirs, files in os.walk(folder):
        for fname in files:
            if not fname.lower().endswith(args.ext.lower()):
                continue
            total_files += 1
            path = os.path.join(root, fname)
            matches, err = find_matches_in_notebook(path, SEARCH_PAT)
            if err:
                print(f"[ERR] {path}: {err}")
                continue
            if matches:
                files_with_matches += 1
                total_matches += len(matches)
                print(f"--- {path}  (matches: {len(matches)})")
                for (cell_idx, start, end, snippet) in matches:
                    print(f"   cell[{cell_idx}] snippet: {snippet}")
                if args.remove:
                    removed, rerr = remove_matches_in_notebook(path, SEARCH_PAT, backup_dir=args.backup_dir, verbose=args.verbose)
                    if rerr:
                        print(f"   [REMOVE-ERROR] {rerr}")
                    else:
                        print(f"   [REMOVED] {removed} occurrence{'s' if removed!=1 else ''} (backup created)")
                print()
    print("=== Summary ===")
    print(f"Scanned files: {total_files}")
    print(f"Files with matches: {files_with_matches}")
    print(f"Total matches found: {total_matches}")
    if files_with_matches == 0:
        print("No pierian/pieriandata/logo occurrences detected with the permissive search. If you still expect matches, the content might be obfuscated or present in attachments rather than markdown cells.")

if __name__ == "__main__":
    main()
