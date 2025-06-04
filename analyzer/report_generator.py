def generate_report(stats, estimate):
    report = []
    report.append("# Energy Efficiency Report\n")
    report.append(f"Estimated energy cost: {estimate} units\n")
    report.append(f"Loop count: {stats['loop_count']}\n")
    if stats["io_calls"]:
        report.append("IO Calls:")
        for call, lineno in stats["io_calls"]:
            report.append(f"- {call} at line {lineno}")
    else:
        report.append("No I/O detected.")
    return "\n".join(report)
