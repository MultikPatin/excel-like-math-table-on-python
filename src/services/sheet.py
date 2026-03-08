from collections.abc import Callable, MutableSequence, Sequence
from typing import Any

from src.protocols import CellProtocol, TableProtocol


class Sheet:
    __slots__ = ("_sheet",)

    _sheet: Sequence[Sequence[CellProtocol]]

    def __init__(self, *, table: TableProtocol, cell: CellProtocol) -> None:
        self._init_sheet(table, cell)

    def _init_sheet(self, table: TableProtocol, cell: CellProtocol) -> None:
        self._sheet = [
            [cell.create_empty() for _ in range(table.columns)]
            for _ in range(table.rows)
        ]
        for i in range(table.rows):
            for j in range(table.columns):
                self._sheet[i][j].value = table.get_value(i, j)

    @property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.columns

    @property
    def rows(self) -> int:
        return len(self._sheet)

    @property
    def columns(self) -> int:
        return len(self._sheet[0])

    def set_value(self, row: int, col: int, value: Any) -> None:  # noqa: ANN401
        self._cell(row, col).value = value

    def set_formula(
        self,
        row: int,
        col: int,
        formula: Callable,
        dependencies: MutableSequence[CellProtocol],
    ) -> None:
        self._cell(row, col).set_formula(formula, dependencies)

    def _cell(self, row: int, col: int) -> CellProtocol:
        try:
            return self._sheet[row][col]
        except IndexError:
            msg = (
                f"Index out of range. Table shape: {self.shape}. "
                f"Requested row: {row}, column: {col}"
            )  # Set custom exception
            raise ValueError(msg)  # noqa: B904
