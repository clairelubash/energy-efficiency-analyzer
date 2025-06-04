import argparse
from urllib.parse import urlparse
from analyzer.static_analyzer import StaticAnalyzer
from analyzer.estimator import estimate_energy
from analyzer.suggester import suggest_optimizations
from analyzer.report_generator import generate_report
from analyzer.profiler import profile_code
from analyzer.repo_fetch_files import fetch_py_files_from_repo


def main() -> None:
    """
    Command-line entry point for analyzing either a single Python script's energy and performance or for all files in a Github repository.
    
    Parses arguments, runs static and dynamic analysis, and writes a markdown report.
    """
    parser = argparse.ArgumentParser(description="Energy Efficiency Analyzer")
    parser.add_argument("--script", help="Python script to analyze")
    parser.add_argument("--repo-url", help="GitHub repository URL to analyze")
    parser.add_argument("--branch", help="Branch name for GitHub repo (default: main)", default="main")
    parser.add_argument("--output", help="Output markdown file", default="energy_report.md")
    parser.add_argument("--token", help="GitHub token for authenticated requests", default=None)
    args = parser.parse_args()

    if args.script:
        with open(args.script, 'r') as f:
            code = f.read()
        analyzer = StaticAnalyzer()
        stats = analyzer.analyze(code)
        estimate = estimate_energy(stats)
        suggestions = suggest_optimizations(stats)
        profile_summary, mem_current, mem_peak = profile_code(args.script)
        report = generate_report(stats, estimate, suggestions, profile_summary, mem_current, mem_peak)

    elif args.repo_url:
        # Parse owner/repo from URL
        parsed_url = urlparse(args.repo_url)
        path_parts = parsed_url.path.strip("/").split("/")
        if len(path_parts) < 2:
            raise ValueError("Invalid GitHub repo URL format.")
        owner, repo = path_parts[0], path_parts[1]

        files = fetch_py_files_from_repo(owner, repo, args.branch, args.token)

        total_stats = {"loop_count": 0, "recursive_calls": [], "io_calls": []}
        analyzer = StaticAnalyzer()

        for file in files:
            analyzer = StaticAnalyzer(filename=file["path"])
            file_stats = analyzer.analyze(file["content"])
            total_stats["loop_count"] += file_stats["loop_count"]
            total_stats["recursive_calls"].extend(file_stats["recursive_calls"])
            total_stats["io_calls"].extend(file_stats["io_calls"])

        estimate = estimate_energy(total_stats)
        suggestions = suggest_optimizations(total_stats)
        profile_summary = "Profiling is not supported for remote repo files."
        mem_current = 0.0
        mem_peak = 0.0
        report = generate_report(total_stats, estimate, suggestions, profile_summary, mem_current, mem_peak, is_repo=True)

    else:
        parser.error("Either --script or --repo-url must be provided.")

    with open(args.output, 'w') as f:
        f.write(report)
    print(f"Report generated: {args.output}")


if __name__ == "__main__":
    main()