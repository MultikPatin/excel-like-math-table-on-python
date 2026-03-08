from typing import Any

from src.domains import Position, TwoOperandsOperation

from .node import Node


class OperationTree:
    def __init__(self) -> None:
        self._targets: dict[Position, Node] = {}

    def dump(self) -> list[dict[str, Any] | tuple[int, int]]:
        return [
            target.dump()
            for target in self._targets.values()
            if target.operation is not None
        ]

    def add_two_operands(self, opr: TwoOperandsOperation) -> None:
        left = self._targets.get(opr.left)
        if not left:
            self._targets[opr.left] = Node(opr.left)

        right = self._targets.get(opr.right)
        if not right:
            self._targets[opr.right] = Node(opr.right)

        target = self._targets.get(opr.target)
        if not target:
            self._targets[opr.target] = Node(
                opr.target,
                operation=opr.operation,
                left=self._targets[opr.left],
                right=self._targets[opr.right],
            )
        else:
            target.operation = opr.operation
            target.left = self._targets[opr.left]
            target.right = self._targets[opr.right]
