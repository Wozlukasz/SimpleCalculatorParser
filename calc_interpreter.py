import math
from nodes import *

class Interpreter:
    def __init__(self):
        self.variables = {}
        # matematyczne funkcje
        self.functions = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "max": max,
            "min": min,
            "abs": abs
        }

    def visit(self, node):
        if node is None:
            return None

        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f"Brak metody wykonawczej '{type(node).__name__}' w interpreterze.")

    def visit_NumberNode(self, node):
        return node.value

    def visit_AddNode(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_SubtractNode(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_MultiplyNode(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_DivideNode(self, node):
        right_value = self.visit(node.right)
        if right_value == 0:
            raise ZeroDivisionError("Błąd: Dzielenie przez zero!")
        return self.visit(node.left) / right_value

    def visit_PowerNode(self, node):
        return self.visit(node.left) ** self.visit(node.right)

    def visit_MinusNode(self, node):
        return -self.visit(node.right)

    def visit_EqualNode(self, node):
        if isinstance(node.left, VariableNode):
            value = self.visit(node.right)
            var_name = node.left.name

            self.variables[var_name] = value

            print(f"Utworzono zmienną {var_name} = {value}")

            return None
        else:
            raise SyntaxError("Błąd: Po lewej stronie znaku równości musi znajdować się nazwa zmiennej.")

    def visit_VariableNode(self, node):
        if node.name in self.variables:
            return self.variables[node.name]

        elif node.name == "pi":
            return math.pi
        elif node.name == "e":
            return math.e
        else:
            raise NameError(f"Błąd: Zmienna '{node.name}' nie została zdefiniowana.")

    def visit_FunctionNode(self, node):
        if node.name in self.functions:
            evaluated_args = [self.visit(arg) for arg in node.args]
            func = self.functions[node.name]
            try:
                return func(*evaluated_args)
            except TypeError:
                raise Exception(f"Błąd: Nieprawidłowa liczba argumentów dla funkcji '{node.name}'.")
        else:
            raise NameError(f"Błąd: Nieznana funkcja '{node.name}'.")