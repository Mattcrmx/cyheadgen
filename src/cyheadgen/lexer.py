"""A wrapper for the PLY lexer."""
from ._lexer import ply_lexer


class CyHeadGenLexer:
    """The Lexer Wrapper Class."""
    def __init__(self):
        """The initialization method."""
        self._lexer = ply_lexer

    def __call__(self, data: str):
        """Lex the input string.

        Args:
            data: the input string

        Returns:
            the tokenized input string.
        """
        tokens = []
        self._lexer.input(data)
        while True:
            tok = self._lexer.token()
            if not tok:
                break
            tokens.append(tok)
        return tokens

    @classmethod
    def tokenize_from_file(cls, file_path: str):
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


cyheadgen_lexer = CyHeadGenLexer()
