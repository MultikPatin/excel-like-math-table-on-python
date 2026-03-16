from src.domains.value.enums import (
    FirstPriorityOperatorsEnum,
    SecondPriorityOperatorsEnum,
)
from src.domains.value.exceptions import InvalidOperatorValueError

from .base import Value


class OperatorValue(Value):
    __slots__ = ("_value",)

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

    @property
    def is_priority(self) -> bool:
        return isinstance(self._value, FirstPriorityOperatorsEnum)

    def __repr__(self) -> str:
        return self._value.name
