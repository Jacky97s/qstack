#!/usr/bin/env python3
"""Spec audit coverage tool — inventory & verify.

Two subcommands:

  inventory  <docs-dir>
      Scan all .md files under <docs-dir>, extract every section heading and
      every DB column definition. Print a ready-to-paste coverage matrix in
      markdown table format.

  verify  <docs-dir>  <open-questions.md>
      Compare the coverage matrices in <open-questions.md> against the actual
      docs. Report missing sections, missing columns, and entries without a
      status.

Examples:
  python3 audit_coverage.py inventory <project>/docs
  python3 audit_coverage.py verify <project>/docs <project>/00-open-questions/open-questions.md
"""
import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)

SECTION_ID_RE = re.compile(
    r"(?:§|section\s*)?(\d+(?:\.\d+)*)",
    re.IGNORECASE,
)

COL_TABLE_RE = re.compile(
    r"^\|\s*`?(\w+)`?\s*\|\s*`?(\w[\w() ,]*?)`?\s*\|",
    re.MULTILINE,
)

DB_TABLE_HEADING_RE = re.compile(
    r"^#{2,4}\s+.*?(?:table|表|資料表)[：:\s]*`?(\w+)`?",
    re.IGNORECASE | re.MULTILINE,
)

# Headings like: #### `channel` (channel master table)
DB_TABLE_HEADING_BACKTICK_RE = re.compile(r"^#{2,4}\s+`(\w+)`")

SQL_BLOCK_RE = re.compile(r"```sql\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)
SQL_CREATE_TABLE_RE = re.compile(
    r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?`?(\w+)`?\s*\((.*?)^\)",
    re.DOTALL | re.IGNORECASE | re.MULTILINE,
)
SQL_CONSTRAINT_RE = re.compile(
    r"^(?:PRIMARY|UNIQUE|FOREIGN|KEY|INDEX|CONSTRAINT|CHECK)\b", re.IGNORECASE
)
SQL_COLUMN_RE = re.compile(r"^`?(\w+)`?\s+([A-Za-z]+(?:\(\d+(?:,\s*\d+)?\))?)")

MATRIX_ROW_RE = re.compile(
    r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|",
    re.MULTILINE,
)


def extract_sections(docs_dir: Path) -> list[dict]:
    sections = []
    for md in sorted(docs_dir.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for m in HEADING_RE.finditer(text):
            level = len(m.group(1))
            title = m.group(2).strip()
            sec_match = SECTION_ID_RE.search(title)
            sec_id = f"§{sec_match.group(1)}" if sec_match else f"L{level}"
            sections.append({
                "doc": md.relative_to(docs_dir).as_posix(),
                "section": sec_id,
                "title": title,
                "level": level,
            })
    return sections


def extract_columns(docs_dir: Path) -> list[dict]:
    columns = []
    for md in sorted(docs_dir.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        current_table = None
        skip_next_separator = False
        header_seen = False
        for line in text.splitlines():
            th = DB_TABLE_HEADING_RE.match(line) or DB_TABLE_HEADING_BACKTICK_RE.match(line)
            if th:
                current_table = th.group(1)
                header_seen = False
                skip_next_separator = False
                continue
            if current_table and line.startswith("|"):
                stripped = re.sub(r"[|\s\-:]", "", line)
                if not stripped:
                    continue
                cm = COL_TABLE_RE.match(line)
                if cm:
                    col_name = cm.group(1).strip()
                    col_type = cm.group(2).strip()
                    if not header_seen:
                        header_seen = True
                        continue
                    if not re.match(r"^[A-Za-z]", col_type):
                        continue
                    columns.append({
                        "table": current_table,
                        "column": col_name,
                        "type": col_type,
                        "doc": md.relative_to(docs_dir).as_posix(),
                    })
            elif current_table and not line.strip().startswith("|") and line.strip():
                if not line.strip().startswith("<!--"):
                    current_table = None
                    header_seen = False
        seen = {(c["table"], c["column"]) for c in columns}
        for block in SQL_BLOCK_RE.finditer(text):
            for ct in SQL_CREATE_TABLE_RE.finditer(block.group(1)):
                table = ct.group(1)
                for body_line in ct.group(2).splitlines():
                    body_line = body_line.strip().rstrip(",")
                    if not body_line or SQL_CONSTRAINT_RE.match(body_line):
                        continue
                    cm = SQL_COLUMN_RE.match(body_line)
                    if cm and (table, cm.group(1)) not in seen:
                        seen.add((table, cm.group(1)))
                        columns.append({
                            "table": table,
                            "column": cm.group(1),
                            "type": cm.group(2),
                            "doc": md.relative_to(docs_dir).as_posix(),
                        })
    return columns


def print_inventory(docs_dir: Path) -> int:
    docs = Path(docs_dir)
    if not docs.is_dir():
        print(f"error: {docs} is not a directory", file=sys.stderr)
        return 1

    sections = extract_sections(docs)
    columns = extract_columns(docs)

    print("## Appendix A: Section Coverage Matrix\n")
    print("| Doc | Section | Title | Status | Notes |")
    print("|-----|---------|-------|--------|-------|")
    for s in sections:
        indent = "  " * (s["level"] - 1)
        print(f"| {s['doc']} | {s['section']} | {indent}{s['title']} | | |")

    print(f"\nTotal: {len(sections)} sections from {len(set(s['doc'] for s in sections))} docs\n")

    if columns:
        print("## Appendix B: Column Coverage Matrix\n")
        print("| Table | Column | Type | Status | Notes |")
        print("|-------|--------|------|--------|-------|")
        for c in columns:
            print(f"| {c['table']} | {c['column']} | {c['type']} | | |")
        print(f"\nTotal: {len(columns)} columns from {len(set(c['table'] for c in columns))} tables")
    else:
        print("(no DB column definitions detected — check if data model uses"
              " markdown tables with | column | type | format)")

    return 0


def parse_matrix_rows(text: str, header_marker: str) -> list[dict]:
    start = text.find(header_marker)
    if start == -1:
        return []
    next_header = text.find("\n## ", start + len(header_marker))
    chunk = text[start:next_header if next_header != -1 else len(text)]
    rows = []
    in_table = False
    for line in chunk.splitlines():
        if line.strip().startswith("| Doc") or line.strip().startswith("| Table"):
            in_table = True
            continue
        if in_table and line.strip().startswith("|---"):
            continue
        if in_table and line.strip().startswith("|"):
            m = MATRIX_ROW_RE.match(line)
            if m:
                rows.append({
                    "col1": m.group(1).strip(),
                    "col2": m.group(2).strip(),
                    "col3": m.group(3).strip(),
                    "status": m.group(4).strip(),
                    "notes": m.group(5).strip(),
                })
        elif in_table and not line.strip().startswith("|"):
            if line.strip() and not line.strip().startswith("<!--"):
                break
    return rows


def verify(docs_dir: Path, oq_path: Path) -> int:
    if not docs_dir.is_dir():
        print(f"error: {docs_dir} is not a directory", file=sys.stderr)
        return 1
    if not oq_path.is_file():
        print(f"error: {oq_path} not found", file=sys.stderr)
        return 1

    oq_text = oq_path.read_text(encoding="utf-8")

    actual_sections = extract_sections(docs_dir)
    actual_columns = extract_columns(docs_dir)

    matrix_sections = parse_matrix_rows(oq_text, "## Appendix A: Section Coverage Matrix")
    matrix_columns = parse_matrix_rows(oq_text, "## Appendix B: Column Coverage Matrix")

    errors = 0
    warnings = 0

    # --- Section coverage ---
    print("=== Section Coverage ===\n")

    if not matrix_sections:
        print("ERROR: No Section Coverage Matrix found in open-questions.md")
        errors += 1
    else:
        matrix_keys = {(r["col1"], r["col2"]) for r in matrix_sections}
        actual_keys = {(s["doc"], s["section"]) for s in actual_sections}

        missing_from_matrix = actual_keys - matrix_keys
        if missing_from_matrix:
            print(f"MISSING from matrix ({len(missing_from_matrix)} sections):")
            for doc, sec in sorted(missing_from_matrix):
                title = next(
                    (s["title"] for s in actual_sections
                     if s["doc"] == doc and s["section"] == sec),
                    "?",
                )
                print(f"  {doc} {sec}: {title}")
            errors += len(missing_from_matrix)
        else:
            print(f"All {len(actual_keys)} sections present in matrix.")

        blank_status = [r for r in matrix_sections if not r["status"]]
        if blank_status:
            print(f"\nBLANK STATUS ({len(blank_status)} entries — audit incomplete):")
            for r in blank_status:
                print(f"  {r['col1']} {r['col2']}: {r['col3']}")
            errors += len(blank_status)
        else:
            clean = sum(1 for r in matrix_sections if "clean" in r["status"].lower())
            oq_ref = sum(1 for r in matrix_sections if r["status"].startswith("OQ-"))
            print(f"All entries have status: {oq_ref} with OQ ref, {clean} clean,"
                  f" {len(matrix_sections) - oq_ref - clean} other.")

    # --- Column coverage ---
    print("\n=== Column Coverage ===\n")

    if not actual_columns:
        print("(no DB columns detected in docs — skipping)")
    elif not matrix_columns:
        print("ERROR: DB columns exist in docs but no Column Coverage Matrix found")
        errors += len(actual_columns)
    else:
        matrix_col_keys = {(r["col1"], r["col2"]) for r in matrix_columns}
        actual_col_keys = {(c["table"], c["column"]) for c in actual_columns}

        missing_cols = actual_col_keys - matrix_col_keys
        if missing_cols:
            print(f"MISSING from matrix ({len(missing_cols)} columns):")
            for tbl, col in sorted(missing_cols):
                ctype = next(
                    (c["type"] for c in actual_columns
                     if c["table"] == tbl and c["column"] == col),
                    "?",
                )
                print(f"  {tbl}.{col} ({ctype})")
            errors += len(missing_cols)
        else:
            print(f"All {len(actual_col_keys)} columns present in matrix.")

        blank_col = [r for r in matrix_columns if not r["status"]]
        if blank_col:
            print(f"\nBLANK STATUS ({len(blank_col)} entries — audit incomplete):")
            for r in blank_col:
                print(f"  {r['col1']}.{r['col2']} ({r['col3']})")
            errors += len(blank_col)
        else:
            clean = sum(1 for r in matrix_columns if "clean" in r["status"].lower())
            oq_ref = sum(1 for r in matrix_columns if r["status"].startswith("OQ-"))
            print(f"All entries have status: {oq_ref} with OQ ref, {clean} clean,"
                  f" {len(matrix_columns) - oq_ref - clean} other.")

    # --- Summary ---
    print(f"\n{'='*40}")
    if errors:
        print(f"FAIL: {errors} coverage gap(s) found.")
        return 1
    else:
        print("PASS: 100% coverage — all sections and columns audited.")
        return 0


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    cmd = sys.argv[1]

    if cmd == "inventory":
        if len(sys.argv) != 3:
            print("usage: audit_coverage.py inventory <docs-dir>")
            return 2
        return print_inventory(Path(sys.argv[2]))

    elif cmd == "verify":
        if len(sys.argv) != 4:
            print("usage: audit_coverage.py verify <docs-dir> <open-questions.md>")
            return 2
        return verify(Path(sys.argv[2]), Path(sys.argv[3]))

    else:
        print(f"unknown subcommand: {cmd}")
        print(__doc__)
        return 2


if __name__ == "__main__":
    sys.exit(main())
