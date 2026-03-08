from typing import Any

from src.domains import cell, table


class Sheet:
    __slots__ = ("_sheet", "_table")

    def __init__(self, *, new_table: table.Port, cell_cls: cell.Port) -> None:
        self._init_sheet(new_table, cell_cls)

    def _init_sheet(self, new_table: table.Port, cell_cls: cell.Port) -> None:
        self._table = new_table
        self._sheet = []

        for i in range(new_table.rows):
            self._sheet.append([])
            for j in range(new_table.columns):
                new_cell = cell_cls.new(i, j)
                new_cell.value = new_table.get_value(i, j)
                self._sheet[i].append(new_cell)

    def get_table(self) -> table.Values:
        return self._table.values

    def set_value(self, row: int, col: int, *, value: Any) -> None:  # noqa: ANN401
        self._cell(row, col).value = value

    def set_formula(
        self,
        row: int,
        col: int,
        *,
        formula: cell.TypeFormula,
        dependencies: cell.TypeCellDependencies,
    ) -> None:
        self._cell(row, col).set_formula(formula, dependencies)

    def _cell(self, row: int, col: int) -> cell.Port:
        try:
            return self._sheet[row][col]
        except IndexError:
            shape = (len(self._sheet), len(self._sheet[0]))
            msg = (
                f"Index out of range. Table shape: {shape}. "
                f"Requested row: {row}, column: {col}"
            )  # Set custom exception
            raise ValueError(msg)  # noqa: B904
