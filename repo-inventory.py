#!/usr/bin/env python3
"""
repo-inventory.py — Enumerate Markdown files in a documentation repository
and emit a CSV suitable for content analysis.

Node IDs (column B) are computed from .nav.yml nav order for awesome-nav
repos, giving hierarchical codes like A01, A03-B02, A03-B05-C01.  For other
nav formats the column is left blank for manual assignment.

Usage:
    python repo-inventory.py [--repo REPO_KEY] [--no-url-check]

Add entries to REPOS below to support other Kubernetes doc sets.
"""

import argparse
import csv
import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required:  pip install pyyaml")

try:
    import requests as _requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

# ---------------------------------------------------------------------------
# Repository profiles
# ---------------------------------------------------------------------------
# nav_format options:
#   "awesome-nav"  — reads .nav.yml files (mkdocs-awesome-nav plugin)
#   "mkdocs"       — reads nav: section in top-level mkdocs.yml
#   "hugo"         — sorts by weight: in front matter, then filename
#   "filesystem"   — alphabetical os.walk order, no node IDs
# ---------------------------------------------------------------------------

REPOS = {
    "kubevirt": {
        "name": "user-guide",
        "local_path": "/home/brucehamilton/github/cncf/kubevirt/user-guide/docs",
        "base_url": "https://kubevirt.io/user-guide",
        "nav_format": "awesome-nav",
        "output_csv": "kubevirt-analysis.csv",
    },
    # ── Add other Kubernetes / CNCF doc repos below ──────────────────────
    #
    # "kubernetes": {
    #     "name": "kubernetes-docs",
    #     "local_path": "/path/to/kubernetes/website/content/en",
    #     "base_url": "https://kubernetes.io/docs",
    #     "nav_format": "hugo",
    #     "output_csv": "kubernetes-analysis.csv",
    # },
    # "gateway-api": {
    #     "name": "gateway-api",
    #     "local_path": "/path/to/gateway-api/site-src",
    #     "base_url": "https://gateway-api.sigs.k8s.io",
    #     "nav_format": "mkdocs",
    #     "output_csv": "gateway-api-analysis.csv",
    # },
    # "istio": {
    #     "name": "istio",
    #     "local_path": "/path/to/istio.io/content/en",
    #     "base_url": "https://istio.io/latest/docs",
    #     "nav_format": "hugo",
    #     "output_csv": "istio-analysis.csv",
    # },
    # "cert-manager": {
    #     "name": "cert-manager",
    #     "local_path": "/path/to/cert-manager/website/content",
    #     "base_url": "https://cert-manager.io/docs",
    #     "nav_format": "hugo",
    #     "output_csv": "cert-manager-analysis.csv",
    # },
}

DEFAULT_REPO = "kubevirt"

# Letters used to build hierarchical node IDs (A=depth-0, B=depth-1, …)
_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ---------------------------------------------------------------------------
# Navigation parsing — awesome-nav (.nav.yml)
# ---------------------------------------------------------------------------

def _read_nav_yml(directory: Path) -> list:
    """Return the raw 'nav' list from .nav.yml, or [] if absent."""
    nav_path = directory / ".nav.yml"
    if not nav_path.exists():
        return []
    with open(nav_path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return (data or {}).get("nav", [])


def _flatten_nav_entries(entries: list) -> list[str]:
    """
    Flatten an awesome-nav entry list into a plain list of file/dir names.

    Handles:
      - Plain strings:           "installation.md"
      - Labeled file entries:    {"Activating feature gates": "activating_feature_gates.md"}
      - Labeled inline groups:   {"ARM cluster": ["device_status.md", "operations.md"]}
      - Labeled subdir entries:  {"Hotplug": "hotplug"}

    Labeled inline groups are expanded in-place so the files remain siblings
    in the same directory at the same nav depth.
    """
    result = []
    for entry in entries:
        if isinstance(entry, str):
            result.append(entry)
        elif isinstance(entry, dict):
            for _label, target in entry.items():
                if isinstance(target, str):
                    result.append(target)
                elif isinstance(target, list):
                    result.extend(_flatten_nav_entries(target))
    return result


def build_node_ids(docs_root: Path, nav_format: str) -> dict[str, str]:
    """
    Walk .nav.yml files and return {relative_path → node_id}.

    Node IDs encode the navigation hierarchy:
      depth-0 top-level entries   →  A00, A01, A02, …
      depth-1 inside a section    →  A03-B00, A03-B01, …
      depth-2 inside a subsection →  A03-B05-C00, A03-B05-C01, …

    A directory entry (section) receives the node that corresponds to its
    own position in the parent nav list (e.g. A03).  Its children then
    start at A03-B00.  This makes the section placeholder explicit so the
    writer knows to add an overview page for it.

    Files not listed in any .nav.yml receive no node ID (left blank).
    """
    if nav_format != "awesome-nav":
        return {}

    node_ids: dict[str, str] = {}

    def _seg(depth: int, idx: int) -> str:
        letter = _ALPHA[depth] if depth < len(_ALPHA) else f"?{depth}"
        return f"{letter}{idx:02d}"

    def _walk(directory: Path, parent_node: str, depth: int):
        raw = _read_nav_yml(directory)
        names = _flatten_nav_entries(raw) if raw else sorted(
            p.name for p in directory.iterdir()
            if p.suffix == ".md" or (p.is_dir() and not p.name.startswith("."))
        )

        for idx, name in enumerate(names):
            target = directory / name
            seg = _seg(depth, idx)
            node = f"{parent_node}-{seg}" if parent_node else seg

            if target.is_dir():
                # The directory itself gets a node (section placeholder)
                rel_dir = str(target.relative_to(docs_root)) + "/"
                node_ids[rel_dir] = node
                _walk(target, node, depth + 1)
            elif target.suffix == ".md" and target.exists():
                rel = str(target.relative_to(docs_root))
                node_ids[rel] = node
            # else: label-only or missing file — skip silently

    _walk(docs_root, "", 0)
    return node_ids


# ---------------------------------------------------------------------------
# Markdown analysis
# ---------------------------------------------------------------------------

_FRONT_MATTER_RE = re.compile(r"^---[ \t]*\n(.*?)\n---[ \t]*\n", re.DOTALL)
_HEADING_RE      = re.compile(r"^(#{1,6})\s+(.+)", re.MULTILINE)
_FENCE_OPEN_RE   = re.compile(r"^```(\S*)")
_IMAGE_RE        = re.compile(r"!\[.*?\]\(.*?\)")
_LINK_HREF_RE    = re.compile(r"\[.+?\]\(([^)]+)\)")
_ADMONITION_RE   = re.compile(r"^(?:!!!|\?\?\?)\s+\w", re.MULTILINE)

# ---------------------------------------------------------------------------
# Content-type classification (Diátaxis)
# ---------------------------------------------------------------------------

_CT_TUTORIAL_TITLE = re.compile(
    r"\b(tutorial|quickstart|quick[\s\-]start|getting[\s\-]started|walkthrough)\b",
    re.IGNORECASE,
)
_CT_TUTORIAL_BODY = re.compile(
    r"\b(you will learn|by the end|prerequisites|what you.ll need|learning objectives)\b",
    re.IGNORECASE,
)
_CT_HOWTO_HEADING = re.compile(
    r"\b(how[\s\-]to|install|configur|set[\s\-]up|setting[\s\-]up|creat|enabl|disabl"
    r"|deploy|migrat|upgrad|connect|hotplug|initiat|cancel|start|stop"
    r"|generat|export|import|backup|restor|add(?:ing)?|remov|delet)\b",
    re.IGNORECASE,
)
_CT_EXPLANATION_HEADING = re.compile(
    r"\b(understand|overview|concept|introduction|background|architecture"
    r"|how\s+\w+\s+works?|why\b|about\b|what\s+is\b|in[\s\-]depth|internals|strateg)\b",
    re.IGNORECASE,
)
_CT_REFERENCE_HEADING = re.compile(
    r"\b(reference|api\b|spec(?:ification)?|parameter|field|option|flag"
    r"|syntax|schema|glossary|limitation|status|condition)\b",
    re.IGNORECASE,
)


def classify_content_type(title: str, headings: list[str], body: str) -> str:
    """
    Return the most prominent Diátaxis content type:
    Tutorial, How-to, Explanation, or Reference.

    Scores each type from heading text and body signals and returns the winner.
    Defaults to How-to when signals are absent (most common in Kubernetes docs).
    """
    scores: dict[str, int] = {"Tutorial": 0, "How-to": 0, "Explanation": 0, "Reference": 0}

    # Tutorial
    if _CT_TUTORIAL_TITLE.search(title):
        scores["Tutorial"] += 4
    if _CT_TUTORIAL_BODY.search(body):
        scores["Tutorial"] += 3

    # How-to — count imperative/task headings (cap contribution)
    howto_hits = sum(1 for h in headings if _CT_HOWTO_HEADING.search(h))
    scores["How-to"] += min(howto_hits, 5)
    if re.search(r"\bhow[\s\-]to\b", title, re.IGNORECASE):
        scores["How-to"] += 2

    # Explanation
    explanation_hits = sum(1 for h in [title] + headings if _CT_EXPLANATION_HEADING.search(h))
    scores["Explanation"] += min(explanation_hits * 2, 8)

    # Reference — headings + markdown tables
    ref_hits = sum(1 for h in [title] + headings if _CT_REFERENCE_HEADING.search(h))
    scores["Reference"] += min(ref_hits * 2, 8)
    table_rows = len(re.findall(r"^\|", body, re.MULTILINE))
    if table_rows >= 6:
        scores["Reference"] += 3
    elif table_rows >= 2:
        scores["Reference"] += 1

    # Tiebreak How-to vs Explanation: numbered steps tip toward How-to
    if scores["How-to"] == scores["Explanation"]:
        if len(re.findall(r"^\d+\.", body, re.MULTILINE)) >= 3:
            scores["How-to"] += 1

    best = max(scores, key=lambda k: scores[k])
    return best if scores[best] > 0 else "How-to"


def analyze_markdown(filepath: Path) -> dict:
    """
    Parse a Markdown file and return a dict of analysis fields.

    Fields returned
    ---------------
    front_title, linktitle, description, weight   — from YAML front matter
    h1_title                                       — first # heading in body
    lines                                          — total line count
    word_count                                     — prose words (code stripped)
    h2_count, h3_count                             — section heading counts
    code_block_count                               — number of fenced blocks
    code_languages                                 — sorted list of languages
    image_count                                    — inline image references
    internal_link_count, external_link_count       — link breakdown
    has_admonition                                 — !!! or ??? present
    """
    out = dict(
        front_title="", linktitle="", description="", weight="",
        h1_title="",
        headings=[],   # all heading texts (H1–H6), used for content-type classification
        body="",       # body text after front matter, used for content-type classification
        lines=0, word_count=0,
        h2_count=0, h3_count=0,
        code_block_count=0, code_languages=[],
        image_count=0, internal_link_count=0, external_link_count=0,
        has_admonition=False,
    )

    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception as exc:
        print(f"  ✗ read error {filepath}: {exc}")
        return out

    # --- YAML front matter ---
    fm_match = _FRONT_MATTER_RE.match(text)
    body = text[fm_match.end():] if fm_match else text
    out["body"] = body
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1)) or {}
            out["front_title"] = str(fm.get("title",       "")).strip()
            out["linktitle"]   = str(fm.get("linktitle",   "")).strip()
            out["description"] = str(fm.get("description", "")).strip()
            w = fm.get("weight", "")
            out["weight"] = str(w) if w != "" else ""
        except yaml.YAMLError:
            pass

    # --- Line count (whole file) ---
    out["lines"] = text.count("\n")

    # --- Headings (in body only) ---
    for m in _HEADING_RE.finditer(body):
        level = len(m.group(1))
        heading_text = m.group(2).strip()
        out["headings"].append(heading_text)
        if level == 1 and not out["h1_title"]:
            out["h1_title"] = heading_text
        elif level == 2:
            out["h2_count"] += 1
        elif level == 3:
            out["h3_count"] += 1

    # --- Code blocks: count, collect languages, build prose text ---
    in_block = False
    langs = []
    prose_lines = []
    for line in body.splitlines():
        stripped = line.strip()
        m = _FENCE_OPEN_RE.match(stripped)
        if m and not in_block:
            in_block = True
            lang = m.group(1).strip()
            if lang:
                langs.append(lang)
            out["code_block_count"] += 1
            continue
        if stripped == "```" and in_block:
            in_block = False
            continue
        if not in_block:
            prose_lines.append(line)

    out["code_languages"] = sorted(set(langs))
    out["word_count"] = len(" ".join(prose_lines).split())

    # --- Images and links ---
    out["image_count"] = len(_IMAGE_RE.findall(body))
    for href in _LINK_HREF_RE.findall(body):
        if href.startswith(("http://", "https://")):
            out["external_link_count"] += 1
        else:
            out["internal_link_count"] += 1

    # --- Admonitions (MkDocs material !!! note / ??? warning …) ---
    out["has_admonition"] = bool(_ADMONITION_RE.search(body))

    return out


# ---------------------------------------------------------------------------
# URL validation
# ---------------------------------------------------------------------------

def check_url(url: str) -> str:
    """Return HTTP status as a string, or 'err' on connection failure."""
    if not HAS_REQUESTS:
        return ""
    try:
        r = _requests.head(url, timeout=8, allow_redirects=True)
        if r.status_code >= 400:
            print(f"  ✗ HTTP {r.status_code}  {url}")
        return str(r.status_code)
    except Exception as exc:
        print(f"  ✗ err  {url}  ({exc})")
        return "err"


# ---------------------------------------------------------------------------
# Core inventory builder
# ---------------------------------------------------------------------------

def _make_hyperlink(url: str) -> str:
    return f'=HYPERLINK("{url}","link")'


def _build_url(base_url: str, rel_path: str) -> str:
    p = Path(rel_path)
    stem = p.stem.lower()
    parent = p.parent
    if str(parent) == ".":
        return f"{base_url}/{stem}"
    return f"{base_url}/{parent}/{stem}"


def _node_sort_key(node: str) -> tuple:
    """Sort key that orders nodes hierarchically: A00 < A01 < A01-B00 < A02."""
    if not node:
        return ("ZZ",)
    return tuple(node.split("-"))


def inventory(repo_key: str, url_check: bool = False) -> list[dict]:
    profile   = REPOS[repo_key]
    docs_root = Path(profile["local_path"])
    base_url  = profile["base_url"]
    repo_name = profile["name"]
    nav_fmt   = profile.get("nav_format", "filesystem")

    print(f"Scanning  {docs_root}")
    node_ids = build_node_ids(docs_root, nav_fmt)
    print(f"Nav map:  {len(node_ids)} entries")

    rows = []
    for dirpath, dirnames, filenames in os.walk(docs_root):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith("."))
        for filename in sorted(filenames):
            if not filename.endswith(".md"):
                continue

            filepath = Path(dirpath) / filename
            rel      = str(filepath.relative_to(docs_root))
            analysis = analyze_markdown(filepath)

            node       = node_ids.get(rel, "")
            topic_url  = _build_url(base_url, rel)
            hyperlink  = _make_hyperlink(topic_url)
            http_status = check_url(topic_url) if url_check else ""

            title   = analysis["front_title"] or analysis["h1_title"]
            snippets = " ".join(analysis["code_languages"])
            content_type = classify_content_type(
                title, analysis["headings"], analysis["body"]
            )

            rows.append({
                "repo":                repo_name,
                "node":                node,
                "link":                hyperlink,
                "path":                rel,
                "title or task":       title,
                "content type":        content_type,
                "task priority":       "",
                "linktitle":           analysis["linktitle"],
                "description":         analysis["description"],
                "weight":              analysis["weight"],
                "lines":               analysis["lines"],
                "word_count":          analysis["word_count"],
                "h2_sections":         analysis["h2_count"],
                "h3_sections":         analysis["h3_count"],
                "code_blocks":         analysis["code_block_count"],
                "snippets":            snippets,
                "images":              analysis["image_count"],
                "internal_links":      analysis["internal_link_count"],
                "external_links":      analysis["external_link_count"],
                "has_admonition":      "yes" if analysis["has_admonition"] else "",
                "http_status":         http_status,
                "notes":               "",
            })

    # Sort: nav-ordered files first (by node hierarchy), then unlisted files by path
    rows.sort(key=lambda r: (_node_sort_key(r["node"]), r["path"]))

    print(f"Found     {len(rows)} topics")
    return rows


# ---------------------------------------------------------------------------
# CSV output
# ---------------------------------------------------------------------------

FIELDNAMES = [
    "repo", "node", "link", "path",
    "title or task", "content type", "task priority",
    "linktitle", "description", "weight",
    "lines", "word_count", "h2_sections", "h3_sections",
    "code_blocks", "snippets", "images",
    "internal_links", "external_links",
    "has_admonition", "http_status",
    "notes",
]


def write_csv(rows: list[dict], output_path: str):
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Written → {output_path}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--repo", default=DEFAULT_REPO, choices=list(REPOS.keys()),
        help=f"Repository profile to scan (default: {DEFAULT_REPO})",
    )
    parser.add_argument(
        "--no-url-check", action="store_true",
        help="Skip HTTP HEAD requests (much faster)",
    )
    args = parser.parse_args()

    profile = REPOS[args.repo]
    rows    = inventory(args.repo, url_check=not args.no_url_check)
    write_csv(rows, profile["output_csv"])


if __name__ == "__main__":
    main()

