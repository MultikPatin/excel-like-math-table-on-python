from dataclasses import dataclass
from typing import Self

from src.domains.value.enums import FunctionsEnum
from src.domains.value.exceptions import InvalidFunctionValueError


@dataclass(frozen=True, slots=True)
class FunctionValue:
    value: FunctionsEnum

    @classmethod
    def model_validate(cls, value: str) -> Self:
        functions = FunctionsEnum.values_set()
        if value not in functions:
            raise InvalidFunctionValueError(value, functions)
        return cls(value=FunctionsEnum(value))
