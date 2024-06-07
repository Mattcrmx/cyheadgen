"""A wrapper for the PLY parser."""

from __future__ import annotations

from cyheadgen._parser import ply_parser  # type: ignore[attr-defined]
from cyheadgen.ast import Node


class CyHeadGenParser:
    """The Parser Wrapper Class."""

    def __init__(self) -> None:
        """The initialization method."""
        self._parser = ply_parser

    def __call__(self, data: str, **kwargs: str | bool) -> list[Node]:
        """Parse the input string.

        Args:
            data: the input string
            kwargs: the kwargs to pass to the yacc parser

        Returns:
            the parsed input string.
        """
        result: list[Node] = self._parser.parse(data, **kwargs)  # mypy needs some help
        # parse from bottom up so we need to reverse to have the correct order
        return result[::-1]

    @classmethod
    def parse_file(cls, file_path: str, **kwargs: str | bool) -> list[Node]:
        """Lex the content of a file.

        Args:
            file_path: the path to the file
            kwargs: the kwargs to pass to the yacc parser

        Returns:
            the file parsed
        """
        parser = cls()
        with open(file_path) as f:
            data = f.read()
        return parser(data, **kwargs)
