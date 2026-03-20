from dataclasses import dataclass
from typing import Any, Self

from src.domains.node.exceptions import InvalidNumberValueTypeError
from src.domains.value import NumberValue


@dataclass(frozen=True, slots=True)
class NumberNode:
    number: NumberValue

    @classmethod
    def model_validate(cls, number: Any) -> Self:  # noqa: ANN401
        if not isinstance(number, NumberValue):
            raise InvalidNumberValueTypeError(number, NumberValue)
        return cls(number=number)
