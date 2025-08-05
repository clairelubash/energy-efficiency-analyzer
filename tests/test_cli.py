from typer.testing import CliRunner
from main import app
import tempfile
from pathlib import Path

runner = CliRunner()

def test_script_command():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write("print('Hello')\n")
        f.flush()
        output_path = Path(f.name).with_suffix(".md")

        result = runner.invoke(app, ["script", f.name, "--output", str(output_path)])

    assert result.exit_code == 0
    assert output_path.exists()
    assert "Hello" in result.stdout
