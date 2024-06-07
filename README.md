# CyHeadGen


## About

`CyHeadGen` is a project aimed at simplifying the process of converting C header files into Cython files.
It uses a lexer and a parser based on the Lex/Yacc python implementation with [`ply`](https://github.com/dabeaz/ply).

## Usage
`cyheadgen` exposes the C header lexing and parsing APIs with wrapper classes

### Lexing

The lexer returns `LexToken` which are the token produced by the ply parser, but it's pretty easy to access
the symbol corresponding to the token.
```python
from cyheadgen import CyHeadGenLexer
lexer = CyHeadGenLexer()

my_func = "int super_func(int arg1, int *arg2);"
print([tok.value for tok in lexer(my_func)])  # ['int', 'super_func', '(', 'int', 'arg1', ',', 'int', '*', 'arg2', ')', ';']
```

### Parsing

The parser returns the Node associated with the parsing, all abstraction are easily tweakable and their behaviour
can be change at will.
```python
from cyheadgen import CyHeadGenParser
parser = CyHeadGenParser()

my_func = "int super_func(int arg1, int *arg2);"
print(parser(my_func))  # [Function(name='super_func', type='int', parameters=[Argument(name='arg1', type='int', value=None), Argument(name='arg2', type='int*', value=None)])]
```

### Generation

The Generator is built on the two previous structures, and supports generating cython headers from an input string or
from a header file.
```python
from cyheadgen import CythonHeaderGenerator
cygen = CythonHeaderGenerator()

my_func = "int super_func(int arg1, int *arg2);"
print(cygen(my_func, header_name="toto.h"))  # "int super_func(int arg1, int *arg2)"

print(cygen.generate_from_file(filepath="./toto.h"))
```
