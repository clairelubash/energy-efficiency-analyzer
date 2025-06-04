import ast

class StaticAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loop_count = 0
        self.recursive_calls = []
        self.io_calls = []
        self.function_defs = []

    def visit_FunctionDef(self, node):
        self.function_defs.append(node.name)
        self.generic_visit(node)

    def visit_For(self, node):
        self.loop_count += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.loop_count += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id in ("open", "read", "write"):
                self.io_calls.append((node.func.id, node.lineno))
            if node.func.id in self.function_defs:
                self.recursive_calls.append((node.func.id, node.lineno))
        self.generic_visit(node)

    def analyze(self, code):
        tree = ast.parse(code)
        self.visit(tree)
        return {
            "loop_count": self.loop_count,
            "recursive_calls": self.recursive_calls,
            "io_calls": self.io_calls
        }