from typing import Self

from src.domains.values.enums import FormulaCharsEnum
from src.domains.values.exceptions import InvalidNumberValueError

from .base import Value


class NumberValue(Value, float):
    # def __init__(self, value: float | int = 0) -> None:
    #     self._value = value

    @classmethod
    def from_str(cls, value: str) -> Self:
        try:
            v = float(value) if FormulaCharsEnum.DOT in value else int(value)
        except (ValueError, TypeError) as e:
            raise InvalidNumberValueError from e

        return cls(v)

    # @property
    # def value(self) -> float | int:
    #     return self._value

    #
    # def __repr__(self) -> str:
    #     return str(self._value)
    #
    # def __add__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         return NumberValue(self.value + other.value)
    #     if isinstance(other, (int, float)):
    #         return NumberValue(self.value + other)
    #     raise NotImplementedError
    #
    # def __radd__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         return NumberValue(other.value + self.value)
    #     if isinstance(other, (int, float)):
    #         return NumberValue(other + self.value)
    #     raise NotImplementedError
    #
    # def __iadd__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         self._value += other.value
    #         return self
    #     if isinstance(other, (int, float)):
    #         self._value += other
    #         return self
    #     raise NotImplementedError
    #
    # def __sub__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         return NumberValue(self.value - other.value)
    #     if isinstance(other, (int, float)):
    #         return NumberValue(self.value - other)
    #     raise NotImplementedError
    #
    # def __rsub__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         return NumberValue(other.value - self.value)
    #     if isinstance(other, (int, float)):
    #         return NumberValue(other - self.value)
    #     raise NotImplementedError
    #
    # def __isub__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         self._value -= other.value
    #         return self
    #     if isinstance(other, (int, float)):
    #         self._value -= other
    #         return self
    #     raise NotImplementedError
    #
    # def __mul__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         return NumberValue(self.value * other.value)
    #     if isinstance(other, (int, float)):
    #         return NumberValue(self.value * other)
    #     raise NotImplementedError
    #
    # def __rmul__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         return NumberValue(other.value * self.value)
    #     if isinstance(other, (int, float)):
    #         return NumberValue(other * self.value)
    #     raise NotImplementedError
    #
    # def __imul__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         self._value *= other.value
    #         return self
    #     if isinstance(other, (int, float)):
    #         self._value *= other
    #         return self
    #     raise NotImplementedError
    #
    # def __truediv__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         return NumberValue(self.value / other.value)
    #     if isinstance(other, (int, float)):
    #         return NumberValue(self.value / other)
    #     raise NotImplementedError
    #
    # def __rtruediv__(self, other: object) -> "NumberValue":
    #     if isinstance(other, NumberValue):
    #         return NumberValue(other.value / self.value)
    #     if isinstance(other, (int, float)):
    #         return NumberValue(other / self.value)
    #     raise NotImplementedError
    #
    # def __eq__(self, other: object) -> bool:
    #     if isinstance(other, NumberValue):
    #         return self.value == other.value
    #     if isinstance(other, (int, float)):
    #         return self.value == other
    #     return False
    #
    # def __hash__(self) -> int:
    #     return hash(self._value)
