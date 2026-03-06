from src.services.calculation_table import CalculationTable
from src.test_data import layout, sheet

if __name__ == "__main__":
    calculation = CalculationTable(
        sheet=sheet,  # ty:ignore[invalid-argument-type]
        layout=layout,  # ty:ignore[invalid-argument-type]
    )
