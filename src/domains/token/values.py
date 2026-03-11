import re
from typing import Self

from .enums import (
    FirstPriorityOperatorsEnum,
    FormulaCharsEnum,
    FunctionsEnum,
    SecondPriorityOperatorsEnum,
)
from .exceptions import (
    InvalidCellValueError,
    InvalidFormulaCharValueError,
    InvalidFunctionValueError,
    InvalidNumberValueError,
    InvalidOperatorValueError,
)

_CELL_PATTERN = re.compile(r"^[A-Z]+[0-9]+$")


class Value:
    __slots__ = ("_value",)

    @property
    def value(self) -> None:
        return None


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


class LetterValue(Value):
    def __init__(self, value: str) -> None:
        if not _CELL_PATTERN.match(value):
            raise InvalidCellValueError(value, _CELL_PATTERN)

        self._value = value

    @property
    def value(self) -> str:
        return self._value


class OperatorValue(Value):
    def __init__(self, value: str) -> None:
        if value in FirstPriorityOperatorsEnum.values_set():
            self._value = FirstPriorityOperatorsEnum(value)
        elif value in SecondPriorityOperatorsEnum.values_set():
            self._value = SecondPriorityOperatorsEnum(value)
        else:
            raise InvalidOperatorValueError(value)

    @property
    def value(self) -> FirstPriorityOperatorsEnum | SecondPriorityOperatorsEnum:
        return self._value


class FunctionValue(Value):
    def __init__(self, value: str) -> None:
        functions = FunctionsEnum.values_set()
        if value not in functions:
            raise InvalidFunctionValueError(value, functions)

        self._value = FunctionsEnum(value)

    @property
    def value(self) -> FunctionsEnum:
        return self._value


class FormulaCharValue(Value):
    def __init__(self, value: str) -> None:
        functions = FormulaCharsEnum.values_set()
        if value not in functions:
            raise InvalidFormulaCharValueError(value, functions)

        self._value = FormulaCharsEnum(value)

    @property
    def value(self) -> FormulaCharsEnum:
        return self._value
