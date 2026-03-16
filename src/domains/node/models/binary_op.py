from typing import Any

from src.domains.node.exceptions import InvalidBinaryOpValueTypeError
from src.domains.values import OperatorValue, Value

from .base import ASTNode


class BinaryOpNode(ASTNode):
    __slots__ = ("_left", "_operator", "_right")

    _operator: OperatorValue

    def __init__[Node: ASTNode, Operator: Value](
        self, left: Node, op: Operator, right: Node
    ) -> None:
        if not isinstance(op, OperatorValue):
            raise InvalidBinaryOpValueTypeError(op, OperatorValue)

        self._left = left
        self._operator = op
        self._right = right

    @property
    def left(self) -> ASTNode:
        return self._left

    @property
    def operator(self) -> OperatorValue:
        return self._operator

    @property
    def right(self) -> ASTNode:
        return self._right

    def dump(self) -> dict[str, Any]:
        return {
            "BinaryOpNode": {
                "left": self._left.dump(),
                "OP": self._operator,
                "right": self._right.dump(),
            }
        }
