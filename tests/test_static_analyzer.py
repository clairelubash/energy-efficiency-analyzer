from analyzer.static_analyzer import StaticAnalyzer

def test_loop_and_recursion_detection():
    from analyzer.static_analyzer import StaticAnalyzer

    code = (
        "def factorial(n):\n"
        "    if n == 0:\n"
        "        return 1\n"
        "    return n * factorial(n - 1)\n"
        "\n"
        "for i in range(5):\n"
        "    print(factorial(i))\n"
    )
    analyzer = StaticAnalyzer()
    result = analyzer.analyze(code)

    assert result["loop_count"] == 1

    recursive_func_names = [name for name, _ in result["recursive_calls"]]
    assert "factorial" in recursive_func_names


