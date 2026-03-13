from typing import Self

from src.domains.values.enums import FormulaCharsEnum
from src.domains.values.exceptions import InvalidNumberValueError

from .base import Value


class NumberValue(Value):
    def __init__(self, value: float | int = 0) -> None:
        self._value = value

    @classmethod
    def from_str(cls, value: str) -> Self:
        try:
            v = float(value) if FormulaCharsEnum.DOT in value else int(value)
        except (ValueError, TypeError) as e:
            raise InvalidNumberValueError from e

        return cls(v)

    @property
    def value(self) -> float | int:
        return self._value

    def __repr__(self) -> str:
        return str(self._value)
