from __future__ import annotations

import re

from typing import Any
from typing import TextIO

from core.cleo._compat import shell_quote
from core.cleo.exceptions import CleoMissingArgumentsError
from core.cleo.exceptions import CleoValueError
from core.cleo.io.inputs.definition import Definition


class Input:
    """
    This class is the base class for concrete Input implementations.
    """

    def __init__(self, definition: Definition | None = None) -> None:
        ...