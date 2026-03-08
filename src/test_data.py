from src.domains import Layout, Position, Schema, TwoOperandsOperation
from src.enums import LayoutDataTypeEnum, OperationEnum

_ROWS_COUNT: int = 4
_COLS_COUNT: int = 5
_SCHEMA_COUNT: int = 5

# Values

values: list[list[int]] = [
    [(i * 10 + j) for j in range(_COLS_COUNT)] for i in range(_ROWS_COUNT)
]

# Layout

layout = Layout(
    schemas=[
        Schema(key=f"col {j}", type=LayoutDataTypeEnum.integer)
        for j in range(_SCHEMA_COUNT)
    ]
)

# Operations

_operations = [
    [Position(row_idx=i, col_idx=j) for j in range(_COLS_COUNT)]
    for i in range(_ROWS_COUNT)
]
operations = [
    TwoOperandsOperation(
        left=_operations[0][0],
        right=_operations[1][0],
        operation=OperationEnum.ADD,
        target=_operations[2][0],
    ),
    TwoOperandsOperation(
        left=_operations[2][0],
        right=_operations[0][1],
        operation=OperationEnum.ADD,
        target=_operations[3][0],
    ),
    TwoOperandsOperation(
        left=_operations[0][1],
        right=_operations[1][1],
        operation=OperationEnum.MUL,
        target=_operations[3][1],
    ),
    TwoOperandsOperation(
        left=_operations[0][2],
        right=_operations[1][2],
        operation=OperationEnum.MUL,
        target=_operations[3][2],
    ),
    TwoOperandsOperation(
        left=_operations[3][0],
        right=_operations[3][1],
        operation=OperationEnum.MUL,
        target=_operations[0][2],
    ),
    TwoOperandsOperation(
        left=_operations[0][1],
        right=_operations[1][1],
        operation=OperationEnum.SUB,
        target=_operations[2][2],
    ),
]

_operation_tree_ref = [
    {
        "left": {
            "left": {
                "left": {
                    "left": (0, 0),
                    "operation": OperationEnum.ADD,
                    "right": (1, 0),
                    "target": (2, 0),
                },
                "operation": OperationEnum.ADD,
                "right": (0, 1),
                "target": (3, 0),
            },
            "operation": OperationEnum.MUL,
            "right": {
                "left": (0, 1),
                "operation": OperationEnum.MUL,
                "right": (1, 1),
                "target": (3, 1),
            },
            "target": (0, 2),
        },
        "operation": OperationEnum.MUL,
        "right": (1, 2),
        "target": (3, 2),
    },
    {
        "left": (0, 1),
        "operation": OperationEnum.SUB,
        "right": (1, 1),
        "target": (2, 2),
    },
]
