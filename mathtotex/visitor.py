
from mathtotex.abstract_syntax_tree import (
    Math,
)
from mathtotex.constants import (
    LATEX_FUNCTIONS,
    LATEX_UTILS_FUNCTIONS,
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
        if math.equations is None:
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
                self.text.append(self.indent*self.tab)
                self.visit(expression)
                self.text.append("\n")
        if math.equations is None:
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
        # Aucun argument n'est passé, on est dans le cas général
        if args is None:
            self.text.append("(")
            for i, expression in enumerate(parenth.expressions):
                self.visit(expression)
                if i < len(parenth.commas):
                    self.text.append(f"{parenth.commas[i].value}")
            self.text.append(")")
        # On est dans le cas d'une fonction utilitaire avec une syntaxe particulière
        else:
            if args.term.value != "pow":
                self.text.append("_")
            for i, expression in enumerate(parenth.expressions):
                self.text.append("{")
                self.visit(expression)
                self.text.append("}")
                if i == 0:
                    self.text.append("^")
            



    def visitTerm(self, term, args):
        if term.term.value in LATEX_FUNCTIONS:
            self.text.append('\\'+term.term.value)
        elif term.term.tag == "GREEK_LETTER":
            self.text.append('\\'+term.term.value.lower())
        else:
            self.text.append(term.term.value)
    
    def visitFunction(self, function, args):
        if function.litteral.term.value != "pow":
            self.visit(function.litteral)
        args_to_send = None
        try:
            # On vérifie si la fonction est une fonction utilitaire avec une syntaxe particulière
            if function.litteral.term.value in LATEX_UTILS_FUNCTIONS:
                if function.litteral.term.value == "sum":
                    assert len(function.parenth.expressions) == 3
                    assert function.parenth.expressions[0].op[0].value == ":"
                    args_to_send = function.litteral
                    function.parenth.expressions[0].op[0].value = "="
                elif function.litteral.term.value == "int":
                    assert len(function.parenth.expressions) == 4
                    args_to_send = function.litteral
                elif function.litteral.term.value == "pow":
                    assert len(function.parenth.expressions) == 2
                    args_to_send = function.litteral
            self.visit(function.parenth, args_to_send)
        except AssertionError as e:
            print(f"Erreur de syntaxe pour la fonction {function.litteral.term.value}",e)
            raise 
