import requests

def fetch_py_files_from_repo(
    owner: str,
    repo: str,
    branch: str = "main",
    github_token: str = None,
) -> list[dict[str, str]]:
    """
    Fetch all Python files from a GitHub repository branch via GitHub API.

    Args:
        owner (str): GitHub repo owner.
        repo (str): Repository name.
        branch (str): Branch to analyze (default 'main').
        github_token (str): Optional GitHub token for authenticated requests.

    Returns:
        list[dict[str, str]]: List of dicts with 'path' and 'content' of each Python file.
    """

    headers = {}
    if github_token:
        headers['Authorization'] = f'token {github_token}'

    # Step 1: Get the repo tree recursively (list of all files)
    tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    resp = requests.get(tree_url, headers=headers)
    resp.raise_for_status()
    tree = resp.json()

    python_files = []
    for item in tree.get("tree", []):
        if item["path"].endswith(".py") and item["type"] == "blob":
            # Step 2: Get file contents
            file_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{item['path']}?ref={branch}"
            file_resp = requests.get(file_url, headers=headers)
            file_resp.raise_for_status()
            file_json = file_resp.json()
            import base64
            content = base64.b64decode(file_json["content"]).decode("utf-8")
            python_files.append({"path": item["path"], "content": content})

    return python_files
