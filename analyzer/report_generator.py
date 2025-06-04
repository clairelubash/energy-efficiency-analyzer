def generate_report(stats, estimate, suggestions, profile_summary):
    report = []
    report.append("# Energy Efficiency Report\n")
    report.append(f"**Estimated energy cost:** `{estimate}` units\n")
    report.append(f"- **Loop count:** {stats['loop_count']}\n")
    report.append(f"- **Recursive calls:** {len(stats['recursive_calls'])}\n")
    report.append(f"- **I/O calls:** {len(stats['io_calls'])}\n")

    if stats["io_calls"]:
        report.append("\n### Detailed I/O Calls:")
        for call, lineno in stats["io_calls"]:
            report.append(f"- `{call}` at line {lineno}")

    report.append("\n### Suggestions:")
    if suggestions:
        for s in suggestions:
            report.append(f"- {s}")
    else:
        report.append("- No major optimizations suggested.")

    report.append("\n### Profiling Summary (Top 10 by cumulative time):\n")
    report.append("```text\n" + profile_summary + "```\n")
    return "\n".join(report)