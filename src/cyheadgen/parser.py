"""A wrapper for the PLY parser."""

from ._parser import ply_parser


class CyHeadGenParser:
    """The Parser Wrapper Class."""

    def __init__(self):
        """The initialization method."""
        self._parser = ply_parser

    def __call__(self, data: str):
        """Lex the input string.

        Args:
            data: the input string

        Returns:
            the tokenized input string.
        """
        tokens = []
        self._parser.input(data)
        while True:
            tok = self._parser.token()
            if not tok:
                break
            tokens.append(tok)
        return tokens

    @classmethod
    def parse_file(cls, file_path: str):
        """Lex the content of a file.

        Args:
            file_path: the path to the file

        Returns:
            the tokens corresponding to the file
        """
        lexer = cls()
        with open(file_path) as f:
            data = f.read()
        return lexer(data)


cyheadgen_parser = CyHeadGenParser()
