from src.enums.layout import LayoutDataTypeEnum
from src.enums.operations import OperationEnum
from src.models import Layout, Position, Schema, Sheet, TwoOperandsOperation

pos00 = Position(row_idx=0, col_idx=0)
pos01 = Position(row_idx=0, col_idx=1)
pos02 = Position(row_idx=0, col_idx=2)
pos03 = Position(row_idx=0, col_idx=3)

pos10 = Position(row_idx=1, col_idx=0)
pos11 = Position(row_idx=1, col_idx=1)
pos12 = Position(row_idx=1, col_idx=2)
pos13 = Position(row_idx=1, col_idx=3)

pos20 = Position(row_idx=2, col_idx=0)
pos21 = Position(row_idx=2, col_idx=1)
pos22 = Position(row_idx=2, col_idx=2)
pos23 = Position(row_idx=2, col_idx=3)

pos30 = Position(row_idx=3, col_idx=0)
pos31 = Position(row_idx=3, col_idx=1)
pos32 = Position(row_idx=3, col_idx=2)
pos33 = Position(row_idx=3, col_idx=3)

operations = [
    TwoOperandsOperation(
        left=pos00,
        right=pos10,
        operation=OperationEnum.ADD,
        result=pos20,
    ),
    TwoOperandsOperation(
        left=pos20,
        right=pos01,
        operation=OperationEnum.ADD,
        result=pos30,
    ),
    TwoOperandsOperation(
        left=pos01,
        right=pos11,
        operation=OperationEnum.MUL,
        result=pos31,
    ),
    TwoOperandsOperation(
        left=pos02,
        right=pos12,
        operation=OperationEnum.MUL,
        result=pos32,
    ),
    TwoOperandsOperation(
        left=pos30,
        right=pos31,
        operation=OperationEnum.MUL,
        result=pos02,
    ),
    TwoOperandsOperation(
        left=pos01,
        right=pos11,
        operation=OperationEnum.SUB,
        result=pos22,
    ),
]

_schemas = [
    Schema(
        key="col 1",
        type=LayoutDataTypeEnum.integer,
        default=1,
    ),
    Schema(
        key="col 2",
        type=LayoutDataTypeEnum.integer,
        default=1,
    ),
    Schema(
        key="col 3",
        type=LayoutDataTypeEnum.integer,
        default=1,
    ),
    Schema(
        key="col4",
        type=LayoutDataTypeEnum.integer,
        default=1,
    ),
]

layout = Layout(schemas=_schemas)

_matrix = [[0 for _ in range(4)] for _ in range(4)]

sheet = Sheet(matrix=_matrix)
