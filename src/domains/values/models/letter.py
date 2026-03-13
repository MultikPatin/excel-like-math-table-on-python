import re

from src.domains.values.exceptions import InvalidCellValueError

from .base import Value

_CELL_PATTERN = re.compile(r"^[A-Z]+[0-9]+$")


class LetterValue(Value):
    def __init__(self, value: str) -> None:
        if not _CELL_PATTERN.match(value):
            raise InvalidCellValueError(value, _CELL_PATTERN)

        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def split(self) -> tuple[str, int]:
        """Разделяет A1 на (A, 1)"""
        alpha = "".join(c for c in self._value if c.isalpha())
        digit = int("".join(c for c in self._value if c.isdigit()))
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

    def __eq__(self, other) -> bool:  # noqa: ANN001
        if not isinstance(other, LetterValue):
            return False
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return self._value
