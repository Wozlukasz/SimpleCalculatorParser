from calc_lexer import Lexer
from calc_parser import Parser
from calc_interpreter import Interpreter
from nodes import print_tree

interpreter = Interpreter()

print("Kalkulator uruchomiony. Wpisz równanie lub 'exit' aby wyjść.")
display_tree = 0 #false

while True:
    try:
        text = input("> ")

        stripped_txt = text.strip().lower()
        if not stripped_txt:
            continue

        if stripped_txt in ['exit', 'quit']:
            break
        elif stripped_txt == "\\ast":
            display_tree = (display_tree + 1) % 2
            print("włączono rysowanie AST") if display_tree else print("wyłączono rysowanie AST")
            continue

        lexer = Lexer(text)
        tokens_list = list(lexer.tokenize())

        parser = Parser(tokens_list)
        ast = parser.parse()

        result = interpreter.visit(ast)

        if result is not None:
            print(result)
        
        if display_tree:
            print_tree(ast)

    except Exception as e:
        print(f"{e}")