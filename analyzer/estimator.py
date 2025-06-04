def estimate_energy(stats: dict[str, any]) -> int:
    """
    Estimate the energy cost of a given Python script based on static analysis stats.

    Args:
        stats (dict[str, any]): A dictionary containing code metrics such as:
            - "loop_count" (int): Number of loops detected.
            - "recursive_calls" (list[str]): List of function names using recursion.
            - "io_calls" (list[str]): List of detected I/O calls.

    Returns:
        int: An estimated "energy" score based on operation types and frequency.
    """
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