from dataclasses import dataclass

from src.enums import OperationEnum


@dataclass(frozen=True, slots=True, kw_only=True)
class Position:
    row_idx: int
    col_idx: int


@dataclass(frozen=True, slots=True, kw_only=True)
class SimpleOperation:
    first_operand: Position
    second_operand: Position
    operation: OperationEnum
    result: Position

    def __post_init__(self) -> None:
        if self.first_operand == self.second_operand:
            msg = (
                f"Cannot have both operands at the same position: "
                f"first={self.first_operand}, second={self.second_operand}"
            )
            raise ValueError(msg)
