# ⚡️ Energy Efficiency Analyzer

Analyze the energy and performance impact of Python scripts or GitHub repositories. 

This tool performs static and dynamic code analysis, estimates energy cost, suggests optimizations, and generates a detailed Markdown report with charts.



## 📦 Features

- ✅ Static analysis (loops, recursion, I/O calls)
- ✅ Dynamic profiling (CPU time, memory usage)
- ✅ Energy estimation model
- ✅ Markdown report generation
- ✅ GitHub repo analysis


## 🔧 Pre-requisites

Before you begin, make sure you have the following installed:

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or alternatively, `pip` for package management  

To install `uv`, run:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```


## 🚀 Quick Start

### ▶️ Analyze a local Python script

```bash
python -m main script my_script.py --output report.md
```

### ▶️ Analyze a GitHub repository

```bash
python -m main repo-url https://github.com/user/repo --branch main --token YOUR_GITHUB_TOKEN
```
> Requires a GitHub token for private repos or higher rate limits. 

## 🛠 Installation

### Option 1: With `uv`
```bash
uv venv
source .venv/bin/activate
uv pip install .
```

### Option 2: With `pip`
```bash
python -m venv .venv
source .venv/bin/activate
pip install .
```

## 🧪 Testing

### Run unit tests locally: 
```bash
pytest -v
```

### Pre-commit Hooks (optionally):
```bash
uv pip install pre-commit 
pre-commit install 
```

> This will automatically run unit tests before every commit. 

