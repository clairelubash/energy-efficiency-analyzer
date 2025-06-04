import sys
from analyzer.static_analyzer import StaticAnalyzer
from analyzer.estimator import estimate_energy
from analyzer.suggester import suggest_optimizations
from analyzer.report_generator import generate_report
from analyzer.profiler import profile_code


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m cli.main <script_to_analyze.py>")
        sys.exit(1)

    script_path = sys.argv[1]
    with open(script_path, 'r') as f:
        code = f.read()

    analyzer = StaticAnalyzer()
    stats = analyzer.analyze(code)
    estimate = estimate_energy(stats)
    suggestions = suggest_optimizations(stats)
    profile_summary = profile_code(script_path)
    report = generate_report(stats, estimate, suggestions, profile_summary)

    output_path = "energy_report.md"
    with open(output_path, 'w') as f:
        f.write(report)

    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    main()