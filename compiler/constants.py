LEXEM_REGEXES = [

    # Special characters
    (r"\(", "L_PAREN"),
    (r"\)", "R_PAREN"),
    (r"\{", "L_CURL_BRACKET"),
    (r"\}", "R_CURL_BRACKET"),
    (r"\[", "L_SQUARE_BRACKET"),
    (r"\]", "R_SQUARE_BRACKET"),
    (r";", "SEMICOLON"),
    (r",", "COMMA"),

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
    (r"=", "EQUOP_EQUAL"),
    (r"\!\=", "EQUOP_NOT_EQUAL"),


    # Fonctions 
    (r"\babs\b", "FUNC_ABS"),
    (r"\bacos\b", "FUNC_ACOS"),
    (r"\basin\b", "FUNC_ASIN"),
    (r"\batan\b", "FUNC_ATAN"),
    (r"\bceil\b", "FUNC_CEIL"),
    (r"\bcos\b", "FUNC_COS"),
    (r"\bexp\b", "FUNC_EXP"),
    (r"\bfloor\b", "FUNC_FLOOR"),
    (r"\blog\b", "FUNC_LOG"),
    (r"\bmax\b", "FUNC_MAX"),
    (r"\bmin\b", "FUNC_MIN"),
    (r"\bpow\b", "FUNC_POW"),
    (r"\brandom\b", "FUNC_RANDOM"),
    (r"\bsin\b", "FUNC_SIN"),
    (r"\bsqrt\b", "FUNC_SQRT"),
    (r"\btan\b", "FUNC_TAN"),

    ##(r"[a-zA-Z]\([^)]*\)", "FUNC_CUSTOM"),
    #(r"[a-zA-Z]\([^)]*\)", "FUNC_CUSTOM"),

    # Literals
    (r"[0-9]+\.[0-9]+", "LIT_FLOAT"),
    (r"[0-9]+", "LIT_INT"),
    (r"\'[a-zA-Z0-9]+\'", "LIT_CHAR"),
    
    # Identifiers
    #(r"[a-zA-Z_][a-zA-Z0-9_]*", "IDENTIFIER"),
    (r"[a-zA-Z_]*", "IDENTIFIER")
]