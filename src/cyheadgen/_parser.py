# flake8: noqa
# type: ignore
import cyheadgen._lexer as lexer_module
import ply.yacc as yacc
from cyheadgen.ast import Function, Header, Macro, Argument, CEnum

tokens = lexer_module.tokens


def p_header_file(p):
    """header_file : declaration
                  | declaration header_file
                  | empty"""
    if len(p) == 3:
        p[2].append(p[1])
        p[0] = p[2]
    else:
        p[0] = [p[1]]


def p_declaration(p):
    """declaration : function
                   | header
                   | macro"""
    p[0] = p[1]


def p_function(p):
    """function : type ID LPAREN parameters RPAREN SEMI
                | type ID LPAREN VOID RPAREN SEMI
                | ID ID LPAREN parameters RPAREN SEMI
                | ID ID LPAREN VOID RPAREN SEMI
                | ID STAR ID LPAREN parameters RPAREN SEMI
                | ID STAR ID LPAREN VOID RPAREN SEMI
                | type STAR ID LPAREN parameters RPAREN SEMI
                | type STAR ID LPAREN VOID RPAREN SEMI"""
    if "*" in p:
        p[0] = Function(
            name=p[3],
            type=f"{p[2]}{p[1]}",
            parameters=p[5]
        )
    else:
        p[0] = Function(
            name=p[2],
            type=p[1],
            parameters=p[4]
        )


def p_struct_or_union_specifier(p):
    """struct_or_union_specifier : struct_or_union ID LBRACE struct_declaration_list RBRACE
                                 | struct_or_union LBRACE struct_declaration_list RBRACE
                                 | struct_or_union ID"""
    pass


def p_struct_or_union(p):
    """struct_or_union : STRUCT
                       | UNION
                       """
    p[0] = p[1]


def p_struct_declaration_list(p):
    """struct_declaration_list : struct_declaration
                               | struct_declaration_list struct_declaration"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].extend(p[2])
        p[0] = p[1]


def p_struct_declaration(p):
    """struct_declaration : specifier_qualifier_list struct_declarator_list SEMI"""
    p[0] = p[1]


def p_specifier_qualifier_list(p):
    """specifier_qualifier_list : type specifier_qualifier_list
                                | type"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].extend(p[2])
        p[0] = p[1]


def p_struct_declarator_list_1(p):
    """struct_declarator_list : struct_declarator
                              | struct_declarator_list COMMA struct_declarator"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].extend(p[3])
        p[0] = p[1]


def p_struct_declarator_1(p):
    """struct_declarator : declarator
                         | declarator COLON constant"""
    pass


def p_declarator_1(p):
    """declarator : pointer direct_declarator
                  | direct_declarator"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"*{p[1]}"


def p_direct_declarator(p):
    """direct_declarator : ID
                         | LPAREN declarator RPAREN
                         | direct_declarator LPAREN parameter_type_list RPAREN"""
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]
    else:
        # TODO: handle params
        p[0] = p[1:]


def p_direct_declarator_2(p):
    """direct_declarator : direct_declarator LPAREN RPAREN
                         | direct_declarator LPAREN identifier_list RPAREN """
    if len(p) == 2:
        p[0] = p[1]
    else:
        # TODO: handle params
        p[0] = p[1:]


def p_enum_specifier(p):
    """enum_specifier : ENUM ID LBRACE enumerator_list RBRACE"""
    p[0] = CEnum(name=p[2], attributes=p[4])


def p_enumerator_list(p):
    """enumerator_list : enumerator
                       | enumerator_list COMMA enumerator"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].extend(p[3])
        p[0] = p[1]


def p_enumerator(p):
    """enumerator : ID
                  | ID EQUALS constant"""
    if len(p) == 2:
        p[0] = Argument(name=p[1])
    else:
        p[0] = Argument(name=p[1], value=p[3])


def p_parameters(p):
    """parameters : type ID COMMA parameters
                  | type ID
                  | type pointer ID
                  | type pointer ID COMMA parameters"""
    if len(p) == 3:
        p[0] = [Argument(name=p[2], type=p[1])]
    elif len(p) == 4:
        p[0] = [Argument(name=p[3], type=f"{p[1]}{p[2]}")]

    # insert to preserver to arguments order
    elif "*" in p[1:]:
        p[5].insert(0, Argument(name=p[3], type=f"{p[1]}{p[2]}"))
        p[0] = p[5]
    else:
        p[4].insert(0, Argument(name=p[2], type=p[1]))
        p[0] = p[4]


def p_parameter_type_list(p):
    """parameter_type_list : type ID COMMA parameter_type_list
                           | type ID"""
    if len(p) == 3:
        p[0] = [Argument(type=p[1], name=p[2])]
    else:
        p[4].extend(Argument(type=p[1], name=p[2]))
        p[0] = p[4]


def p_pointer(p):
    """pointer : STAR
               | STAR pointer"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"*{p[2]}"


def p_identifier_list(p):
    """identifier_list : ID
                       | identifier_list COMMA ID"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].extend(p[3])
        p[0] = p[1]


def p_types(p):
    """type : VOID
            | CHAR
            | SHORT
            | INT
            | LONG
            | FLOAT
            | DOUBLE
            | SIGNED
            | UNSIGNED
            | ID
            | struct_or_union_specifier
            | enum_specifier
            """
    p[0] = p[1]


def p_macro(p):
    """macro : SHARP IFNDEF ID
             | SHARP DEFINE ID
             | SHARP ENDIF"""
    if len(p) == 4:
        p[0] = Macro(name=p[3], type=p[2])
    else:
        p[0] = Macro(name=None, type=p[2])


def p_header(p):
    """header : SHARP INCLUDE SCONST
              | SHARP INCLUDE LT ID DOT ID GT"""
    if len(p) == 4:
        p[0] = Header(name=p[3], type="custom")
    else:
        p[0] = Header(name=p[4], type="standard")


def p_constant(p):
    """constant : ICONST
                | FCONST
                | CCONST"""
    p[0] = p[1]


def p_empty(p):
    """empty : """
    pass


def p_error(t):
    raise ValueError(f"Error generation production with token {t}")


ply_parser = yacc.yacc()

if __name__ == "__main__":

    simple_fn = "#endif // API_H"
    p = ply_parser.parse(simple_fn)
    print(p)
