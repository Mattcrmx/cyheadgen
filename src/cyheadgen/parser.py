"""A wrapper for the PLY parser."""

from typing import List

from cyheadgen.ast import Node

from ._parser import ply_parser


class CyHeadGenParser:
    """The Parser Wrapper Class."""

    def __init__(self):
        """The initialization method."""
        self._parser = ply_parser

    def __call__(self, data: str, **kwargs) -> List[Node]:
        """Parse the input string.

        Args:
            data: the input string
            kwargs: the kwargs to pass to the yacc parser

        Returns:
            the parsed input string.
        """
        return self._parser.parse(data, **kwargs)

    @classmethod
    def parse_file(cls, file_path: str, **kwargs) -> List[Node]:
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
