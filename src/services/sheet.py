from typing import Any

from src.domains.cell import Cell, TypeCellDependencies, TypeFormula
from src.domains.table import Table, TypeTableValues
from src.domains.token import TypeValue


class Sheet:
    __slots__ = ("_sheet", "_table")

    def __init__(self, values: TypeTableValues) -> None:
        self._table = Table(values=values)
        self._sheet = []

        for i in range(self._table.rows):
            self._sheet.append([])
            for j in range(self._table.columns):
                self._sheet[i].append(
                    Cell[TypeValue](i, j, value=self._table.get_value(i, j))
                )

    def get_table(self) -> TypeTableValues:
        return self._table.values

    def set_value(self, row: int, col: int, *, value: Any) -> None:  # noqa: ANN401
        self._cell(row, col).value = value

    def set_formula(
        self,
        row: int,
        col: int,
        *,
        formula: TypeFormula,
        dependencies: TypeCellDependencies,
    ) -> None:
        self._cell(row, col).set_formula(formula, dependencies)

    def _cell(self, row: int, col: int) -> Cell:
        try:
            return self._sheet[row][col]
        except IndexError:
            shape = (len(self._sheet), len(self._sheet[0]))
            msg = (
                f"Index out of range. Table shape: {shape}. "
                f"Requested row: {row}, column: {col}"
            )  # Set custom exception
            raise ValueError(msg)  # noqa: B904
