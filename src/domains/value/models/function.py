from src.domains.value.enums import FunctionsEnum
from src.domains.value.exceptions import InvalidFunctionValueError

from .base import Value


class FunctionValue(Value):
    __slots__ = ("_value",)

    def __init__(self, value: str) -> None:
        functions = FunctionsEnum.values_set()
        if value not in functions:
            raise InvalidFunctionValueError(value, functions)

        self._value = FunctionsEnum(value)

    @property
    def value(self) -> FunctionsEnum:
        return self._value

    def __repr__(self) -> str:
        return self._value.name
