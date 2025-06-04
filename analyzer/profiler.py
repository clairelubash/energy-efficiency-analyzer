import cProfile
import pstats
import io
import tracemalloc

def profile_code(script_path):
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
