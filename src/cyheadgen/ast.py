"""AST module."""

from dataclasses import dataclass
from enum import Enum
from typing import List, Literal, Optional


class Type(str, Enum):
    """C types."""

    INT = "int"
    FLOAT = "float"
    LONG = "long"
    LONG_LONG = "long long"
    VOID = "void"
    CHAR = "char"


@dataclass(frozen=True)
class Header:
    """Header Node."""

    name: str
    type: Literal["custom", "standard"]

    def expand(self):
        """Expand included header."""
        pass


@dataclass(frozen=True)
class Macro:
    """Macro Node."""

    name: Optional[str]
    type: Literal["ifndef", "def", "endif"]


@dataclass
class Argument:
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
class CEnum:
    """Enum Node."""

    name: str
    attributes: List[Argument]


@dataclass
class Function:
    """Function Node."""

    name: str
    type: str
    parameters: List[Argument]
