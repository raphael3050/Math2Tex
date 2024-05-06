# -*- encoding: utf-8 -*-

import sys
from mathtotex.parser import Parser
from mathtotex.lexer import Lexer
from mathtotex.visitor import LatexGeneratorVisitor

if __name__ == "__main__":
    print("# ================== #")
    print("# MathToTex Compiler # ")
    print("# ================== #")
    lexer = Lexer()
    print("# Lexer is working...")
    lexems = lexer.lex_file(sys.argv[1])
    print("> Parser is working...")
    parser = Parser(lexems)
    ast = parser.parse()
    print(" Parser has finished ✅")
    print("> Code generation is working...")
    visitor = LatexGeneratorVisitor()
    ast.accept(visitor)
    print('Formatted code: \n')
    print('————————————————————————————————————————————————————————————————')
    visitor.get_text()
    print('————————————————————————————————————————————————————————————————')
    
