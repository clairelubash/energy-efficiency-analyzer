def estimate_energy(stats):
    base_costs = {
        "loop": 10,
        "recursion": 100,
        "io": 50
    }
    energy = (
        stats["loop_count"] * base_costs["loop"] +
        len(stats["recursive_calls"]) * base_costs["recursion"] +
        len(stats["io_calls"]) * base_costs["io"]
    )
    return energy