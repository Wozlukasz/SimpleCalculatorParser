from calc_tokens import Token, TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token is None:
            return None

        result = self.find_equation()

        if self.current_token is not None:
            token_val = self.current_token.value if self.current_token.value else self.current_token.type.name
            raise SyntaxError(
                f"Błąd składni: Nieoczekiwany znak '{token_val}'. Prawdopodobnie brakuje operatora (np. '+', '*').")

        return result

    def find_equation(self):
        result = self.find_addition_and_subtraction()
        self.found_equal_token = False

        while self.current_token != None and self.current_token.type == TokenType.EQUAL:
            if self.found_equal_token:
                raise SyntaxError("Błąd składni: W jednej instrukcji dozwolony jest tylko jeden znak równości '='.")

            self.found_equal_token = True
            self.advance()
            result = EqualNode(result, self.find_addition_and_subtraction())

        return result

    def find_addition_and_subtraction(self):
        result = self.find_multiplication_and_division()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.find_multiplication_and_division())

            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.find_multiplication_and_division())
        return result

    def find_multiplication_and_division(self):
        result = self.find_exponents()

        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.find_exponents())

            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.find_exponents())

        return result

    def find_exponents(self):
        result = self.find_brackets_and_values()

        while self.current_token != None and self.current_token.type == TokenType.POWER:
            self.advance()
            result = PowerNode(result, self.find_brackets_and_values())
        return result

    def find_brackets_and_values(self):
        token = self.current_token
        if self.current_token is None: raise SyntaxError("Błąd składni: Brak wyrażenia po '(' lub na końcu wejścia.")

        if token.type == TokenType.INVALID:
            raise SyntaxError("Błąd składni: Wprowadzono nieznany lub niepoprawny znak.")

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)

        if token.type == TokenType.IDENTIFIER:
            name = token.value
            self.advance()

            if self.current_token != None and self.current_token.type == TokenType.LBRACKET:
                self.advance()
                args = self.parse_function_args()

                if self.current_token is None or self.current_token.type != TokenType.RBRACKET:
                    raise SyntaxError(
                        f"Błąd składni: Brakuje zamykającego nawiasu ')' przy wywołaniu funkcji '{name}'.")

                self.advance()
                return FunctionNode(name, args)

            else:
                return VariableNode(name)

        if token.type == TokenType.LBRACKET:
            self.advance()
            result = self.find_addition_and_subtraction()

            if self.current_token is None or self.current_token.type != TokenType.RBRACKET:
                raise SyntaxError("Błąd składni: Nawias otwierający '(' nie został zamknięty.")

            self.advance()
            return result

        if token.type == TokenType.MINUS:
            self.advance()
            result = self.find_brackets_and_values()
            return MinusNode(result)

        error_val = token.value if token.value else token.type.name
        raise SyntaxError(f"Błąd składni: Nieoczekiwany znak '{error_val}'.")

    def parse_function_args(self):
        args = []

        while self.current_token != None and self.current_token.type != TokenType.RBRACKET:
            args.append(self.find_addition_and_subtraction())

            if self.current_token != None and self.current_token.type == TokenType.COMMA:
                self.advance()
            elif self.current_token != None and self.current_token.type != TokenType.RBRACKET:
                raise SyntaxError("Błąd składni: Oczekiwano przecinka ',' pomiędzy argumentami funkcji.")

        return args