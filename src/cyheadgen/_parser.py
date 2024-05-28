# flake8: noqa
import _lexer
import ply.yacc as yacc

tokens = _lexer.tokens

# translation-unit:


def p_translation_unit_1(p):
    """translation_unit : external_declaration"""
    p[0] = p[1]


def p_translation_unit_2(p):
    """translation_unit : translation_unit external_declaration"""
    # p[1].extend(p[2])
    # p[0] = p[1]

# external-declaration:


def p_external_declaration_1(p):
    """external_declaration : function_definition"""
    p[0] = [p[1]]


def p_external_declaration_2(p):
    """external_declaration : declaration"""
    p[0] = p[1]

# function-definition:


def p_function_definition_1(p):
    """function_definition : declaration_specifiers declarator declaration_list compound_statement"""
    # p[0] = p[1]
    print("p")


def p_function_definition_2(p):
    """function_definition : declarator declaration_list compound_statement"""
    print("p")


def p_function_definition_3(p):
    """function_definition : declarator compound_statement"""
    print("p")


def p_function_definition_4(p):
    """function_definition : declaration_specifiers declarator compound_statement"""
    print("p")


# declaration:


def p_declaration_1(p):
    """declaration : declaration_specifiers init_declarator_list SEMI"""
    pass


def p_declaration_2(p):
    """declaration : declaration_specifiers SEMI"""
    pass


def p_declaration_3(p):
    """declaration : header"""
    p[0] = p[1]


def p_declaration_4(p):
    """declaration : macro"""
    pass


# declaration-list:


def p_declaration_list_1(p):
    """declaration_list : declaration"""
    pass


def p_declaration_list_2(p):
    """declaration_list : declaration_list declaration """
    pass

# declaration-specifiers


def p_declaration_specifiers_1(p):
    """declaration_specifiers : storage_class_specifier declaration_specifiers"""
    pass


def p_declaration_specifiers_2(p):
    """declaration_specifiers : type_specifier declaration_specifiers"""
    pass


def p_declaration_specifiers_3(p):
    """declaration_specifiers : type_qualifier declaration_specifiers"""
    pass


def p_declaration_specifiers_4(p):
    """declaration_specifiers : storage_class_specifier"""
    pass


def p_declaration_specifiers_5(p):
    """declaration_specifiers : type_specifier"""
    pass


def p_declaration_specifiers_6(p):
    """declaration_specifiers : type_qualifier"""
    pass

# storage-class-specifier


def p_storage_class_specifier(p):
    """storage_class_specifier : EXTERN
                               | STATIC
                               | TYPEDEF
                               """
    pass

# type-specifier:


def p_type_specifier(p):
    """type_specifier : VOID
                      | CHAR
                      | SHORT
                      | INT
                      | LONG
                      | FLOAT
                      | DOUBLE
                      | SIGNED
                      | UNSIGNED
                      | struct_or_union_specifier
                      | enum_specifier
                      """
    p[0] = p[1]

# type-qualifier:


def p_type_qualifier(p):
    """type_qualifier : CONST
                      | VOLATILE"""
    pass

# struct-or-union-specifier


def p_struct_or_union_specifier_1(p):
    """struct_or_union_specifier : struct_or_union ID LBRACE struct_declaration_list RBRACE"""
    pass


def p_struct_or_union_specifier_2(p):
    """struct_or_union_specifier : struct_or_union LBRACE struct_declaration_list RBRACE"""
    pass


def p_struct_or_union_specifier_3(p):
    """struct_or_union_specifier : struct_or_union ID"""
    pass

# struct-or-union:


def p_struct_or_union(p):
    """struct_or_union : STRUCT
                       | UNION
                       """
    pass

# struct-declaration-list:


def p_struct_declaration_list_1(p):
    """struct_declaration_list : struct_declaration"""
    pass


def p_struct_declaration_list_2(p):
    """struct_declaration_list : struct_declaration_list struct_declaration"""
    pass

# init-declarator-list:


def p_init_declarator_list_1(p):
    """init_declarator_list : init_declarator"""
    pass


def p_init_declarator_list_2(p):
    """init_declarator_list : init_declarator_list COMMA init_declarator"""
    pass

# init-declarator


def p_init_declarator_1(p):
    """init_declarator : declarator"""
    pass


def p_init_declarator_2(p):
    """init_declarator : declarator EQUALS initializer"""
    pass

# struct-declaration:


def p_struct_declaration(p):
    """struct_declaration : specifier_qualifier_list struct_declarator_list SEMI"""
    pass

# specifier-qualifier-list:


def p_specifier_qualifier_list_1(p):
    """specifier_qualifier_list : type_specifier specifier_qualifier_list"""
    pass


def p_specifier_qualifier_list_2(p):
    """specifier_qualifier_list : type_specifier"""
    pass


def p_specifier_qualifier_list_3(p):
    """specifier_qualifier_list : type_qualifier specifier_qualifier_list"""
    pass


def p_specifier_qualifier_list_4(p):
    """specifier_qualifier_list : type_qualifier"""
    pass

# struct-declarator-list:


def p_struct_declarator_list_1(p):
    """struct_declarator_list : struct_declarator"""
    pass


def p_struct_declarator_list_2(p):
    """struct_declarator_list : struct_declarator_list COMMA struct_declarator"""
    pass

# struct-declarator:


def p_struct_declarator_1(p):
    """struct_declarator : declarator"""
    pass


def p_struct_declarator_2(p):
    """struct_declarator : declarator COLON constant_expression"""
    pass


def p_struct_declarator_3(p):
    """struct_declarator : COLON constant_expression"""
    pass

# enum-specifier:


def p_enum_specifier_1(p):
    """enum_specifier : ENUM ID LBRACE enumerator_list RBRACE"""
    pass


def p_enum_specifier_2(p):
    """enum_specifier : ENUM LBRACE enumerator_list RBRACE"""
    pass


def p_enum_specifier_3(p):
    """enum_specifier : ENUM ID"""
    pass

# enumerator_list:


def p_enumerator_list_1(p):
    """enumerator_list : enumerator"""
    pass


def p_enumerator_list_2(p):
    """enumerator_list : enumerator_list COMMA enumerator"""
    pass

# enumerator:


def p_enumerator_1(p):
    """enumerator : ID"""
    pass


def p_enumerator_2(p):
    """enumerator : ID EQUALS constant_expression"""
    pass

# declarator:


def p_declarator_1(p):
    """declarator : pointer direct_declarator"""
    pass


def p_declarator_2(p):
    """declarator : direct_declarator"""
    pass

# direct-declarator:


def p_direct_declarator_1(p):
    """direct_declarator : ID"""
    pass


def p_direct_declarator_2(p):
    """direct_declarator : LPAREN declarator RPAREN"""
    pass


def p_direct_declarator_3(p):
    """direct_declarator : direct_declarator LBRACKET constant_expression_opt RBRACKET"""
    pass


def p_direct_declarator_4(p):
    """direct_declarator : direct_declarator LPAREN parameter_type_list RPAREN """
    pass


def p_direct_declarator_5(p):
    """direct_declarator : direct_declarator LPAREN identifier_list RPAREN """
    pass


def p_direct_declarator_6(p):
    """direct_declarator : direct_declarator LPAREN RPAREN """
    pass

# pointer:


def p_pointer_1(p):
    """pointer : STAR type_qualifier_list"""
    pass


def p_pointer_2(p):
    """pointer : STAR"""
    pass


def p_pointer_3(p):
    """pointer : STAR type_qualifier_list pointer"""
    pass


def p_pointer_4(p):
    """pointer : STAR pointer"""
    pass

# type-qualifier-list:


def p_type_qualifier_list_1(p):
    """type_qualifier_list : type_qualifier"""
    pass


def p_type_qualifier_list_2(p):
    """type_qualifier_list : type_qualifier_list type_qualifier"""
    pass

# parameter-type-list:


def p_parameter_type_list_1(p):
    """parameter_type_list : parameter_list"""
    pass


def p_parameter_type_list_2(p):
    """parameter_type_list : parameter_list COMMA ELLIPSIS"""
    pass

# parameter-list:


def p_parameter_list_1(p):
    """parameter_list : parameter_declaration"""
    pass


def p_parameter_list_2(p):
    """parameter_list : parameter_list COMMA parameter_declaration"""
    pass

# parameter-declaration:


def p_parameter_declaration_1(p):
    """parameter_declaration : declaration_specifiers declarator"""
    pass


def p_parameter_declaration_2(p):
    """parameter_declaration : declaration_specifiers abstract_declarator_opt"""
    pass

# identifier-list:


def p_identifier_list_1(p):
    """identifier_list : ID"""
    pass


def p_identifier_list_2(p):
    """identifier_list : identifier_list COMMA ID"""
    pass

# initializer:


def p_initializer_1(p):
    """initializer : assignment_expression"""
    pass


def p_initializer_2(p):
    """initializer : LBRACE initializer_list RBRACE
                   | LBRACE initializer_list COMMA RBRACE"""
    pass

# initializer-list:


def p_initializer_list_1(p):
    """initializer_list : initializer"""
    pass


def p_initializer_list_2(p):
    """initializer_list : initializer_list COMMA initializer"""
    pass

# type-name:


def p_type_name(p):
    """type_name : specifier_qualifier_list abstract_declarator_opt"""
    pass


def p_abstract_declarator_opt_1(p):
    """abstract_declarator_opt : empty"""
    pass


def p_abstract_declarator_opt_2(p):
    """abstract_declarator_opt : abstract_declarator"""
    pass

# abstract-declarator:


def p_abstract_declarator_1(p):
    """abstract_declarator : pointer """
    pass


def p_abstract_declarator_2(p):
    """abstract_declarator : pointer direct_abstract_declarator"""
    pass


def p_abstract_declarator_3(p):
    """abstract_declarator : direct_abstract_declarator"""
    pass

# direct-abstract-declarator:


def p_direct_abstract_declarator_1(p):
    """direct_abstract_declarator : LPAREN abstract_declarator RPAREN"""
    pass


def p_direct_abstract_declarator_2(p):
    """direct_abstract_declarator : direct_abstract_declarator LBRACKET constant_expression_opt RBRACKET"""
    pass


def p_direct_abstract_declarator_3(p):
    """direct_abstract_declarator : LBRACKET constant_expression_opt RBRACKET"""
    pass


def p_direct_abstract_declarator_4(p):
    """direct_abstract_declarator : direct_abstract_declarator LPAREN parameter_type_list_opt RPAREN"""
    pass


def p_direct_abstract_declarator_5(p):
    """direct_abstract_declarator : LPAREN parameter_type_list_opt RPAREN"""
    pass

# Optional fields in abstract declarators


def p_constant_expression_opt_1(p):
    """constant_expression_opt : empty"""
    pass


def p_constant_expression_opt_2(p):
    """constant_expression_opt : constant_expression"""
    pass


def p_parameter_type_list_opt_1(p):
    """parameter_type_list_opt : empty"""
    pass


def p_parameter_type_list_opt_2(p):
    """parameter_type_list_opt : parameter_type_list"""
    pass

# statement:


def p_statement(p):
    """
    statement : compound_statement
              | selection_statement
              """
    pass

# compound-statement:


def p_compound_statement_1(p):
    """compound_statement : LBRACE declaration_list statement_list RBRACE"""
    pass


def p_compound_statement_2(p):
    """compound_statement : LBRACE statement_list RBRACE"""
    pass


def p_compound_statement_3(p):
    """compound_statement : LBRACE declaration_list RBRACE"""
    pass


def p_compound_statement_4(p):
    """compound_statement : LBRACE RBRACE"""
    pass

# statement-list:


def p_statement_list_1(p):
    """statement_list : statement"""
    pass


def p_statement_list_2(p):
    """statement_list : statement_list statement"""
    pass

# selection-statement


def p_selection_statement_1(p):
    """selection_statement : IF LPAREN expression RPAREN statement"""
    pass


def p_selection_statement_2(p):
    """selection_statement : IF LPAREN expression RPAREN statement ELSE statement """
    pass

# expression:


def p_expression_1(p):
    """expression : assignment_expression"""
    pass


def p_expression_2(p):
    """expression : expression COMMA assignment_expression"""
    pass

# assigment_expression:


def p_assignment_expression_1(p):
    """assignment_expression : conditional_expression"""
    pass


def p_assignment_expression_2(p):
    """assignment_expression : unary_expression assignment_operator assignment_expression"""
    pass

# assignment_operator:


def p_assignment_operator(p):
    """
    assignment_operator : EQUALS
                        | LSHIFTEQUAL
                        | RSHIFTEQUAL
                        | ANDEQUAL
                        | OREQUAL
                        | XOREQUAL
                        """
    pass

# conditional-expression


def p_conditional_expression_1(p):
    """conditional_expression : logical_or_expression"""
    pass


def p_conditional_expression_2(p):
    """conditional_expression : logical_or_expression CONDOP expression COLON conditional_expression """
    pass

# constant-expression


def p_constant_expression(p):
    """constant_expression : conditional_expression"""
    pass

# logical-or-expression


def p_logical_or_expression_1(p):
    """logical_or_expression : logical_and_expression"""
    pass


def p_logical_or_expression_2(p):
    """logical_or_expression : logical_or_expression LOR logical_and_expression"""
    pass

# logical-and-expression


def p_logical_and_expression_1(p):
    """logical_and_expression : inclusive_or_expression"""
    pass


def p_logical_and_expression_2(p):
    """logical_and_expression : logical_and_expression LAND inclusive_or_expression"""
    pass

# inclusive-or-expression:


def p_inclusive_or_expression_1(p):
    """inclusive_or_expression : exclusive_or_expression"""
    pass


def p_inclusive_or_expression_2(p):
    """inclusive_or_expression : inclusive_or_expression OR exclusive_or_expression"""
    pass

# exclusive-or-expression:


def p_exclusive_or_expression_1(p):
    """exclusive_or_expression :  and_expression"""
    pass


def p_exclusive_or_expression_2(p):
    """exclusive_or_expression :  exclusive_or_expression XOR and_expression"""
    pass

# AND-expression


def p_and_expression_1(p):
    """and_expression : equality_expression"""
    pass


def p_and_expression_2(p):
    """and_expression : and_expression AND equality_expression"""
    pass


# equality-expression:
def p_equality_expression_1(p):
    """equality_expression : relational_expression"""
    pass


def p_equality_expression_2(p):
    """equality_expression : equality_expression EQ relational_expression"""
    pass


def p_equality_expression_3(p):
    """equality_expression : equality_expression NE relational_expression"""
    pass


# relational-expression:
def p_relational_expression_1(p):
    """relational_expression : shift_expression"""
    pass


def p_relational_expression_2(p):
    """relational_expression : relational_expression LT shift_expression"""
    pass


def p_relational_expression_3(p):
    """relational_expression : relational_expression GT shift_expression"""
    pass


def p_relational_expression_4(p):
    """relational_expression : relational_expression LE shift_expression"""
    pass


def p_relational_expression_5(p):
    """relational_expression : relational_expression GE shift_expression"""
    pass

# shift-expression


def p_shift_expression_1(p):
    """shift_expression : additive_expression"""
    pass


def p_shift_expression_2(p):
    """shift_expression : shift_expression LSHIFT additive_expression"""
    pass


def p_shift_expression_3(p):
    """shift_expression : shift_expression RSHIFT additive_expression"""
    pass

# additive-expression


def p_additive_expression_1(p):
    """additive_expression : multiplicative_expression"""
    pass


def p_additive_expression_2(p):
    """additive_expression : additive_expression PLUS multiplicative_expression"""
    pass


def p_additive_expression_3(p):
    """additive_expression : additive_expression MINUS multiplicative_expression"""
    pass

# multiplicative-expression


def p_multiplicative_expression_1(p):
    """multiplicative_expression : cast_expression"""
    pass


def p_multiplicative_expression_2(p):
    """multiplicative_expression : multiplicative_expression STAR cast_expression"""
    pass


def p_multiplicative_expression_3(p):
    """multiplicative_expression : multiplicative_expression DIVIDE cast_expression"""
    pass

# cast-expression:


def p_cast_expression_1(p):
    """cast_expression : unary_expression"""
    pass


def p_cast_expression_2(p):
    """cast_expression : LPAREN type_name RPAREN cast_expression"""
    pass

# unary-expression:


def p_unary_expression_1(p):
    """unary_expression : postfix_expression"""
    pass


def p_unary_expression_4(p):
    """unary_expression : unary_operator cast_expression"""
    pass

# unary-operator


def p_unary_operator(p):
    """unary_operator : AND
                    | STAR
                    | PLUS
                    | MINUS
                    | NOT
                    | LNOT """
    pass

# postfix-expression:


def p_postfix_expression_1(p):
    """postfix_expression : primary_expression"""
    pass


def p_postfix_expression_2(p):
    """postfix_expression : postfix_expression LBRACKET expression RBRACKET"""
    pass


def p_postfix_expression_3(p):
    """postfix_expression : postfix_expression LPAREN argument_expression_list RPAREN"""
    pass


def p_postfix_expression_4(p):
    """postfix_expression : postfix_expression LPAREN RPAREN"""
    pass


def p_postfix_expression_5(p):
    """postfix_expression : postfix_expression PERIOD ID"""
    pass


# primary-expression:


def p_primary_expression(p):
    """primary_expression :  ID
                        |  constant
                        |  SCONST
                        |  LPAREN expression RPAREN"""
    pass

# argument-expression-list:


def p_argument_expression_list(p):
    """argument_expression_list :  assignment_expression
                              |  argument_expression_list COMMA assignment_expression"""
    pass

# constant:

def p_macro(p):
    """macro : SHARP IFNDEF ID"""
    p[0] = p[2]


def p_macro_1(p):
    """macro : SHARP DEFINE ID"""
    p[0] = p[2]


def p_macro_2(p):
    """macro : SHARP ENDIF"""
    pass


def p_header(p):
    """header : SHARP INCLUDE SCONST"""
    p[0] = p[3]


def p_header_2(p):
    """header : SHARP INCLUDE LT SCONST GT"""
    p[0] = p[4]


def p_constant(p):
    """constant : ICONST
               | FCONST
               | CCONST"""
    p[0] = p[1]


def p_empty(p):
    """empty : """
    pass


def p_error(p):
    print("Whoa. We're hosed")



ply_parser = yacc.yacc()

if __name__ == "__main__":

    sample_input = """
        #ifndef API_H
        #define API_H

        #include "toto.h"
        #include "titi.h"

        CustomStruct *new_args(int interval, int time, char *name, int pid, int stats);
        int super_func(float interval, int time, char *name, int pid, int stats);

        #endif // API_H"""
    ply_parser.parse(sample_input, debug=True)
