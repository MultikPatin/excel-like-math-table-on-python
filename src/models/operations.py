from dataclasses import dataclass

from src.enums import OperationEnum


@dataclass(frozen=True, slots=True, kw_only=True)
class Position:
    row_idx: int
    col_idx: int


@dataclass(frozen=True, slots=True, kw_only=True)
class TwoOperandsOperation:
    left: Position
    right: Position
    operation: OperationEnum
    result: Position

    def __post_init__(self) -> None:
        if self.left == self.right:
            msg = (
                f"Cannot have both operands at the same position: "
                f"first={self.left}, second={self.right}"
            )
            raise ValueError(msg)
