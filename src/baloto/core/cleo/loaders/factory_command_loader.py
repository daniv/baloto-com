from __future__ import annotations

from collections.abc import Callable

from baloto.core.cleo.commands.command import Command
from baloto.core.cleo.exceptions import CleoCommandNotFoundError
from baloto.core.cleo.loaders.command_loader import CommandLoader


Factory = Callable[[], Command]


class FactoryCommandLoader(CommandLoader):
    """
    A simple command loader using factories to instantiate commands lazily.
    """

    def __init__(self, factories: dict[str, Factory]) -> None:
        self._factories = factories

    @property
    def names(self) -> list[str]:
        return list(self._factories)

    def has(self, name: str) -> bool:
        return name in self._factories

    def get(self, name: str) -> Command:
        if name not in self._factories:
            raise CleoCommandNotFoundError(name)

        return self._factories[name]()
