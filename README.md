# CyHeadGen

`CyHeadGen` is a project aimed at simplifying the process of converting C header files into Cython files. It includes a lexer, parser, and converter designed specifically for this purpose. The project utilizes PLY, a Python Lex-Yacc implementation, to provide robust lexical and syntactic analysis of C header files.

**NB:** This work is heavily inspired by the great ansi c [lexer](https://github.com/dabeaz/ply/blob/master/example/ansic/clex.py)/[parser](https://github.com/dabeaz/ply/blob/master/example/ansic/cparse.py) from the PLY repo,
since the C header grammar is mostly the same as the C language grammar.
