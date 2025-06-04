import cProfile
import pstats
import io
import tracemalloc

def profile_code(script_path: str) -> tuple[str, float, float]:
    """
    Profile a Python script to get runtime statistics and memory usage.

    Args:
        script_path (str): The file path of the Python script to profile.

    Returns:
        tuple[str, float, float]: A tuple containing:
            - A string summary of top function calls sorted by cumulative time.
            - The current memory usage in MB.
            - The peak memory usage in MB.
    """
    pr = cProfile.Profile()
    tracemalloc.start()
    pr.enable()
    globals_dict = {}
    with open(script_path, 'r') as f:
        exec(f.read(), globals_dict)
    pr.disable()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumtime')
    ps.print_stats(10)
    return s.getvalue(), current / 10**6, peak / 10**6
