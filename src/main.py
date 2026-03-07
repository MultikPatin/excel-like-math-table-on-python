from icecream import ic

from src.services import CalculationTable, OperationTree
from src.test_data import layout, operations, sheet

if __name__ == "__main__":
    operation_tree = OperationTree()

    for operation in operations:
        operation_tree.add_two_operands(operation)

    for operation in operation_tree.dump():
        ic("================================================================")
        ic(operation)

    calculation = CalculationTable(
        sheet=sheet,  # ty:ignore[invalid-argument-type]
        layout=layout,  # ty:ignore[invalid-argument-type]
    )
