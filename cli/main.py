import os
import argparse
from analyzer.static_analyzer import StaticAnalyzer
from analyzer.estimator import estimate_energy
from analyzer.suggester import suggest_optimizations
from analyzer.report_generator import generate_report
from analyzer.profiler import profile_code


def main():
    parser = argparse.ArgumentParser(description="Energy Efficiency Analyzer")
    parser.add_argument("script", help="Python script to analyze")
    parser.add_argument("--output", help="Output markdown file", default="energy_report.md")
    args = parser.parse_args()

    with open(args.script, 'r') as f:
        code = f.read()

    analyzer = StaticAnalyzer()
    stats = analyzer.analyze(code)
    estimate = estimate_energy(stats)
    suggestions = suggest_optimizations(stats)
    profile_summary, mem_current, mem_peak = profile_code(args.script)
    report = generate_report(stats, estimate, suggestions, profile_summary, mem_current, mem_peak)

    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(args.output, 'w') as f:
        f.write(report)

    print(f"Report generated: {args.output}")


if __name__ == "__main__":
    main()