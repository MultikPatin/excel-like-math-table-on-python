from typing import Any

from src._types import AnyMatrix
from src.dtos import OperationRequest, Position


class CalculationTable:
    __slots__ = ["_opers", "_sheet"]

    def __init__(
        self, sheet_data: AnyMatrix, operations: list[OperationRequest]
    ) -> None:
        self._sheet = sheet_data
        self._opers = operations

    def add_values(self, position: Position, values: list[Any]) -> None:
        pass
