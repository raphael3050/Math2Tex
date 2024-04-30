
from compiler.abstract_syntax_tree import *


class LatexGeneratorVisitor():
    
    def __init__(self):
        self.text : list[str]= []
        self.indent = 0
        self.tab = "    "
        
    def get_text(self):
        for line in self.text:
            print(line, end="")
    
    def visit(self, ast, args=None):
        ast.accept(self, args)

    def visitMath(self, math: Math, args):
        self.text.append("\begin{math}")
        self.text.append("\n")
        self.indent += 1
        for declaraion in program.declarations:
            self.visit(declaraion)
        self.visit(program.body)
        self.text.append("}")
        