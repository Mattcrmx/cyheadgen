"""The C header tokenizer."""

import logging

import ply.lex as lex

logger = logging.getLogger(__name__)

keywords = (
    "CHAR",
    "CONST",
    "DOUBLE",
    "ENUM",
    "EXTERN",
    "FLOAT",
    "INT",
    "LONG",
    "SHORT",
    "UNION",
    "IF",
    "ELSE",
    "SIGNED",
    "STATIC",
    "STRUCT",
    "TYPEDEF",
    "UNSIGNED",
    "VOID",
    "VOLATILE",
    # Macros
    "DEFINE",
    "IFNDEF",
    "INCLUDE",
    "ENDIF",
    "ID",
)

keywords_map = {kw.lower(): kw for kw in keywords}

tokens = keywords + (
    # Delimiters ( ) [ ] { } , . ; :
    "LPAREN",
    "RPAREN",
    "LBRACKET",
    "RBRACKET",
    "LBRACE",
    "RBRACE",
    "COMMA",
    "PERIOD",
    "SEMI",
    "COLON",
    "ELLIPSIS",
    "SHARP",
    "STAR",
    "PLUS",
    "MINUS",
    "DIVIDE",
    "LT",
    "GT",
    "LE",
    "GE",
    "OR",
    "AND",
    "NOT",
    "LNOT",
    "CONDOP",
    "LAND",
    "LOR",
    "XOR",
    "EQ",
    "NE",
    "LSHIFT",
    "RSHIFT",
    "ICONST",
    "FCONST",
    "SCONST",
    "CCONST",
    "EQUALS",
    "LSHIFTEQUAL",
    "RSHIFTEQUAL",
    "ANDEQUAL",
    "XOREQUAL",
    "OREQUAL",
)

# Completely ignored characters
t_ignore = " \t\x0c"


def t_NEWLINE(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count("\n")


# Delimiters
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_COMMA = r","
t_PERIOD = r"\."
t_SEMI = r";"
t_COLON = r":"
t_ELLIPSIS = r"\.\.\."
t_SHARP = r"\#"
t_STAR = r"\*"
t_PLUS = r"\+"
t_MINUS = r"-"
t_DIVIDE = r"/"
t_LT = r"\<"
t_GT = r"\>"
t_OR = r"\|"
t_LOR = r"\|\|"
t_AND = r"&"
t_LAND = r"&&"
t_NOT = r"~"
t_LNOT = r"!"
t_XOR = r"\^"
t_LSHIFT = r"<<"
t_RSHIFT = r">>"
t_EQ = r"=="
t_NE = r"!="
t_CONDOP = r"\?"
t_LE = r"<="
t_GE = r">="

t_EQUALS = r"="
t_LSHIFTEQUAL = r"<<="
t_RSHIFTEQUAL = r">>="
t_ANDEQUAL = r"&="
t_OREQUAL = r"\|="
t_XOREQUAL = r"\^="

# Integer literal
t_ICONST = r"\d+([uU]|[lL]|[uU][lL]|[lL][uU])?"

# Floating literal
t_FCONST = r"((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?"

# String literal
t_SCONST = r"\"([^\\\n]|(\\.))*?\""

# Character constant 'c' or L'c'
t_CCONST = r"(L)?\'([^\\\n]|(\\.))*?\'"


def t_ID(t):
    r"""[A-Za-z_][\w_]*"""
    t.type = keywords_map.get(t.value, "ID")
    return t


def t_multiline_comment(t):
    r"""/\*(.|\n)*?\*/"""
    t.lexer.lineno += t.value.count("\n")


# skip single and multi line comments
def t_simple_comment(t):
    r"""//.*$"""
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    logger.debug(f"Illegal character {repr(t.value[0])}")
    t.lexer.skip(1)


ply_lexer = lex.lex()
