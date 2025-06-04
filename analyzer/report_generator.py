import matplotlib.pyplot as plt
import base64
from io import BytesIO

def generate_chart(loop_count, recursion_count, io_count):
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

def generate_report(stats, estimate, suggestions, profile_summary, mem_current, mem_peak):
    report = []
    report.append("# Energy Efficiency Report\n")
    report.append(f"**Estimated energy cost:** `{estimate}` units\n")
    report.append(f"- **Loop count:** {stats['loop_count']}\n")
    report.append(f"- **Recursive calls:** {len(stats['recursive_calls'])}\n")
    report.append(f"- **I/O calls:** {len(stats['io_calls'])}\n")
    report.append(f"- **Current memory usage:** {mem_current:.2f} MB\n")
    report.append(f"- **Peak memory usage:** {mem_peak:.2f} MB\n")

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

    # Embed chart
    report.append("\n### Visual Summary:\n")
    report.append(generate_chart(stats['loop_count'], len(stats['recursive_calls']), len(stats['io_calls'])))

    return "\n".join(report)