from src.domains.value.enums import FormulaCharsEnum
from src.domains.value.exceptions import InvalidFormulaCharValueError

from .base import Value


class FormulaCharValue(Value):
    __slots__ = ("_value",)

    def __init__(self, value: str) -> None:
        functions = FormulaCharsEnum.values_set()
        if value not in functions:
            raise InvalidFormulaCharValueError(value, functions)

        self._value = FormulaCharsEnum(value)

    @property
    def value(self) -> FormulaCharsEnum:
        return self._value

    def __repr__(self) -> str:
        return self._value.value
