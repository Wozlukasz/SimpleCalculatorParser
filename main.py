from lexer import Lexer

while True:
    text = input("> ")
    lexer = Lexer(text)
    tokens = lexer.tokenize()
    print(list(tokens))