from icecream import ic

from src.domains import cell, table
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

    sheet = Sheet(new_table=table.Model(values=values), cell_cls=cell.Model())

    ic(1)
    values = sheet.get_table()
    ic(values)
