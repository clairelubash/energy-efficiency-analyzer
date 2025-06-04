import matplotlib.pyplot as plt
import base64
from io import BytesIO

def generate_chart(loop_count: int, recursion_count: int, io_count: int) -> str:
    """
    Generate a base64-encoded PNG bar chart summarizing static analysis counts.

    Args:
        loop_count (int): Number of loops detected.
        recursion_count (int): Number of recursive calls detected.
        io_count (int): Number of I/O calls detected.

    Returns:
        str: Markdown image tag with embedded base64 PNG chart.
    """
    labels = ['Loops', 'Recursions', 'I/O Calls']
    values = [loop_count, recursion_count, io_count]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['blue', 'orange', 'green'])
    ax.set_title('Static Analysis Counts')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    img_data = base64.b64encode(buf.read()).decode('utf-8')
    return f"![Chart](data:image/png;base64,{img_data})"


def generate_report(
    stats: dict[str, any],
    estimate: int,
    suggestions: list[str],
    profile_summary: str,
    mem_current: float,
    mem_peak: float
) -> str:
    """
    Generate a markdown report summarizing energy estimate, code analysis, suggestions, 
    profiling data, and a visual summary chart.

    Args:
        stats (dict[str, any]): Dictionary of static analysis results (loop counts, recursive calls, io calls).
        estimate (int): Estimated energy cost.
        suggestions (list[str]): List of optimization suggestions.
        profile_summary (str): Text summary of profiling stats.
        mem_current (float): Current memory usage in MB.
        mem_peak (float): Peak memory usage in MB.

    Returns:
        str: Complete markdown report as a string.
    """
    report = [
        "# Energy Efficiency Report\n",
        f"**Estimated energy cost:** `{estimate}` units\n",
        f"- **Loop count:** {stats['loop_count']}\n",
        f"- **Recursive calls:** {len(stats['recursive_calls'])}\n",
        f"- **I/O calls:** {len(stats['io_calls'])}\n",
        f"- **Current memory usage:** {mem_current:.2f} MB\n",
        f"- **Peak memory usage:** {mem_peak:.2f} MB\n"
    ]

    if stats["io_calls"]:
        report.append("\n### Detailed I/O Calls:")
        for call, lineno in stats["io_calls"]:
            report.append(f"- `{call}` at line {lineno}")

    report.append("\n### Suggestions:")
    if suggestions:
        report.extend(f"- {s}" for s in suggestions)
    else:
        report.append("- No major optimizations suggested.")

    report.append("\n### Profiling Summary (Top 10 by cumulative time):\n")
    report.append("```text\n" + profile_summary + "```\n")

    report.append("\n### Visual Summary:\n")
    report.append(generate_chart(stats['loop_count'], len(stats['recursive_calls']), len(stats['io_calls'])))

    return "\n".join(report)