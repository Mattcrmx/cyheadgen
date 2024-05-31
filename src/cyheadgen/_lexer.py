"""The C header tokenizer."""

import logging

import ply.lex as lex

logger = logging.getLogger(__name__)

keywords = (
    "CHAR",
    "DOUBLE",
    "ENUM",
    "FLOAT",
    "INT",
    "LONG",
    "SHORT",
    "UNION",
    "SIGNED",
    "UNSIGNED",
    "STRUCT",
    "TYPEDEF",
    "VOID",
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
    "LBRACE",
    "RBRACE",
    "COMMA",
    "SEMI",
    "COLON",
    "DOT",
    "SHARP",
    "STAR",
    "LT",
    "GT",
    "ICONST",
    "FCONST",
    "SCONST",
    "CCONST",
    "EQUALS",
)

# Completely ignored characters
t_ignore = " \t\x0c"


def t_NEWLINE(t: lex.LexToken) -> None:
    r"""\n+"""
    t.lexer.lineno += t.value.count("\n")


# Delimiters
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_COMMA = r","
t_SEMI = r";"
t_COLON = r":"
t_DOT = r"\."
t_SHARP = r"\#"
t_STAR = r"\*"
t_LT = r"\<"
t_GT = r"\>"

# literals (integer, float, string and single char)
t_ICONST = r"\d+([uU]|[lL]|[uU][lL]|[lL][uU])?"
t_FCONST = r"((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?"
t_SCONST = r"\"([^\\\n]|(\\.))*?\""
t_CCONST = r"(L)?\'([^\\\n]|(\\.))*?\'"


def t_ID(t: lex.LexToken) -> lex.LexToken:
    r"""[A-Za-z_][\w_]*"""
    t.type = keywords_map.get(t.value, "ID")
    return t


def t_multiline_comment(t: lex.LexToken) -> None:
    r"""/\*(.|\n)*?\*/"""
    t.lexer.lineno += t.value.count("\n")


# skip single and multi line comments
def t_simple_comment(t: lex.LexToken) -> None:
    r"""//.*$"""
    t.lexer.lineno += t.value.count("\n")


def t_error(t: lex.LexToken) -> None:
    logger.debug(f"Illegal character {repr(t.value[0])}")
    t.lexer.skip(1)


ply_lexer = lex.lex()
