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
            #==========================================================================
            # tu jest błąd w synatxie, że brakuje jakiegoś operatora najprawdopodobniej (ale może też inne przypadki,
            # na razie taki tylko znalazłem). Przykładowo: 2(3+1) 
            # brakuje "*" przed nawiasem. Wiem, że często się robi niejawne mnożenie w matmie, ale nie utrudniajmy
            # sobie życia wszystkimi możliwymi przypadkami :)
            return None

        return result


    def find_equation(self):
        result = self.find_addition_and_subtraction()
        self.found_equal_token = False 
        
        while self.current_token != None and self.current_token.type == TokenType.EQUAL:
            if self.found_equal_token:
                #==========================================================================
                # tu powinno wywalić błąd, jeżeli w jednej linijce są dwa znaki równości (zakładam,
                # że dopuszczamy weryfikację tylko pojedynczego równania w linijce, ale może być wiele linii)
                return None

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

        if token.type == TokenType.INVALID:
            #==========================================================================
            # W zapisie pojawił się jakiś nieznany/niepoprawny znak
            return None

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        
        if token.type == TokenType.IDENTIFIER:
            name = self.current_token.value
            self.advance()

            # to jest parsowanie wywołania funkcji np: fun(a1, a2)
            if self.current_token != None and self.current_token.type == TokenType.LBRACKET:
                self.advance()

                args = self.parse_function_args()

                if self.current_token != None and self.current_token.type != TokenType.RBRACKET:
                    #=========================================================================
                    # brakuje ")" przy  funkcji
                    return None
                
                self.advance() #to jakby pożera nawias zamykający
                return FunctionNode(name, args)
            
            #jeżeli nie ma nawiasów po nazwie to jest to zmienna np: fun
            else:
                return VariableNode(name)


            
        if token.type == TokenType.LBRACKET:
            self.advance()
            result = self.find_addition_and_subtraction()

            if self.current_token is None or self.current_token.type != TokenType.RBRACKET:
                #==========================================================================
                # tu musi być błąd związany ze złym nawiasowaniem (nawias nie został zamknięty)
                # Ten w warunku "if self.current_token is None" jest na wypadek końca tokenów
                #  przed zamknięciem nawiasu np: (3+(5-1) 
                return None
			
            self.advance()
            return result
        
        if token.type == TokenType.MINUS:
            self.advance()
            result = self.find_brackets_and_values()
            return MinusNode(result)
        
        return None
        #==========================================================================
        # jeżeli kod dojdzie do tej linijki, to znaczy, że gdzieś jest syntax error
        # Także to "None należy zamienić na łapanie błędu"
        # Np. gdy jest coś pokroju: 5*/6
        # albo jest zamknięcie nawiasu bez wcześniejszego otwarcia: 5+6)
        #trzeba będzie więc przechwycić aktualny token i co z nim nie tak
    
    def parse_function_args(self):
        args = []

        while self.current_token != None and self.current_token.type != TokenType.RBRACKET:
            args.append(self.find_addition_and_subtraction())

            if self.current_token != None and self.current_token.type == TokenType.COMMA:
                self.advance()
            elif self.current_token != None and self.current_token.type != TokenType.RBRACKET:
                #==========================================================================
                #po argumencie powinien być "," lub ")" a jest coś innego lub brakuje ")"
                return None

        return args
