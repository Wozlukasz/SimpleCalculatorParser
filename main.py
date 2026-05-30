from calc_lexer import Lexer
from calc_parser import Parser
from calc_interpreter import Interpreter

interpreter = Interpreter()

print("Kalkulator uruchomiony. Wpisz równanie lub 'exit' aby wyjść.")

while True:
    try:
        text = input("> ")
        if text.strip().lower() in ['exit', 'quit']:
            break
        if not text.strip():
            continue

        lexer = Lexer(text)
        tokens_list = list(lexer.tokenize())

        parser = Parser(tokens_list)
        ast = parser.parse()

        if ast is None:
            print("Błąd składni.")
            continue

        result = interpreter.visit(ast)

        if result is not None:
            print(result)

    except Exception as e:
        print(f"{e}")