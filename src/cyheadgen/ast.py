"""AST module."""

from dataclasses import dataclass
from enum import Enum
from typing import List, Literal, Optional


def _resolve_type(value: str) -> str:
    """Resolve the type based on the value."""
    if '"' in value:
        return Type.CHAR
    if "." in value:
        return Type.FLOAT
    if 32767 < abs(int(value)) < 2147483647:
        return Type.LONG
    if abs(int(value)) > 2147483647:
        return Type.LONG_LONG

    return Type.INT


class Node:
    """Node class."""

    pass


class Type(str, Enum):
    """C types."""

    INT = "int"
    FLOAT = "float"
    LONG = "long"
    LONG_LONG = "long long"
    VOID = "void"
    CHAR = "char"


@dataclass
class Header(Node):
    """Header Node."""

    name: str
    type: Literal["custom", "standard"]

    def __post_init__(self) -> None:
        """Initialize the name."""
        if self.type == "custom":
            self.name = self.name.strip('"')

    def expand(self) -> None:
        """Expand included header."""
        pass


@dataclass(frozen=True)
class Macro(Node):
    """Macro Node."""

    name: Optional[str]
    type: Literal["ifndef", "define", "endif"]


@dataclass
class Argument(Node):
    """Abstraction for an argument."""

    name: str
    type: str = "int"
    value: Optional[str] = None

    def __post_init__(self) -> None:
        """Initialize the type."""
        if self.value is not None:
            self.type = _resolve_type(value=self.value)


@dataclass(frozen=True)
class CEnum(Node):
    """Enum Node."""

    name: str
    attributes: List[Argument]


@dataclass
class Function(Node):
    """Function Node."""

    name: str
    type: str
    parameters: List[Argument]
