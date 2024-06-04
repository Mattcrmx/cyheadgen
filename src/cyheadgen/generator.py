"""The Cython header generator."""

from __future__ import annotations

from cyheadgen.ast import Node
from cyheadgen.lexer import CyHeadGenLexer
from cyheadgen.parser import CyHeadGenParser


def _generate_from_productions(productions: list[Node], header_name: str) -> str:
    """Generate cython header from a list of parser productions.

    Args:
        header_name: the header name.
        productions: the parser productions.

    Returns:
        The cython representation.
    """
    cython_header = f'cdef extern from "{header_name}":\n'

    for prod in productions:
        cython_repr = f"\t{prod.representation}\n" if prod.representation != "" else ""
        cython_header += cython_repr

    return cython_header


class CythonHeaderGenerator:
    """The Generator class."""

    def __init__(
        self, lexer: CyHeadGenLexer | None = None, parser: CyHeadGenParser | None = None
    ) -> None:
        """Initialization method."""
        self.lexer = lexer or CyHeadGenLexer()
        self.parser = parser or CyHeadGenParser()

    def __call__(self, data: str, header_name: str) -> str:
        """Generate the cython representation from the C header.

        Args:
            data: the data to translate to cython
            header_name: the name of the header from which to include the parsed data.

        Returns:
            The cython representation.
        """
        productions = self.parser(data)
        return _generate_from_productions(productions, header_name)

    def generate_from_file(self, filepath: str) -> str:
        """Generate the cython representation from the file.

        Args:
            filepath: the path to the header file

        Returns:
            the generated header
        """
        productions = self.parser.parse_file(filepath)
        return _generate_from_productions(productions, filepath)
