from src.models import Position, TwoOperandsOperation

from .node import Node


class OperationTree:
    def __init__(self) -> None:
        self._trees: dict[Position, Node] = {}
        self._targets: dict[Position, Node] = {}

    def dump(self) -> str:
        result = "Trees are an operation in a table\n"

        for position in self._trees.values():
            result += "=================================\n"
            result += position.dump()

        return result

    def add_two_operands(self, opr: TwoOperandsOperation) -> None:
        left = self._targets.get(opr.left, Node(opr.left))
        right = self._targets.get(opr.right, Node(opr.right))

        result = self._targets.get(opr.result)
        if not result:
            result = Node(
                opr.result,
                operation=opr.operation,
                left=left,
                right=right,
            )
            self._targets[opr.result] = result
            self._trees[opr.result] = result
        else:
            result.operation = opr.operation
            result.left = left
            result.right = right

        self._targets[opr.left] = result
        self._targets[opr.right] = result
