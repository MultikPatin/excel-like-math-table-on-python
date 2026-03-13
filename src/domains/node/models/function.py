from typing import Any

from src.domains.node.exceptions import InvalidFunctionValueTypeError
from src.domains.values import FunctionValue, Value

from .base import ASTNode


class FunctionNode(ASTNode):
    __slots__ = ("_args", "_function")

    _function: FunctionValue

    def __init__(self, function: Value, args: list[ASTNode]) -> None:
        if not isinstance(function, FunctionValue):
            raise InvalidFunctionValueTypeError(function, FunctionValue)

        self._function = function
        self._args = args

    @property
    def function(self) -> FunctionValue:
        return self._function

    @property
    def args(self) -> list[ASTNode]:
        return self._args

    def dump(self) -> dict[str, Any]:
        return {
            "FunctionNode": {
                "FUNC": self._function,
                "ARGS": [a.dump() for a in self._args],
            }
        }
