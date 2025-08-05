from analyzer.repo_fetch_files import fetch_py_files_from_repo

def test_fetch_py_files_from_repo(requests_mock):
    owner = "fake"
    repo = "repo"
    branch = "main"

    tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    file_url = f"https://api.github.com/repos/{owner}/{repo}/contents/file1.py?ref={branch}"

    requests_mock.get(tree_url, json={
        "tree": [{"path": "file1.py", "type": "blob"}]
    })

    requests_mock.get(file_url, json={
        "content": "cHJpbnQoIkhpIik=",  # base64 for print("Hi")
        "encoding": "base64"
    })

    files = fetch_py_files_from_repo(owner, repo, branch)

    assert len(files) == 1
    assert files[0]["path"] == "file1.py"
    assert "print" in files[0]["content"]
