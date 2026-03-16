from typing import Any

from src.domains.node.exceptions import (
    InvalidRangeEbdValueTypeError,
    InvalidRangeStartValueTypeError,
)
from src.domains.value import LetterValue, Value

from .base import ASTNode


class RangeNode(ASTNode):
    __slots__ = ("_end", "_start")

    _start: LetterValue
    _end: LetterValue

    def __init__(self, start: Value, end: Value) -> None:
        if not isinstance(start, LetterValue):
            raise InvalidRangeStartValueTypeError(start, LetterValue)
        if not isinstance(end, LetterValue):
            raise InvalidRangeEbdValueTypeError(end, LetterValue)

        self._start = start
        self._end = end

    @property
    def start(self) -> LetterValue:
        return self._start

    @property
    def end(self) -> LetterValue:
        return self._end

    def dump(self) -> dict[str, Any]:
        return {"RANGE": {"start": self._start, "end": self._end}}

    def expand(self) -> list[LetterValue]:
        s_pos = self._start.position()
        e_pos = self._end.position()

        return [
            LetterValue(f"{num_to_letters(col)}{row}")
            for col in range(s_pos[1], e_pos[1] + 1)
            for row in range(s_pos[0], e_pos[0] + 1)
        ]


def num_to_letters(num: int) -> str:
    """Конвертирует 1 -> 'A', 27 -> 'AA'"""

    letters = ""
    while num > 0:
        num -= 1
        letters = chr(num % 26 + ord("A")) + letters
        num //= 26
    return letters
