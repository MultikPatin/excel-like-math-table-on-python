from src.domains.values.enums import FunctionsEnum
from src.domains.values.exceptions import InvalidFunctionValueError

from .base import Value


class FunctionValue(Value):
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
