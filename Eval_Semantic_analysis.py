from typing import List

from Token import *
from Lexer import *

class Node: ...


class Statement(Node): ...


class Expression(Node): ...


identifiers = {}
nodes = {}


# describes literals
class Literal(Expression):
    def __init__(self, token_type: str, value: str):
        self.type = token_type
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

    def __get_type(self):
        if self.type == INTEGER:
            return int(self.value)
        elif self.type == FLOAT:
            return float(self.value)
        elif self.type == STRING:
            return str(self.value)
        elif self.type == BOOLEAN:
            if self.value == 'true':
                return True
            else:
                return False
        else:
            return None

    def eval(self):
        try:
            literal_type = self.__get_type()
        except ValueError:
            raise ValueError(f'Error converting {self.value} to {self.type}')
        return literal_type


# descries identifiers
class Identifier(Expression):
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def eval(self):
        if self.name in identifiers:
            return identifiers[self.name]
        else:
            raise NameError(f'{self.name} is not defined')


# describes variable declaration statements
class VariableDeclarationStatement(Statement):
    def __init__(self, variable_type: str, name: Identifier, value: Expression):
        self.variable_type = variable_type
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f'({self.variable_type} {self.name} {self.value})'

    def eval(self):
        if self.name in identifiers:
            raise NameError(f'"{self.name}" is already defined')
        if self.value is not None:
            identifiers[self.name] = self.value.eval()
        else:
            identifiers[self.name] = None


# describes flow description
class NodesExpression(Statement):
    def __init__(self, from_node: Identifier, to_node: Identifier, action: str):
        self.from_node = from_node
        self.to_node = to_node
        self.action = action

    def __repr__(self) -> str:
        return f'(nodes ({self.from_node}) ({self.to_node}) (description ({self.action})))'

    def eval(self):
        if self.from_node not in nodes:
            nodes[self.from_node] = {}
            nodes[self.from_node][self.to_node] = self.action
        elif self.to_node in nodes[self.from_node]:
            raise SyntaxError(f'This path is already described')
        if self.from_node not in nodes:
            nodes[self.from_node] = self.from_node


# describes the block of more expressions/statements in a statement
class BlockStatement(Statement):
    def __init__(self, statements: List[Statement]):
        self.statements = statements

    def __repr__(self) -> str:
        data = ''
        for x in self.statements:
            data += x.__repr__()
        return f'({data})'

    def eval(self):
        for x in self.statements:
            data = x.eval()


# describes variable assignment statement
class AssignStatement(Statement):
    def __init__(self, name: str, value: Expression):
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f'({self.name} {self.value})'

    def eval(self):
        if self.name not in identifiers:
            raise NameError(f' "{self.name}" is not defined')
        identifiers[self.name] = self.value.eval()


# describes if statements
class IfStatement(Statement):
    def __init__(self, condition, if_condition: BlockStatement, if_not_condition: BlockStatement):
        self.condition = condition
        self.if_condition = if_condition
        self.if_not_condition = if_not_condition

    def __repr__(self) -> str:
        return f'(if ({self.condition}) ({self.if_condition}) ({self.if_not_condition}))'

    def eval(self):
        if self.condition.eval():
            self.if_condition.eval()
        else:
            self.if_not_condition.eval() if self.if_not_condition else None


# describes while statements
class WhileStatement(Statement):
    def __init__(self, condition: Expression, action: Statement):
        self.condition = condition
        self.action = action

    def __repr__(self) -> str:
        return f'(while ({self.condition}) ({self.action}))'

    def eval(self):
        while self.condition.eval():
            self.action.eval()


# describes negation or opposite number usage
class PrefixExpression(Expression):
    def __init__(self, operator: Statement, right: Expression):
        self.operator = operator
        self.right = right

    def __get_type(self) -> str:
        return self.type.right

    def __repr__(self) -> str:
        return f'({self.operator}{self.right})'

    def eval(self):
        operator = {
            '!': lambda a: not a,
            '-': lambda a: -a,
            '+': lambda a: a,
        }
        try:
            return operator[self.operator](self.right.eval())
        except TypeError:
            raise TypeError(f'Operator {self.operator} is not used in this scope')


# describes expressions with two operands
class NormalExpression(Expression):
    def __init__(self, left: Expression, operator: Statement, right: Expression):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self) -> str:
        return f'({self.left} {self.operator} {self.right})'

    def eval(self):
        operator = {
            # arithmetic operations
            '//': lambda a, b: a % b,
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '&&': lambda a, b: a and b,
            '||': lambda a, b: a or b,
            #  conditional operations
            '==': lambda a, b: a == b,
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
        }

        try:
            return operator[self.operator](self.left.eval(), self.right.eval())
        except TypeError:
            raise TypeError(f'Cannot perform "{self.operator}" between {self.left_type()} and {self.right_type()}')
