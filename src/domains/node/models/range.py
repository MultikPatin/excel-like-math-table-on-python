from dataclasses import dataclass
from typing import Any, Self

from src.domains.node.exceptions import (
    InvalidRangeEbdValueTypeError,
    InvalidRangeStartValueTypeError,
)
from src.domains.value import LetterValue


@dataclass(frozen=True, slots=True)
class RangeNode:
    start: LetterValue
    end: LetterValue

    @classmethod
    def model_validate(cls, start: Any, end: Any) -> Self:  # noqa: ANN401
        if not isinstance(start, LetterValue):
            raise InvalidRangeStartValueTypeError(start, LetterValue)
        if not isinstance(end, LetterValue):
            raise InvalidRangeEbdValueTypeError(end, LetterValue)
        return cls(start=start, end=end)

    def expand(self) -> list[LetterValue]:
        s_pos = self.start.position()
        e_pos = self.end.position()

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
