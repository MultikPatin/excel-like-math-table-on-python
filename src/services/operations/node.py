from typing import Any

from src.enums import OperationEnum
from src.models import Position

type MaybeNode = Node | None


class Node:
    def __init__(
        self,
        target: Position,
        operation: OperationEnum | None = None,
        left: MaybeNode = None,
        right: MaybeNode = None,
    ) -> None:
        self._target = target
        self._operation = operation
        self._left = left
        self._right = right

    @property
    def target(self) -> Position:
        return self._target

    @property
    def operation(self) -> OperationEnum | None:
        return self._operation

    @operation.setter
    def operation(self, operation: "OperationEnum") -> None:
        if self._operation is not None:
            msg = "Operation already set"
            raise ValueError(msg)
        self._operation = operation
        # print("Set operation")

    @property
    def left(self) -> MaybeNode | None:
        return self._left

    @left.setter
    def left(self, left: "Node") -> None:
        if left.target == self.target:
            msg = "Left node is equal to target node "
            raise ValueError(msg)
        self._left = left
        # print("Set left")

    @property
    def right(self) -> MaybeNode | None:
        return self._right

    @right.setter
    def right(self, right: "Node") -> None:
        if right.target == self.target:
            msg = "Right node is equal to target node "
            raise ValueError(msg)
        self._right = right
        # print("Set right")

    def dump(self) -> dict[str, Any] | tuple[int, int]:
        result = {}

        if self._operation:
            result["operation"] = self._operation
        if self._left:
            result["left"] = self._left.dump()
        if self._right:
            result["right"] = self._right.dump()

        if result:
            result["target"] = self._target.dump()
            return result

        return self._target.dump()
