import re
from dataclasses import dataclass
from typing import Self

from src.domains.value.exceptions import InvalidCellValueError

_CELL_PATTERN = re.compile(r"^[A-Z]+[0-9]+$")


@dataclass(frozen=True, slots=True)
class LetterValue:
    value: str

    @classmethod
    def model_validate(cls, value: str) -> Self:
        if not _CELL_PATTERN.match(value):
            raise InvalidCellValueError(value, _CELL_PATTERN)
        return cls(value=value)

    def split(self) -> tuple[str, int]:
        """Разделяет A1 на (A, 1)"""
        alpha = "".join(c for c in self.value if c.isalpha())
        digit = int("".join(c for c in self.value if c.isdigit()))
        return alpha, digit

    def row(self) -> int:
        _, row = self.split()
        return row

    def column(self) -> int:
        col, _ = self.split()

        num = 0
        for c in col:
            num = num * 26 + (ord(c.upper()) - ord("A") + 1)
        return num

    def position(self) -> tuple[int, int]:
        return self.row(), self.column()
