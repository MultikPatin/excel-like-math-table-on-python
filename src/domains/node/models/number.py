from typing import Any

from src.domains.node.exceptions import InvalidNumberValueTypeError
from src.domains.value import NumberValue, Value

from .base import ASTNode


class NumberNode(ASTNode):
    __slots__ = ("_value",)

    _number: NumberValue

    def __init__(self, value: Value) -> None:
        if not isinstance(value, NumberValue):
            raise InvalidNumberValueTypeError(value, NumberValue)

        self._number = value

    @property
    def value(self) -> NumberValue:
        return self._number

    def dump(self) -> dict[str, Any]:
        return {"NUMBER": self._number}
