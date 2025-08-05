from analyzer.suggester import suggest_optimizations

def test_suggestions():
    stats = {
        "loop_count": 4,
        "recursive_calls": ["a"],
        "io_calls": ["print"]
    }
    suggestions = suggest_optimizations(stats)
    assert "vectorizing" in suggestions[0].lower()
    assert "recursion" in suggestions[1].lower()
    assert "i/o" in suggestions[2].lower()
