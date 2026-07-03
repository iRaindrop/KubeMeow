#!/usr/bin/env python3
import argparse
import csv
import os
import re
from pathlib import Path


DEFAULT_LOCAL_PATH = "/home/brucehamilton/github/flatcar-refactor/content/docs/latest"
DEFAULT_INPUT_CSV = "add-h1-headings.csv"
DEFAULT_OUTPUT_CSV = "missing_h1_headings.csv"


def add_missing_h1_headings(local_path=DEFAULT_LOCAL_PATH, input_csv=DEFAULT_INPUT_CSV):
    updated_files = 0
    skipped_files = 0

    with open(input_csv, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            rel_or_abs_path = (row.get("path") or "").strip()
            if os.path.isabs(rel_or_abs_path):
                filepath = rel_or_abs_path
            else:
                filepath = os.path.join(local_path, rel_or_abs_path)

            meta_title = (row.get("meta-title") or "").strip()
            new_h1 = (row.get("new-h1") or "").strip()

            if not os.path.exists(filepath):
                print(f"File not found: {filepath}. Skipping.")
                skipped_files += 1
                continue

            if not new_h1:
                print(f"No new-h1 found for {filepath}. Skipping.")
                skipped_files += 1
                continue

            with open(filepath, "r+", encoding="utf-8") as f:
                content = f.read()
                lines = content.splitlines(keepends=True)

                if not lines or lines[0].strip() != "---":
                    print(f"No front matter delimiter found at top of {filepath}. Skipping.")
                    skipped_files += 1
                    continue

                closing_idx = None
                for i in range(1, len(lines)):
                    if lines[i].strip() == "---":
                        closing_idx = i
                        break

                if closing_idx is None:
                    print(f"No closing front matter delimiter found in {filepath}. Skipping.")
                    skipped_files += 1
                    continue

                changed = False

                if meta_title:
                    title_idx = None
                    for i in range(1, closing_idx):
                        if re.match(r"^\s*title\s*:\s*", lines[i], flags=re.IGNORECASE):
                            title_idx = i

                    if title_idx is not None:
                        current_title = lines[title_idx].split(":", 1)[1].strip().strip('"').strip("'")
                        if current_title != meta_title:
                            lines[title_idx] = f"title: {meta_title}\n"
                            changed = True

                body_start = closing_idx + 1
                body_lines = lines[body_start:]

                # Check the full body (outside fenced code blocks) for any existing H1.
                has_existing_h1 = False
                in_code_fence = False
                for line in body_lines:
                    stripped = line.strip()

                    if stripped.startswith("```") or stripped.startswith("~~~"):
                        in_code_fence = not in_code_fence
                        continue

                    if in_code_fence:
                        continue

                    if re.match(r"^#\s+\S", stripped):
                        has_existing_h1 = True
                        break

                if not has_existing_h1:
                    while body_lines and body_lines[0].strip() == "":
                        body_lines.pop(0)

                    heading_line = f"# {new_h1}\n"
                    lines = lines[:body_start] + ["\n", heading_line, "\n"] + body_lines
                    changed = True

                if changed:
                    f.seek(0)
                    f.write("".join(lines))
                    f.truncate()
                    updated_files += 1
                    print(f"Updated: {filepath}")
                else:
                    skipped_files += 1
                    print(f"No changes needed: {filepath}")

    print(f"Completed. Updated: {updated_files}, Skipped: {skipped_files}")


def find_missing_h1_headings(local_path=DEFAULT_LOCAL_PATH, output_csv=DEFAULT_OUTPUT_CSV):
    fix_data = []
    missing_h1_files = 0

    for dirpath, _, filenames in os.walk(local_path):
        for filename in filenames:
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    found_h1 = False
                    title = ""
                    in_code_fence = False

                    for line in lines:
                        stripped = line.strip()

                        if stripped.startswith("```") or stripped.startswith("~~~"):
                            in_code_fence = not in_code_fence
                            continue

                        if in_code_fence:
                            continue

                        if stripped.startswith("title:"):
                            title = line.split(":", 1)[1].strip()
                        elif re.match(r"^#\s+\S", stripped):
                            found_h1 = True
                            break

                    if not found_h1:
                        fix_data.append(
                            {
                                "path": str(Path(filepath).resolve().relative_to(Path(local_path).resolve())),
                                "filename": filename,
                                "meta-title": title,
                                "new-h1": "",
                            }
                        )
                        missing_h1_files += 1
            except Exception as e:
                print(f"Error reading file {filepath}: {e}")

    print(f"Total files missing H1 headings: {missing_h1_files}")
    fieldnames = ["path", "filename", "meta-title", "new-h1"]

    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(fix_data)

    print(f"Wrote results to: {output_csv}")


def main():
    parser = argparse.ArgumentParser(description="Find and add missing H1 headings in Markdown files.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    find_parser = subparsers.add_parser("find", help="Find Markdown files missing H1 headings.")
    find_parser.add_argument("--local-path", default=DEFAULT_LOCAL_PATH, help="Root docs directory to scan.")
    find_parser.add_argument("--output-csv", default=DEFAULT_OUTPUT_CSV, help="CSV file to write scan results.")

    add_parser = subparsers.add_parser("add", help="Add missing H1 headings from a CSV input file.")
    add_parser.add_argument("--local-path", default=DEFAULT_LOCAL_PATH, help="Root docs directory.")
    add_parser.add_argument("--input-csv", default=DEFAULT_INPUT_CSV, help="CSV input containing path/meta-title/new-h1.")

    args = parser.parse_args()

    if args.command == "find":
        find_missing_h1_headings(local_path=args.local_path, output_csv=args.output_csv)
    elif args.command == "add":
        add_missing_h1_headings(local_path=args.local_path, input_csv=args.input_csv)


if __name__ == "__main__":
    main()
