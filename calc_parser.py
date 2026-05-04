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
        
        result = self.find_addition_and_subtraction()

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

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        
        if token.type == TokenType.LBRACKET:
            self.advance()
            result = self.find_addition_and_subtraction()

            if self.current_token.type != TokenType.RBRACKET:
                
                # tu musi być błąd związany ze złym nawiasowaniem (nawias nie został zamknięty)
                return
			
            self.advance()
            return result
        
        if token.type == TokenType.MINUS:
            self.advance()
            result = self.find_brackets_and_values()
            return MinusNode(result)
        
        return None
        #==========================================================================
        # jeżeli kod dojdzie do tej linijki, to znaczy, że gdzieś jest syntax error
        # Np. gdy jest coś pokroju 5*/6
        # albo jest zamknięcie nawiasu bez wcześniejszego otwarcia 5+6)
    
