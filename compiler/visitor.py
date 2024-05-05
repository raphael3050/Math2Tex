
from compiler.abstract_syntax_tree import (
    Math,
)


class LatexGeneratorVisitor():
    
    def __init__(self):
        # Permet de gérer l'indentation du code latex
        self.text : list[str]= []
        self.indent = 0
        self.tab = "    "
        
    def get_text(self):
        for line in self.text:
            print(line, end="")
    
    def visit(self, ast, args=None):
        ast.accept(self, args)

    def visitMath(self, math: Math, args):
        self.text.append("\\begin{math}\n")
        self.indent += 1
        if math.equations is not None:
            for equation in math.equations:
                self.text.append(self.indent*self.tab +"\\begin{equation}\n")
                self.indent += 1
                self.visit(equation)
                self.indent -= 1
                self.text.append(self.indent*self.tab +"\\end{equation}\n")
        if math.expressions is not None:
            for expression in math.expressions:
                self.visit(expression)
        self.text.append("\\end{math}\n")

    def visitEquation(self, equation, args):
        self.text.append(self.indent*self.tab)
        self.visit(equation.expression_1)
        self.text.append(f" {equation.compop.value} ")
        self.visit(equation.expression_2)
        self.text.append("\n")

    def visitExpression(self, expression, args):
        for i, statement in enumerate(expression.statements):
            self.visit(statement)
            if i < len(expression.op):
                self.text.append(f" {expression.op[i].value} ")

    def visitStatement(self, statement, args):
        if statement.parenth is not None:
            self.visit(statement.parenth)
        if statement.term is not None:
            self.visit(statement.term) 
        if statement.function is not None:
            self.visit(statement.function)

    def visitParenth(self, parenth, args):
        self.text.append("(")
        for expression in parenth.expressions:
            self.visit(expression)
        self.text.append(")")

    def visitTerm(self, term, args):
        self.text.append(term.term.value)
    
    def visitFunction(self, function, args):
        self.visit(function.litteral)
        self.visit(function.parenth)
    
        
    def visitLitteral(self, litteral, args):
        self.text.append(litteral.value)