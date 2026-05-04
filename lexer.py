from lexer_tokens import Token, TokenType


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def tokenize(self):
        while self.current_char != None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char == '.' or self.current_char.isdigit():
                yield self.read_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LBRACKET)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RBRACKET)
            elif self.current_char == '^':
                self.advance()
                yield Token(TokenType.POWER)
            else:
                self.advance()
                yield Token(TokenType.INVALID)
                # raise Exception(f"unknown character '{self.current_char}'")

    def read_number(self):
        num_str = ""
        while self.current_char != None and (self.current_char.isdigit() or self.current_char == "."):
            num_str += self.current_char
            self.advance()

        if num_str == "." or num_str.count(".") > 1:
            return Token(TokenType.INVALID, None)
        
        if num_str[0] == ".":
            num_str = '0' + num_str
        if num_str[-1] == ".":
            num_str += '0'

        return Token(TokenType.NUMBER, float(num_str))

class LexerError(Exception):
    def __init__(self, message, line, column):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"Błąd w linii {line}, kolumnie {column}: {message}")