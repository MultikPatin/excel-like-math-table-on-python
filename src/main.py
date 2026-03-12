from icecream import ic

from src.services import Sheet
from src.services.cell.formula import ASTBuilder

_ROWS_COUNT: int = 4
_COLS_COUNT: int = 5
_SCHEMA_COUNT: int = 5

if __name__ == "__main__":
    ast_builder = ASTBuilder()

    formulas = [
        "=A1 + A3",
        "=A1 + A3 / 2.4",
        "=MIN(A1:A3)",
        "=SUM(A1:B3, C3)",
        "=SUM(A1:B3, MIN(A1:A3))",
        "=SUM(A1:B3, MAX(A1:A3)) / 2.1 + C4",
        "=SUM(A1:B3, C3) * 2.1 + C4 / B1 - MIN(A1:A3)",
    ]

    for formula in formulas:
        ic("-------------------------------------------------------")
        ic(formula)
        ast = ast_builder.build(formula)
        ic(ast.dump())

    ic("=============================================================")
    values: list[list[int]] = [
        [(i * 10 + j) for j in range(_COLS_COUNT)] for i in range(_ROWS_COUNT)
    ]

    sheet = Sheet(values)
    values = sheet.get_table()
    ic(values)
