from collections.abc import Sequence
from operator import add, mul, sub, truediv

from src.domains.token import (
    FirstPriorityOperatorsEnum,
    FunctionsEnum,
    FunctionValue,
    OperatorValue,
    SecondPriorityOperatorsEnum,
)

OPERATION_MAP = {
    FirstPriorityOperatorsEnum.MUL: mul,
    FirstPriorityOperatorsEnum.DIV: truediv,
    SecondPriorityOperatorsEnum.ADD: add,
    SecondPriorityOperatorsEnum.SUB: sub,
}
FUNCTION_MAP = {
    FunctionsEnum.SUM: sum,
    FunctionsEnum.MAX: max,
    FunctionsEnum.MIN: min,
}


def _call_op(operator: OperatorValue, left, right):  # noqa: ANN001, ANN202
    try:
        return OPERATION_MAP[operator.value](left, right)
    except KeyError as e:
        # TODO Custom exception!
        msg = f"Invalid operator: {operator}"
        raise ValueError(msg) from e


def _call_func(function: FunctionValue, args: Sequence):  # noqa: ANN202
    try:
        return FUNCTION_MAP[function.value](*args)
    except KeyError as e:
        # TODO Custom exception!
        msg = f"Invalid function: {function}"
        raise ValueError(msg) from e
