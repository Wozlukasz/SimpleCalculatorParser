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
     
@dataclass
class VariableNode:
    name: any

    def __repr__(self):
        return f"{self.name}"
    
@dataclass
class FunctionNode:
    name: any
    args: any

    def __repr__(self):
        args_str = ", ".join(str(arg) for arg in self.args)
        return f"{self.name}({args_str})"

    
@dataclass
class EqualNode:
    left: any
    right: any

    def __repr__(self):
    	return f"{self.left} = {self.right}"
    

def print_tree(node, prefix="", is_last=True):
    if node is None:
        return

    connector = "└── " if is_last else "├── "
    label = node.__class__.__name__

    if hasattr(node, 'value'):
        label += f": {node.value}"
    elif hasattr(node, 'name'):
        label += f": {node.name}"
        
    print(prefix + connector + label)

    children = [] 
    if hasattr(node, 'left') and hasattr(node, 'right'):
        children = [node.left, node.right]
    elif hasattr(node, 'right'):  
        children = [node.right]
    elif hasattr(node, 'args'):
        children = list(node.args)

    prefix += "    " if is_last else "│   "
    for index, child in enumerate(children):
        print_tree(child, prefix, index == len(children) - 1)