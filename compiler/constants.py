LEXEM_REGEXES = [

    # Special characters
    (r"\(", "L_PAREN"),
    (r"\)", "R_PAREN"),
    (r"\{", "L_CURL_BRACKET"),
    (r"\}", "R_CURL_BRACKET"),
    (r"\[", "L_SQUARE_BRACKET"),
    (r"\]", "R_SQUARE_BRACKET"),
    (r";", "SEMICOLON"),

    # Keywords
    (r"\bmath\b", "KW_MATH"),
    (r"\bequation\b", "KW_EQUATION"),
    (r"\bexpression\b", "KW_EXPRESSION"),



    # Symbols
    (r"\bALPHA\b", "SYM_ALPHA"),
    (r"\bBETA\b", "SYM_BETA)"),
    (r"\bGAMMA\b", "SYM_GAMMA"),
    (r"\bDELTA\b", "SYM_DELTA"),
    (r"\bEPSILON\b", "SYM_EPSILON"),
    (r"\bZETA\b", "SYM_ZETA"),
    (r"\bSIGMA\b", "SYM_SIGMA"),
    (r"\bTHETA\b", "SYM_THETA"),
    (r"\bOMEGA\b", "SYM_OMEGA"),
    (r"\bPHI\b", "SYM_PHI"),
    (r"\bTAU\b", "SYM_TAU"),
    (r"\bMU\b", "SYM_MU"),
    (r"\bDELTA\b", "SYM_DELTA"),
    (r"\bCHI\b", "SYM_CHI"),
    (r"\bKAPPA\b", "SYM_KAPPA"),

    # Operators
    (r"\+", "OP_PLUS"),
    (r"\-", "OP_MINUS"),
    (r"\*", "OP_MULT"),
    (r"\/", "OP_DIV"),
    (r"\%", "OP_MOD"),
    (r"\>\=", "OP_GREATER_EQUAL"),
    (r"\<\=", "OP_LESS_EQUAL"),
    (r"\>", "OP_GREATER"),
    (r"\<", "OP_LESS"),
    
    # Equality operators
    (r"\=", "EQUOP_EQUAL"),
    (r"\!\=", "EQUOP_NOT_EQUAL"),
    
        
    # Literals
    (r"[0-9]+\.[0-9]+", "LIT_FLOAT"),
    (r"[0-9]+", "LIT_INT"),
    (r"\'[a-zA-Z0-9]+\'", "LIT_CHAR"),
    (r"\"[a-zA-Z0-9]+\"", "LIT_CHAR"),
    
    # Identifiers
    (r"[a-zA-Z_][a-zA-Z0-9_]*", "IDENTIFIER")
]