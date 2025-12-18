from datetime import datetime
def render_markdown(report: dict) -> str:
    lines: list[str] = []

    lines.append(f"# CSV Profiling Report")
    lines.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n")

    lines.append("## Summary")
    lines.append(f"- Rows: **{report['n_rows']}**")
    lines.append(f"- Columns: **{report['n_cols']}**\n")

    lines.append("## Columns")
    lines.append("| name | type | missing | missing_pct | unique |")
    lines.append("|---|---:|---:|---:|---:|")
    
    for c in report["columns"]:
        lines.append(
            f"| {c['name']} | {c['type']} | {c['missing']} | {c['missing_pct']:.1f}% | {c['unique']} |"
        )

    lines.append("\n## Notes")
    lines.append("- Missing values are: `''`, `na`, `n/a`, `null`, `none`, `nan` (case-insensitive)")

    return "\n".join(lines)