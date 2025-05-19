from __future__ import annotations

from typing import TYPE_CHECKING

from core.cleo.io.outputs.output import Type as OutputType
from core.cleo.io.outputs.output import Verbosity


if TYPE_CHECKING:
    from collections.abc import Iterable

    from core.cleo.io.inputs.input import Input
    from core.cleo.io.outputs.output import Output
    from core.cleo.io.outputs.section_output import SectionOutput


class IO:
    def __init__(self, input: Input, output: Output, error_output: Output) -> None:
        self._input = input
        self._output = output
        self._error_output = error_output

    @property
    def input(self) -> Input:
        return self._input

    @input.setter
    def input(self, input: Input) -> None:
        self._input = input

    @property
    def output(self) -> Output:
        return self._output

    @property
    def error_output(self) -> Output:
        return self._error_output

    @property
    def interactive(self) -> bool:
        return self._input.is_interactive()

    @interactive.setter
    def interactive(self, interactive: bool = True) -> None:
        self._input.interactive(interactive)

    @property
    def decorated(self) -> bool:
        return self._output.is_decorated()

    @decorated.setter
    def decorated(self, decorated: bool = True) -> None:
        self._output.decorated(decorated)
        self._error_output.decorated(decorated)

    @property
    def supports_utf8(self) -> bool:
        return self._output.supports_utf8()

    def read(self, length: int, default: str = "") -> str:
        """
        Reads the given amount of characters from the input stream.
        """

    def read_line(self, length: int = -1, default: str = "") -> str:
        """
        Reads a line from the input stream.
        """

    def write_line(
            self,
            messages: str | Iterable[str],
            verbosity: Verbosity = Verbosity.NORMAL,
            type: OutputType = OutputType.NORMAL,
    ) -> None:
        ...

    def write(
            self,
            messages: str | Iterable[str],
            new_line: bool = False,
            verbosity: Verbosity = Verbosity.NORMAL,
            type: OutputType = OutputType.NORMAL,
    ) -> None:
        ...

    def write_error_line(
            self,
            messages: str | Iterable[str],
            verbosity: Verbosity = Verbosity.NORMAL,
            type: OutputType = OutputType.NORMAL,
    ) -> None:
        ...

    def write_error(
            self,
            messages: str | Iterable[str],
            new_line: bool = False,
            verbosity: Verbosity = Verbosity.NORMAL,
            type: OutputType = OutputType.NORMAL,
    ) -> None:
        ...

    def overwrite(self, messages: str | Iterable[str]) -> None:
        ...

    def overwrite_error(self, messages: str | Iterable[str]) -> None:
        ...

    def flush(self) -> None:
        ...

    def set_verbosity(self, verbosity: Verbosity) -> None:
        self._output.set_verbosity(verbosity)
        self._error_output.set_verbosity(verbosity)

    def is_verbose(self) -> bool:
        return self.output.is_verbose()

    def is_very_verbose(self) -> bool:
        return self.output.is_very_verbose()

    def is_debug(self) -> bool:
        return self.output.is_debug()

    def with_input(self, input: Input) -> IO:
        ...

    def remove_format(self, text: str) -> str:
        ...

    def section(self) -> SectionOutput:
        ...