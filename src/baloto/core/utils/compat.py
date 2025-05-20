from __future__ import annotations

import locale
import sys
from importlib import metadata

from contextlib import suppress

WINDOWS = sys.platform == "win32"


def decode(string: bytes | str, encodings: list[str] | None = None) -> str:
    if not isinstance(string, bytes):
        return string

    encodings = encodings or ["utf-8", "latin1", "ascii"]

    for encoding in encodings:
        with suppress(UnicodeEncodeError, UnicodeDecodeError):
            return string.decode(encoding)

    return string.decode(encodings[0], errors="ignore")


def encode(string: str, encodings: list[str] | None = None) -> bytes:
    if isinstance(string, bytes):
        return string

    encodings = encodings or ["utf-8", "latin1", "ascii"]

    for encoding in encodings:
        with suppress(UnicodeEncodeError, UnicodeDecodeError):
            return string.encode(encoding)

    return string.encode(encodings[0], errors="ignore")


def getencoding() -> str:
    if sys.version_info < (3, 11):
        return locale.getpreferredencoding()
    else:
        return locale.getencoding()


__all__ = [
    "WINDOWS",
    "decode",
    "encode",
    "getencoding",
    "metadata",
]
