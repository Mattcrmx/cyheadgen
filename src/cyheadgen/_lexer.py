"""The C header tokenizer."""
import ply.lex as lex

keywords = (
    'CHAR', 'CONST',
    'DOUBLE', 'ENUM',
    'EXTERN', 'FLOAT',
    'INT', 'LONG',
    'SHORT', 'SIGNED',
    'STATIC', 'STRUCT',
    'TYPEDEF', 'UNSIGNED',
    'VOID', 'VOLATILE',
    # Macros
    'DEFINE', 'IFNDEF',
    'INCLUDE', 'ENDIF',
    'ID'
)

keywords_map = {kw.lower(): kw for kw in keywords}
keywords_map["#ifndef"] = "IFNDEF"
keywords_map["#define"] = "DEFINE"
keywords_map["#include"] = "INCLUDE"
keywords_map["#endif"] = "ENDIF"

tokens = keywords + (
    # Delimiters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD',
    'SEMI', 'COLON',
    'ELLIPSIS',
)

# Completely ignored characters
t_ignore = ' \t\x0c'


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Delimiters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_SEMI = r';'
t_COLON = r':'
t_ELLIPSIS = r'\.\.\.'


def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = keywords_map.get(t.value, "ID")
    return t


def t_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print(f"Illegal character {repr(t.value[0])}")
    t.lexer.skip(1)


ply_lexer = lex.lex()
