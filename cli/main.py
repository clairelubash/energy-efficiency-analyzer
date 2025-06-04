import sys
from analyzer.static_analyzer import StaticAnalyzer
from analyzer.estimator import estimate_energy
from analyzer.report_generator import generate_report


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m cli.main <script_to_analyze.py>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        code = f.read()

    analyzer = StaticAnalyzer()
    stats = analyzer.analyze(code)
    estimate = estimate_energy(stats)
    report = generate_report(stats, estimate)
    print(report)


if __name__ == "__main__":
    main()