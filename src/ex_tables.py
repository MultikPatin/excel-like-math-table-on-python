from typing import Any

test_operations: list[dict[str, Any]] = [
    {
        "operands": [(0, 0), (1, 0), (2, 0)],
        "operation": "+",
        "result": (3, 0),
    },
    {
        "operands": [(0, 1), (1, 1), (2, 1)],
        "operation": "-",
        "result": (3, 1),
    },
    {
        "operands": [(0, 2), (1, 2), (2, 2)],
        "operation": "*",
        "result": (3, 2),
    },
    {
        "operands": [(3, 0), (3, 1)],
        "operation": "*",
        "result": (0, 2),
    },
    {
        "operands": [(0, 1), (0, 1)],
        "operation": "-",
        "result": (2, 2),
    },
]
