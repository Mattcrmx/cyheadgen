import pytest
from cyheadgen.ast import Argument, Function, Header, Macro
from cyheadgen.parser import CyHeadGenParser


@pytest.fixture
def parser():
    return CyHeadGenParser()


@pytest.mark.parametrize(
    "inp,res",
    [
        ("#ifndef API_H", [Macro(name="API_H", type="ifndef")]),
        ("#define API_H", [Macro(name="API_H", type="define")]),
        ('#include "toto.h"', [Header(name="toto.h", type="custom")]),
        ("#include <titi.h>", [Header(name="titi", type="standard")]),
        (
            "CustomStruct *new_args(int interval, int time, char *name, int pid, int stats);",
            [
                Function(
                    name="new_args",
                    type="*CustomStruct",
                    parameters=[
                        Argument(name="interval", type="int", value=None),
                        Argument(name="time", type="int", value=None),
                        Argument(name="name", type="char*", value=None),
                        Argument(name="pid", type="int", value=None),
                        Argument(name="stats", type="int", value=None),
                    ],
                )
            ],
        ),
        (
            "int super_func(float interval, int time, char *name, int pid, int stats);",
            [
                Function(
                    name="super_func",
                    type="int",
                    parameters=[
                        Argument(name="interval", type="float", value=None),
                        Argument(name="time", type="int", value=None),
                        Argument(name="name", type="char*", value=None),
                        Argument(name="pid", type="int", value=None),
                        Argument(name="stats", type="int", value=None),
                    ],
                )
            ],
        ),
        ("#endif // API_H", [Macro(name=None, type="endif")]),
    ],
)
def test_parse_func(parser, inp, res):
    assert parser(inp) == res
