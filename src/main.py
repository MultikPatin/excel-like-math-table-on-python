from icecream import ic

from src.models import Table
from src.models.cell import Cell
from src.services import Sheet
from src.test_data import values

if __name__ == "__main__":
    # operation_tree = OperationTree()
    #
    # for operation in operations:
    #     operation_tree.add_two_operands(operation)
    #
    # for operation in operation_tree.dump():
    #     ic("================================================================")
    #     ic(operation)

    sheet = Sheet(table=Table(values=values), cell=Cell())  # ty:ignore[invalid-argument-type]

    ic(1)
