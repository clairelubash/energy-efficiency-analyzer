import cProfile
import pstats
import io
import tracemalloc
import runpy

def profile_code(script_path: str) -> tuple[str, float, float]:
    """
    Profile a Python script to get runtime statistics and memory usage.
    """
    pr = cProfile.Profile()
    tracemalloc.start()
    pr.enable()
    runpy.run_path(script_path, run_name="__main__")
    pr.disable()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumtime')
    ps.print_stats(10)
    return s.getvalue(), current / 10**6, peak / 10**6
