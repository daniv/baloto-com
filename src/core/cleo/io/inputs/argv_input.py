from __future__ import annotations

import sys

from typing import TYPE_CHECKING
from typing import Any

from core.cleo.exceptions import CleoNoSuchOptionError
from core.cleo.exceptions import CleoRuntimeError
from core.cleo.io.inputs.input import Input


if TYPE_CHECKING:
    from core.cleo.io.inputs.definition import Definition


class ArgvInput(Input):
    """
    Represents an input coming from the command line.
    """

    def __init__(
        self, argv: list[str] | None = None, definition: Definition | None = None
    ) -> None:
        ...