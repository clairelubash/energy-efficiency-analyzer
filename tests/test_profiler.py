from analyzer.profiler import profile_code
import tempfile

def test_profile_code_runs():
    code = "for i in range(100): pass"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        f.flush()
        summary, current, peak = profile_code(f.name)

    assert isinstance(summary, str)
    assert current >= 0
    assert peak >= 0
