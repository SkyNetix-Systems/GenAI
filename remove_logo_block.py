#!/usr/bin/env python3
"""
remove_logo_block.py

Walk a directory tree, open every .ipynb notebook, remove occurrences of the
specific markdown block linking to Pierian Data logo, for example:

___
<a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
___

Features:
 - flexible regex (accepts single/double quotes, small attribute variants, minor whitespace)
 - dry-run mode (reports changes but doesn't write)
 - per-file backups (default .bak next to file) or centralized backup-dir
 - summary output

Defaults:
 - If no folder argument is provided, defaults to:
   D:\SkyNetix\GenAI\Data Science Bootcamp

Usage:
    python remove_logo_block.py "D:\SkyNetix\GenAI\Data Science Bootcamp" --dry-run
    python remove_logo_block.py /path/to/notebooks --backup-dir ./backups
"""

import os
import re
import argparse
import shutil
import nbformat
from datetime import datetime

# ---------------------------
# Configuration / utilities
# ---------------------------

DEFAULT_FOLDER = r"D:\SkyNetix\GenAI\Data Science Bootcamp"  # default path (Windows raw string)

def normalize_source(src):
    """Return a single string for the cell source (nbformat sometimes uses list)."""
    if src is None:
        return ""
    if isinstance(src, list):
        return "".join(src)
    return str(src)

def build_regex():
    """
    Build a regex to match the logo block, allowing small variations:
    - single or double quotes
    - optional whitespace/newlines
    - optional trailing slash in img tag
    - relative path like ../../Pierian_Data_Logo.png
    - tolerates extra attributes inside img tag (e.g. alt, title)
    """
    pattern = r"""
    ___                       # starting underscores line
    [ \t\f\v]*\r?\n?          # optional whitespace/newline(s)
    <a\s+href\s*=\s*(?P<q1>['"])http://www\.pieriandata\.com(?P=q1)\s*>   # anchor start with href
    [ \t]*                    # optional spaces
    (<img                     # img tag starts
        [^>]*?                # any attributes (non-greedy)
        src\s*=\s*(?P<q2>['"])\.{0,2}/\.{0,2}Pierian_Data_Logo\.png(?P=q2)  # src with ../../ or ../ or ./ or no dots
        [^>]*?                # any other attributes
    \s*/?>)                   # close img tag (allow self-closing or standard)
    [ \t]*                    # optional spaces
    </a>                      # anchor close
    [ \t\f\v]*\r?\n?          # optional whitespace/newline(s)
    ___                       # ending underscores line
    """
    return re.compile(pattern, re.IGNORECASE | re.DOTALL | re.VERBOSE)

def remove_block_from_markdown(source, regex):
    """
    Remove all occurrences of the pattern from a markdown source string.
    Returns (new_source, number_of_replacements)
    """
    new_source, n = regex.subn("", source)
    return new_source, n

# ---------------------------
# Notebook processing
# ---------------------------

def process_notebook(path, regex, backup_dir=None, make_backup=True, dry_run=False, verbose=False):
    """
    Process a single notebook file.
    Returns (modified:bool, total_replacements:int)
    """
    try:
        nb = nbformat.read(path, as_version=4)
    except Exception as e:
        print(f"[ERROR] failed to read {path}: {e}")
        return False, 0

    total_replacements = 0
    changed = False

    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "markdown":
            src = normalize_source(cell.get("source"))
            new_src, n = remove_block_from_markdown(src, regex)
            if n > 0 and new_src != src:
                total_replacements += n
                changed = True
                cell["source"] = new_src  # safe to set as string

    if changed:
        if dry_run:
            if verbose:
                print(f"[DRY-RUN] Would modify: {path} (remove {total_replacements} occurrence{'s' if total_replacements != 1 else ''})")
            return True, total_replacements

        # create backup
        if make_backup:
            try:
                if backup_dir:
                    os.makedirs(backup_dir, exist_ok=True)
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    backup_fname = os.path.basename(path) + f".{timestamp}.bak"
                    backup_path = os.path.join(backup_dir, backup_fname)
                else:
                    backup_path = path + ".bak"
                shutil.copy2(path, backup_path)
                if verbose:
                    print(f"[BACKUP] {path} -> {backup_path}")
            except Exception as e:
                print(f"[WARNING] could not backup {path} -> {backup_path}: {e}")

        # write notebook back
        try:
            nbformat.write(nb, path)
            if verbose:
                print(f"[MODIFIED] Wrote changes to {path} (removed {total_replacements})")
        except Exception as e:
            print(f"[ERROR] failed to write {path}: {e}")
            return False, total_replacements

    return changed, total_replacements

# ---------------------------
# CLI / Main
# ---------------------------

def main():
    p = argparse.ArgumentParser(description="Remove PierianData logo block from Jupyter notebooks in a folder tree.")
    p.add_argument("folder", nargs="?", default=DEFAULT_FOLDER,
                   help=f"Root folder to scan for .ipynb files (default: {DEFAULT_FOLDER})")
    p.add_argument("--dry-run", action="store_true", help="Do not modify files; only report what would change")
    p.add_argument("--no-backup", action="store_true", help="Do not create backups (not recommended)")
    p.add_argument("--backup-dir", default=None, help="Directory to store backups (if not specified, per-file .bak next to notebook)")
    p.add_argument("--ext", default=".ipynb", help="File extension to consider (default .ipynb)")
    p.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = p.parse_args()

    folder = args.folder
    if not os.path.isdir(folder):
        print(f"[ERROR] folder not found: {folder}")
        return 2

    regex = build_regex()

    total_files = 0
    modified_files = 0
    total_replacements = 0
    changed_files = []

    print(f"Scanning folder: {folder}")
    print(f"Options: dry_run={args.dry_run}, backup_dir={args.backup_dir}, no_backup={args.no_backup}, verbose={args.verbose}")
    print("Starting scan...\n")

    for root, dirs, files in os.walk(folder):
        for fname in files:
            if not fname.lower().endswith(args.ext.lower()):
                continue
            total_files += 1
            path = os.path.join(root, fname)
            changed, n = process_notebook(
                path,
                regex,
                backup_dir=args.backup_dir,
                make_backup=not args.no_backup,
                dry_run=args.dry_run,
                verbose=args.verbose,
            )
            if changed:
                modified_files += 1
                total_replacements += n
                changed_files.append((path, n))
                mode = "DRY" if args.dry_run else "MODIFIED"
                print(f"{mode}: {path}  (removed {n} occurrence{'s' if n!=1 else ''})")

    print("\n=== Summary ===")
    print(f"Scanned files: {total_files}")
    print(f"Files changed: {modified_files}")
    print(f"Total occurrences removed: {total_replacements}")
    if args.dry_run and modified_files > 0:
        print("Tip: Re-run without --dry-run to apply the changes.")
    if modified_files == 0:
        print("No matches found. Notebook contents unchanged.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
