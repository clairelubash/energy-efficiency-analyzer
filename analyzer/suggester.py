def suggest_optimizations(stats: dict[str, any]) -> list[str]:
    """
    Suggest code optimizations based on analyzed stats.

    Args:
        stats (dict[str, any]): Code statistics including loops, recursion, and I/O operations.

    Returns:
        list[str]: A list of suggestions to optimize the script for better efficiency.
    """
    suggestions = []
    if stats["loop_count"] > 2:
        suggestions.append("Consider vectorizing loops or using map/filter.")
    if stats["recursive_calls"]:
        suggestions.append("Consider converting recursion to iteration to reduce call overhead.")
    if stats["io_calls"]:
        suggestions.append("Move I/O operations outside of loops where possible.")
    return suggestions