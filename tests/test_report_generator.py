from analyzer.report_generator import generate_report

def test_generate_report():
    stats = {
        "loop_count": 2,
        "recursive_calls": ["func"],
        "io_calls": [("print", 5, "test.py")]
    }
    report = generate_report(
        stats=stats,
        estimate=160,
        suggestions=["Try using vectorization."],
        profile_summary="Sample Profile",
        mem_current=10.5,
        mem_peak=20.5
    )

    assert "**Loop count:** 2" in report
    assert "Try using vectorization" in report
    assert "Sample Profile" in report
    assert "data:image/png;base64" in report
