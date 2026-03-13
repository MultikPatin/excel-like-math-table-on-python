from collections.abc import Sequence
from operator import add, mul, sub, truediv

from src.domains.node import NumberNode
from src.domains.values import (
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


def call_op(operator: OperatorValue, left: NumberNode, right: NumberNode):  # noqa: ANN201
    try:
        return OPERATION_MAP[operator.value](left.value, right.value)
    except KeyError as e:
        # TODO Custom exception!
        msg = f"Invalid operator: {operator}"
        raise ValueError(msg) from e


def call_func(function: FunctionValue, args: Sequence):  # noqa: ANN201
    try:
        return FUNCTION_MAP[function.value](*args)
    except KeyError as e:
        # TODO Custom exception!
        msg = f"Invalid function: {function}"
        raise ValueError(msg) from e
