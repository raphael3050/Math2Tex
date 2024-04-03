# -*- encoding: utf-8 -*-

import pytest
import os

from compiler.lexer import Lexer
from compiler.p4rser import Parser


@pytest.mark.parametrize("test_program", ["example1.c"])
def test_parse_program(test_program):
    lexer = Lexer()
    file_path = os.path.join("examples/"+ test_program)
    lexems = lexer.lex_file(file=file_path)
    print(lexems)
    parser = Parser(lexems)
    parser.parse()

@pytest.mark.parametrize("test_program", ["example2.c"])
def test_parse_program(test_program):
    lexer = Lexer()
    file_path = os.path.join("examples/"+ test_program)
    lexems = lexer.lex_file(file=file_path)
    print(lexems)
    parser = Parser(lexems)
    parser.parse()
    
@pytest.mark.parametrize("test_program", ["example3.c"])
def test_parse_program(test_program):
    lexer = Lexer()
    file_path = os.path.join("examples/"+ test_program)
    lexems = lexer.lex_file(file=file_path)
    print(lexems)
    parser = Parser(lexems)
    parser.parse()