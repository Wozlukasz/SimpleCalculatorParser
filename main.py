from calc_lexer import Lexer
from calc_parser import Parser

while True:
    text = input("> ")
    lexer = Lexer(text)
    tokens_list = list(lexer.tokenize())

    parser = Parser(tokens_list)
    ast = parser.parse()

    print(tokens_list)
    print(ast)
