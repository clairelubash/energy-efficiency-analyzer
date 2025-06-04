import ast

class StaticAnalyzer(ast.NodeVisitor):
    """
    A static code analyzer that inspects Python code to count loops,
    identify recursive function calls, and detect I/O operations.

    Attributes:
        loop_count (int): Number of loops (for and while) detected.
        recursive_calls (list[tuple[str, int]]): List of tuples with recursive function names and line numbers.
        io_calls (list[tuple[str, int]]): List of tuples with I/O function names and line numbers.
        function_defs (list[str]): Names of all functions defined in the code.
    """

    def __init__(self) -> None:
        self.loop_count: int = 0
        self.recursive_calls: list[tuple[str, int]] = []
        self.io_calls: list[tuple[str, int]] = []
        self.function_defs: list[str] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """
        Visit a function definition node and record its name.

        Args:
            node (ast.FunctionDef): The function definition AST node.
        """
        self.function_defs.append(node.name)
        self.generic_visit(node)

    def visit_For(self, node: ast.For) -> None:
        """
        Visit a for loop node and increment the loop count.

        Args:
            node (ast.For): The for loop AST node.
        """
        self.loop_count += 1
        self.generic_visit(node)

    def visit_While(self, node: ast.While) -> None:
        """
        Visit a while loop node and increment the loop count.

        Args:
            node (ast.While): The while loop AST node.
        """
        self.loop_count += 1
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        """
        Visit a function call node. Detects I/O operations and recursive calls.

        Args:
            node (ast.Call): The function call AST node.
        """
        if isinstance(node.func, ast.Name):
            if node.func.id in ("open", "read", "write"):
                self.io_calls.append((node.func.id, node.lineno))
            if node.func.id in self.function_defs:
                self.recursive_calls.append((node.func.id, node.lineno))
        self.generic_visit(node)

    def analyze(self, code: str) -> dict[str, any]:
        """
        Analyze Python source code for loops, recursion, and I/O calls.

        Args:
            code (str): The Python source code as a string.

        Returns:
            dict[str, any]: A dictionary containing:
                - "loop_count": number of loops detected.
                - "recursive_calls": list of (function_name, line_number) tuples for recursive calls.
                - "io_calls": list of (io_function_name, line_number) tuples.
        """
        tree = ast.parse(code)
        self.visit(tree)
        return {
            "loop_count": self.loop_count,
            "recursive_calls": self.recursive_calls,
            "io_calls": self.io_calls
        }
