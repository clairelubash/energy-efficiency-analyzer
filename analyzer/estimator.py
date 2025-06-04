def estimate_energy(stats):
    # Very simple cost model
    return stats["loop_count"] * 10 + len(stats["io_calls"]) * 50