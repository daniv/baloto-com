from __future__ import annotations

from typing import TYPE_CHECKING

from core.cleo.io.outputs.output import Output
from core.cleo.io.outputs.output import Type
from core.cleo.io.outputs.output import Verbosity


if TYPE_CHECKING:
    from collections.abc import Iterable


class NullOutput(Output):
    ...