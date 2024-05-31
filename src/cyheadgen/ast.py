"""AST module."""

from dataclasses import dataclass
from enum import Enum
from typing import List, Literal, Optional


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

    def __post_init__(self):
        """Initialize the name."""
        if self.type == "custom":
            self.name = self.name.strip('"')

    def expand(self):
        """Expand included header."""
        pass


@dataclass(frozen=True)
class Macro(Node):
    """Macro Node."""

    name: Optional[str]
    type: Literal["ifndef", "def", "endif"]


@dataclass
class Argument(Node):
    """Abstraction for an argument."""

    name: str
    type: Type = "int"
    value: Optional[str] = None

    def __post_init__(self):
        """Initialize the type."""
        if self.value:
            self.type = self._resolve_type()

    def _resolve_type(self) -> Type:
        """Resolve the type based on the value."""
        if '"' in self.value:
            return Type.CHAR
        if "." in self.value:
            return Type.FLOAT
        if 32767 < abs(int(self.value)) < 2147483647:
            return Type.LONG
        if abs(int(self.value)) > 2147483647:
            return Type.LONG_LONG

        return Type.INT


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
