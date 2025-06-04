import cProfile
import pstats
import io

def profile_code(script_path):
    pr = cProfile.Profile()
    pr.enable()
    globals_dict = {}
    with open(script_path, 'r') as f:
        exec(f.read(), globals_dict)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumtime')
    ps.print_stats(10)
    return s.getvalue()
