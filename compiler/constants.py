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
    # Greek letters
    (
        r"ALPHA|BETA|GAMMA|DELTA|EPSILON|ZETA|SIGMA|THETA|OMEGA|PHI|TAU|MU|DELTA|CHI|KAPPA",
        "GREEK_LETTER",
    ),
    # Keywords
    (r"\bmath\b", "KW_MATH"),
    (r"\bequation\b", "KW_EQUATION"),
    (r"\bexpression\b", "KW_EXPRESSION"),
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
    #(r"\babs\b", "FUNC_ABS"),
    #(r"\bacos\b", "FUNC_ACOS"),
    ##(r"\basin\b", "FUNC_ASIN"),
    #(r"\batan\b", "FUNC_ATAN"),
    #(r"\bceil\b", "FUNC_CEIL"),
    #(r"\bcos\b", "FUNC_COS"),
    #(r"\bexp\b", "FUNC_EXP"),
    #(r"\bfloor\b", "FUNC_FLOOR"),
    #(r"\blog\b", "FUNC_LOG"),
    #(r"\bmax\b", "FUNC_MAX"),
    #(r"\bmin\b", "FUNC_MIN"),
    #(r"\bpow\b", "FUNC_POW"),
    #(r"\brandom\b", "FUNC_RANDOM"),
    #(r"\bsin\b", "FUNC_SIN"),
    #(r"\bsqrt\b", "FUNC_SQRT"),
    #(r"\btan\b", "FUNC_TAN"),
    # Literals
    (r"[0-9]+\.[0-9]+", "LIT_FLOAT"),
    (r"[0-9]+", "LIT_INT"),
    (r"\'[a-zA-Z0-9]+\'", "LIT_CHAR"),
    # Identifiers
    (r"[a-zA-Z_]*", "IDENTIFIER"),
]
