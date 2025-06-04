import ast

class StaticAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loop_count = 0
        self.io_calls = []

    def visit_For(self, node):
        self.loop_count += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.loop_count += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in ("open", "read", "write"):
            self.io_calls.append((node.func.id, node.lineno))
        self.generic_visit(node)

    def analyze(self, code):
        tree = ast.parse(code)
        self.visit(tree)
        return {
            "loop_count": self.loop_count,
            "io_calls": self.io_calls
        }