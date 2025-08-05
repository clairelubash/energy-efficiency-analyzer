import logging
import typer
from urllib.parse import urlparse
import concurrent.futures
from analyzer.static_analyzer import StaticAnalyzer
from analyzer.estimator import estimate_energy
from analyzer.suggester import suggest_optimizations
from analyzer.report_generator import generate_report
from analyzer.profiler import profile_code
from analyzer.repo_fetch_files import fetch_py_files_from_repo

app = typer.Typer()
logging.basicConfig(level=logging.INFO)


@app.command()
def script(
    path: str,
    output: str = "energy_report.md"
) -> None:
    """
    Analyze a local Python script and generate a markdown report.
    """
    with open(path, 'r') as f:
        code = f.read()

    analyzer = StaticAnalyzer()
    stats = analyzer.analyze(code)
    estimate = estimate_energy(stats)
    suggestions = suggest_optimizations(stats)
    profile_summary, mem_current, mem_peak = profile_code(path)
    report = generate_report(stats, estimate, suggestions, profile_summary, mem_current, mem_peak)

    with open(output, 'w') as f:
        f.write(report)

    logging.info(f"Report generated: {output}")


@app.command()
def repo(
    url: str,
    branch: str = "main",
    output: str = "energy_report.md",
    token: str = typer.Option(None, help="GitHub token for private repo access")
) -> None:
    """
    Analyze a GitHub repository and generate a markdown report.
    """
    parsed_url = urlparse(url)
    parts = parsed_url.path.strip("/").split("/")
    if len(parts) < 2:
        raise typer.BadParameter("Invalid GitHub URL format.")
    owner, repo_name = parts[0], parts[1]

    files = fetch_py_files_from_repo(owner, repo_name, branch, token)

    def analyze_file(file):
        analyzer = StaticAnalyzer(filename=file["path"])
        return analyzer.analyze(file["content"])

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(analyze_file, files))

    total_stats = {"loop_count": 0, "recursive_calls": [], "io_calls": []}
    for stats in results:
        total_stats["loop_count"] += stats["loop_count"]
        total_stats["recursive_calls"].extend(stats["recursive_calls"])
        total_stats["io_calls"].extend(stats["io_calls"])

    estimate = estimate_energy(total_stats)
    suggestions = suggest_optimizations(total_stats)
    report = generate_report(total_stats, estimate, suggestions, "Profiling not available for repo files.", 0.0, 0.0, is_repo=True)

    with open(output, 'w') as f:
        f.write(report)

    logging.info(f"Report generated: {output}")


if __name__ == "__main__":
    app()
