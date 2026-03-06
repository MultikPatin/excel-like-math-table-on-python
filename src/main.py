from src.services import CalculationTable, OperationTree
from src.test_data import layout, operations, sheet

if __name__ == "__main__":
    operation_tree = OperationTree()

    for operation in operations:
        # print(operation)
        operation_tree.add_two_operands(operation)

    # print(operation_tree.dump())

    calculation = CalculationTable(
        sheet=sheet,  # ty:ignore[invalid-argument-type]
        layout=layout,  # ty:ignore[invalid-argument-type]
    )
