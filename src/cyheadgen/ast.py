"""AST module."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Literal


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

    @property
    def representation(self) -> str:
        """The Node representation in cython."""
        return ""


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

    name: str | None
    type: Literal["ifndef", "define", "endif"]


@dataclass
class Argument(Node):
    """Abstraction for an argument."""

    name: str
    type: str = "int"
    value: str | None = None

    def __post_init__(self) -> None:
        """Initialize the type."""
        if self.value is not None:
            self.type = _resolve_type(value=self.value)

    @property
    def representation(self) -> str:
        """The Argument representation."""
        base_repr = f"{self.type} {self.name}"
        if self.value is not None:
            base_repr += f"= {self.value}"
        return base_repr


@dataclass(frozen=True)
class CEnum(Node):
    """Enum Node."""

    name: str
    attributes: list[Argument]

    @property
    def representation(self) -> str:
        """Cython representation for an Enum."""
        attributes = "\n".join([f"\t{attr.representation}" for attr in self.attributes])
        return f"cdef enum {self.name}:\n{attributes}\n"


@dataclass
class CStruct(Node):
    """C struct type."""

    name: str
    attributes: list[Argument]

    @property
    def representation(self) -> str:
        """Cython representation for a Struct."""
        attributes = "\n".join([f"\t{attr.representation}" for attr in self.attributes])
        return f"cdef struct {self.name}:\n{attributes}\n"


@dataclass
class Function(Node):
    """Function Node."""

    name: str
    type: str
    parameters: list[Argument] | str

    @property
    def representation(self) -> str:
        """The function representation."""
        if isinstance(self.parameters, str):
            params = ""
        else:
            params = ", ".join([p.representation for p in self.parameters])

        return f"{self.type} {self.name}({params})"
