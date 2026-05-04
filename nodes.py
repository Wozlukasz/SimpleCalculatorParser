from dataclasses import dataclass

@dataclass
class AddNode():
    left: any
    right: any

    def __repr__(self):
        return f"({self.left} + {self.right})"

@dataclass
class SubtractNode():
    left: any
    right: any

    def __repr__(self):
        return f"({self.left} - {self.right})"
    
@dataclass
class MultiplyNode():
    left: any
    right: any

    def __repr__(self):
        return f"({self.left} * {self.right})"

@dataclass
class DivideNode():
    left: any
    right: any

    def __repr__(self):
        return f"({self.left} / {self.right})"

@dataclass
class PowerNode():
    left: any
    right: any

    def __repr__(self):
        return f"({self.left} ^ {self.right})"


@dataclass    
class MinusNode():
    right: any

    def __repr__(self):
        return f"(-{self.right})"
    
@dataclass
class NumberNode:
	value: any

	def __repr__(self):
		return f"{self.value}"
     
