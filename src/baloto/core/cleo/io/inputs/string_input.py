from __future__ import annotations

from core.cleo.helpers import tokenize
from core.cleo.io.inputs.argv_input import ArgvInput


class StringInput(ArgvInput):
    """
    Represents an input provided as a string
    """

    def __init__(self, input: str) -> None:
        super().__init__([])

    def _tokenize(self, input: str) -> list[str]: ...
