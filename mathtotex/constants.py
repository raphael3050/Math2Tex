# ==================================================
# Fichiers de constantes pour le lexer et le parser.
# ==================================================
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
    (r":", "COLON"),
    # Greek letters
    (
        r"ALPHA|BETA|GAMMA|DELTA|EPSILON|ZETA|SIGMA|THETA|OMEGA|PHI|TAU|MU|CHI|KAPPA",
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

    # Literals
    (r"[0-9]+\.[0-9]+", "LIT_FLOAT"),
    (r"[0-9]+", "LIT_INT"),
    (r"\'[a-zA-Z0-9]+\'", "LIT_CHAR"),
    # Identifiers
    (r"[a-zA-Z_]*", "IDENTIFIER"),
]

LATEX_FUNCTIONS = [
    "abs",
    "acos",
    "asin",
    "atan",
    "ceil",
    "cos",
    "exp",
    "floor",
    "log",
    "max",
    "min",
    "pow",
    "random",
    "sin",
    "sqrt",
    "tan",
    "sum",
    "int",
]

# Fonctions particulières en LaTeX, elles doivent être traitées différemment par le visiteur.
LATEX_UTILS_FUNCTIONS = [
    "sum",
    "int",
    "pow",
]
