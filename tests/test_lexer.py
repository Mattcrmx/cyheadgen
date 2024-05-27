from cyheadgen import cyheadgen_lexer


def test_lexer():
    sample_input = """
    #ifndef API_H
    #define API_H
    
    #include "toto.h"
    #include "titi.h"
    
    CustomStruct *new_args(int interval, int time, char *name, int pid, int stats);
    int super_func(float interval, int time, char *name, int pid, int stats);
    
    #endif // API_H"""
    tokens = cyheadgen_lexer(sample_input)
    print(tokens)