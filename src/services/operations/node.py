from src.constants import INDENT_CHAR
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

    def dump(self, indent: int = 0) -> str:
        target = f"Cell [{self._target.row_idx}, {self._target.col_idx}] "
        operation = f"{self._operation.name}\n" if self._operation else "\n"
        left = self._left.dump(indent + 2) if self._left else ""
        right = self._right.dump(indent + 2) if self._right else ""

        return INDENT_CHAR * indent + target + operation + left + right
