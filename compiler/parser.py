# -*- encoding: utf-8 -*-

import logging
from compiler.abstract_syntax_tree import *

logger = logging.getLogger(__name__)

class ParsingException(Exception):
    pass

class Parser:
    def __init__(self, lexems):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems = lexems

    # ==========================
    #      Helper Functions
    # ==========================

    def accept(self):
        """
        Pops the lexem out of the lexems list.
        """
        self.show_next()
        return self.lexems.pop(0)

    def show_next(self, n=1):
        """
        Returns the next token in the list WITHOUT popping it.
        """
        try:
            return self.lexems[n - 1]
        except IndexError:
            self.error("No more lexems left.")

    def expect(self, tag):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.show_next()
        if next_lexem.tag != tag:
            raise ParsingException(
                f"ERROR at {str(self.show_next().position)}: Expected {tag}, got {next_lexem.tag} instead"
            )
        return self.accept()

    def remove_comments(self):
        """
        Removes the comments from the token list by testing their tags.
        """
        self.lexems = [lexem for lexem in self.lexems if lexem.tag != "COMMENT"]

    # ==========================
    #     Parsing Functions
    # ==========================

    def parse(self):
        """
        Main function: launches the parsing operation given a lexem list.
        """
        try:
            self.remove_comments()
            math = self.parse_math()
            print("Parsing successful!")
        except ParsingException as err:
            logger.exception(err)
            raise 
        return math
        
    def parse_math(self):
        equations = []
        expressions = []
        self.expect("KW_MATH")
        self.expect("L_CURL_BRACKET")
        if self.show_next().tag == "KW_EQUATION":
            while self.show_next().tag != "R_CURL_BRACKET":
                equations.append(self.parse_equation())
        #elif self.show_next().tag == "KW_EQUATION":
            #while self.show_next().tag != "R_CURL_BRACKET":
                #expressions.append(self.parse_expression())
        self.expect("R_CURL_BRACKET")
        return Math(equations, expressions)

    def parse_equation(self):
        self.expect("KW_EQUATION")
        self.expect("L_CURL_BRACKET")
        expression_1 = self.parse_expression()
        compop = self.parse_compop()
        expression_2 = self.parse_expression()
        self.expect("R_CURL_BRACKET")
        return Equation(expression_1, compop, expression_2)

    def parse_compop(self):
        if(self.show_next().tag == "EQUOP_EQUAL"):
            return self.expect("EQUOP_EQUAL")
        if(self.show_next().tag == "OP_GREATER"):
            return self.expect("OP_GREATER")
        elif(self.show_next().tag == "OP_LESS"):
            return self.expect("OP_LESS")
        elif(self.show_next().tag == "OP_GREATER_EQUAL"):
            return self.expect("OP_GREATER_EQUAL")
        elif(self.show_next().tag == "OP_LESS_EQUAL"):
            return self.expect("OP_LESS_EQUAL")

    def parse_expression(self):
        function = None
        statements = []
        op = []
        if self.show_next().tag == "IDENTIFIER" and self.show_next(n=2).tag == "L_PAREN":
            function = self.parse_function()
        else:
            while (self.show_next().tag != "R_CURL_BRACKET") and (self.show_next().tag != "EQUOP_EQUAL") and (self.show_next().tag != "R_PAREN"):
                if self.show_next().tag in ["OP_PLUS", "OP_MINUS", "OP_MULT"]:
                    op.append(self.parse_op())
                statements.append(self.parse_statement())
        return Expression(function, statements, op)

    def parse_function(self):
        litteral = self.expect("IDENTIFIER")
        parenth = self.parse_parenth()
        return Function(litteral, parenth)



    def parse_statement(self):
        parenth = None
        term = None
        if self.show_next().tag == "L_PAREN":
            parenth = self.parse_parenth()
        else:
            term = self.parse_term()
        return Statement(parenth, term)
        
    def parse_parenth(self):
        left_parenth = self.expect("L_PAREN")
        expression = []
        while(self.show_next().tag != "R_PAREN"):
            expression.append(self.parse_expression())
            # TODO : ambiguité entre LIT_CHAR et IDENTIFIER
            """             if self.show_next().tag == "LIT_CHAR":
                litteral = self.expect("LIT_CHAR")
            elif self.show_next().tag == "IDENTIFIER":
                litteral = self.expect("IDENTIFIER") """
        right_parenth = self.expect("R_PAREN")
        return Parenth(expression)        
    
    def parse_term(self):
        term = None
        if self.show_next().tag == "LIT_INT":
            term = self.expect("LIT_INT")
        elif self.show_next().tag == "LIT_FLOAT":
            term = self.expect("LIT_FLOAT")
        elif self.show_next().tag == "IDENTIFIER":
            term = self.expect("IDENTIFIER")
        return Term(term)
    
    def parse_op(self):
        if self.show_next().tag == "OP_PLUS":
            return self.expect("OP_PLUS")
        elif self.show_next().tag == "OP_MINUS":
            return self.expect("OP_MINUS")
        elif self.show_next().tag == "OP_MULT":
            return self.expect("OP_MULT")