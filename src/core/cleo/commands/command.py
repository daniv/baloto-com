from __future__ import annotations

import inspect

from typing import TYPE_CHECKING
from typing import Any
from typing import ClassVar
from typing import cast

from core.cleo.exceptions import CleoError
from core.cleo.formatters.style import Style
from core.cleo.io.inputs.definition import Definition
from core.cleo.io.inputs.string_input import StringInput
from core.cleo.io.null_io import NullIO
from core.cleo.io.outputs.output import Verbosity
from core.cleo.ui.table_separator import TableSeparator


if TYPE_CHECKING:
    from contextlib import AbstractContextManager
    from typing import Literal

    from core.cleo.application import Application
    from core.cleo.io.inputs.argument import Argument
    from core.cleo.io.inputs.option import Option
    from core.cleo.io.io import IO
    from core.cleo.ui.progress_bar import ProgressBar
    from core.cleo.ui.progress_indicator import ProgressIndicator
    from core.cleo.ui.question import Question
    from core.cleo.ui.table import Rows
    from core.cleo.ui.table import Table


class Command:
    arguments: ClassVar[list[Argument]] = []
    options: ClassVar[list[Option]] = []
    aliases: ClassVar[list[str]] = []
    usages: ClassVar[list[str]] = []
    commands: ClassVar[list[Command]] = []
    name: str | None = None

    description = ""

    help = ""

    enabled = True
    hidden = False

    def __init__(self) -> None:
        self._io: IO | None = None
        self._definition = Definition()
        self._full_definition: Definition | None = None
        self._application: Application | None = None
        self._ignore_validation_errors = False
        self._synopsis: dict[str, str] = {}

        self.configure()

        for i, usage in enumerate(self.usages):
            if self.name and not usage.startswith(self.name):
                self.usages[i] = f"{self.name} {usage}"