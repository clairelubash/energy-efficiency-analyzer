from analyzer.estimator import estimate_energy

def test_estimate_energy():
    stats = {
        "loop_count": 2,
        "recursive_calls": ["func1", "func2"],
        "io_calls": ["print", "open"]
    }
    assert estimate_energy(stats) == 2*10 + 2*100 + 2*50
