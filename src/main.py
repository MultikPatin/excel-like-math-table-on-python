from icecream import ic

from src.services import Sheet
from src.services.cell.formula import ASTBuilder

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
        "=MAX(MIN(A1:A3), SUM(C1:C3, D1:D3), B1 * 2.1 + C4 / B1)",
    ]

    for formula in formulas:
        ic("-------------------------------------------------------")
        ic(formula)
        ast = ast_builder.build(formula)
        ic(ast.dump())

    ic("=============================================================")

    sheet = Sheet()
    sheet.set_value("A1", "1")
    sheet.set_value("A2", "1")
    ic("=A1+A2")
    sheet.set_value("A3", "=A1+A2")
    ic("=SUM(A1:A3)")
    sheet.set_value("A4", "=SUM(A1:A3)")
    sheet.set_value("B1", "1")
    sheet.set_value("B3", "1")
    sheet.set_value("C4", "1")
    ic("=SUM(A1:B3, C3) * 2.1 + C4 / B1 - MIN(A1:A3)")
    sheet.set_value("C1", "=SUM(A1:B3, C3) * 2.1 + C4 / B1 - MIN(A1:A3)")
    ic("=MAX(MIN(A1:A3), SUM(C1:C3, D1:D3), B1 * 2.1 + C4 / B1)")
    sheet.set_value(
        "E1", "=MAX(MIN(A1:A3), SUM(C1:C3, D1:D3), B1 * 2.1 + C4 / B1)"
    )
    ic()
