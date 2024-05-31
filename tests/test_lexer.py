"""Test lexer cases."""

from typing import List

import pytest
from cyheadgen import CyHeadGenLexer


@pytest.fixture  # type: ignore[misc]
def lexer() -> CyHeadGenLexer:
    return CyHeadGenLexer()


@pytest.mark.parametrize(
    "inp,res",
    [
        ("#ifndef API_H", ["#", "ifndef", "API_H"]),
        ("#define API_H", ["#", "define", "API_H"]),
        ('#include "toto.h"', ["#", "include", '"toto.h"']),
        ("#include <titi.h>", ["#", "include", "<", "titi", ".", "h", ">"]),
        (
            "CustomStruct *new_args(int interval, int time, char *name, int pid, int stats);",
            [
                "CustomStruct",
                "*",
                "new_args",
                "(",
                "int",
                "interval",
                ",",
                "int",
                "time",
                ",",
                "char",
                "*",
                "name",
                ",",
                "int",
                "pid",
                ",",
                "int",
                "stats",
                ")",
                ";",
            ],
        ),
        (
            "int super_func(float interval, int time, char *name, int pid, int stats);",
            [
                "int",
                "super_func",
                "(",
                "float",
                "interval",
                ",",
                "int",
                "time",
                ",",
                "char",
                "*",
                "name",
                ",",
                "int",
                "pid",
                ",",
                "int",
                "stats",
                ")",
                ";",
            ],
        ),
        ("#endif // API_H", ["#", "endif"]),  # test the comment discard
    ],
)  # type: ignore[misc]
def test_lexer(lexer: CyHeadGenLexer, inp: str, res: List[str]) -> None:
    tokens = lexer(inp)
    assert [t.value for t in tokens] == res


def test_separated_statements(lexer: CyHeadGenLexer) -> None:
    inp = """
    #infdef API_H
    #define API_H

    #include <titi.h>
    """

    assert [tok.value for tok in lexer(inp)] == [
        "#",
        "infdef",
        "API_H",
        "#",
        "define",
        "API_H",
        "#",
        "include",
        "<",
        "titi",
        ".",
        "h",
        ">",
    ]


def test_multiline_comment(lexer: CyHeadGenLexer) -> None:
    inp = """
    #ifndef TOTO_H
    #define TOTO_H
    /* Super comment wow such good */
    #endif // TOTO_H
    """
    assert [tok.value for tok in lexer(inp)] == [
        "#",
        "ifndef",
        "TOTO_H",
        "#",
        "define",
        "TOTO_H",
        "#",
        "endif",
        "TOTO_H",
    ]
