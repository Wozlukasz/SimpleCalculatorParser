from enum import Enum, auto
from dataclasses import dataclass

class TokenType(Enum):
    INVALID  = auto()

    LBRACKET = auto()
    RBRACKET = auto()

    NUMBER   = auto()
    VARIABLE = auto()
    FUNCTION = auto()

    MINUS    = auto()
    PLUS     = auto()
    MULTIPLY = auto()
    DIVIDE   = auto()
    POWER    = auto()

    
@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f" {self.value}" if self.value != None else "")