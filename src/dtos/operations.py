from dataclasses import dataclass

from src.constants import MIN_NUM_OF_OPERANDS
from src.enums import OperatioEnum


@dataclass(frozen=True, slots=True)
class Position:
    row_idx: int
    col_idx: int


@dataclass(frozen=True, slots=True)
class OperationRequest:
    operands: list[Position]
    operation: OperatioEnum
    result: Position

    def __post_init__(self) -> None:
        if len(self.operands) < MIN_NUM_OF_OPERANDS:
            msg = "Operands must contain at least 2 elements"
            raise ValueError(msg)
