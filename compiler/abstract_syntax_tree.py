
from ast import List


class astNode():
    def accept(self, visitor, args=None):
        name = self.__class__.__name__
        getattr(visitor, f"visit{name}")(self, args)
    
class Math(astNode):
    def __init__(self, equations, expressions):
        self.equations : List[Equation] = equations
        self.expressions : List[Expression] = expressions

class Equation(astNode):
    def __init__(self, expression_1, compop, expression_2):
        self.expression_1 : Expression = expression_1
        self.compop = compop
        self.expression_2 : Expression = expression_2

class Expression(astNode):
    def __init__(self, function, statements, op):
        self.function : Function = function
        self.statements : List[Statement] = statements
        self.op = op
        
class Function(astNode):
    def __init__(self, litteral, parenth):
        self.litteral : Litteral = litteral
        self.parenth : Parenth = parenth

class Parenth(astNode):
    def __init__(self, expression):
        self.expressions : List[Expression] = expression

class Statement(astNode):
    def __init__(self, parenth, term):
        self.parenth : Parenth = parenth
        self.term : Term = term
        
class Term(astNode):
    def __init__(self, term):
        self.term = term



        