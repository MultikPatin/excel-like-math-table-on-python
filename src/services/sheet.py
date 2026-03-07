from src.protocols import CellProtocol, TableProtocol


class Sheet:
    __slots__ = ("_sheet",)

    _sheet: list[list[CellProtocol]]

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
