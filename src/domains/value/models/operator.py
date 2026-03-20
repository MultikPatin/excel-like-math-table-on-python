from dataclasses import dataclass
from typing import Self

from src.domains.value.enums import (
    FirstPriorityOperatorsEnum,
    SecondPriorityOperatorsEnum,
)
from src.domains.value.exceptions import InvalidOperatorValueError


@dataclass(frozen=True, slots=True)
class OperatorValue:
    value: FirstPriorityOperatorsEnum | SecondPriorityOperatorsEnum

    @classmethod
    def model_validate(cls, value: str) -> Self:
        if value in FirstPriorityOperatorsEnum.values_set():
            return cls(value=FirstPriorityOperatorsEnum(value))
        if value in SecondPriorityOperatorsEnum.values_set():
            return cls(value=SecondPriorityOperatorsEnum(value))
        raise InvalidOperatorValueError(value)

    @property
    def is_priority(self) -> bool:
        return isinstance(self.value, FirstPriorityOperatorsEnum)
