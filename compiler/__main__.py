# -*- encoding: utf-8 -*-

import sys
from compiler.parser import Parser
from compiler.lexer import Lexer

if __name__ == "__main__":
    lexer = Lexer()
    lexems = lexer.lex_file(sys.argv[1])
    print(lexems)
    parser = Parser(lexems)
    parser.parse()
    
