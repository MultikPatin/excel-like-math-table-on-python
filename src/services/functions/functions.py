from collections.abc import Iterable
from operator import add, mul, sub, truediv

from src.domains.value import (
    FirstPriorityOperatorsEnum,
    FunctionsEnum,
    FunctionValue,
    NumberValue,
    OperatorValue,
    SecondPriorityOperatorsEnum,
)
from src.services.exceptions import InvalidFunctionError, InvalidOperatorError

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


def call_op(operator: OperatorValue, left: NumberValue, right: NumberValue):  # noqa: ANN201
    try:
        return NumberValue(OPERATION_MAP[operator.value](left, right))
    except KeyError as e:
        raise InvalidOperatorError(operator) from e


def call_func(function: FunctionValue, args: Iterable):  # noqa: ANN201
    try:
        return FUNCTION_MAP[function.value](flatten(args))
    except KeyError as e:
        raise InvalidFunctionError(function) from e


def flatten(nested_list: Iterable) -> list:
    """
    Рекурсивно "расплющивает" вложенный список в одномерный.
    Все элементы из подсписков перемещаются в один общий список.

    Пример:
        [[1, 2], [3, [4, 5]], 6] → [1, 2, 3, 4, 5, 6]
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
