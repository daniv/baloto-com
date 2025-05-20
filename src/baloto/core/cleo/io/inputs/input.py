from __future__ import annotations

import re

from typing import Any
from typing import TextIO

from baloto.core.cleo._compat import shell_quote
from baloto.core.cleo.exceptions import CleoMissingArgumentsError
from baloto.core.cleo.exceptions import CleoValueError
from baloto.core.cleo.io.inputs.definition import Definition


class Input:
    """
    This class is the base class for concrete Input implementations.
    """

    def __init__(self, definition: Definition | None = None) -> None: ...
