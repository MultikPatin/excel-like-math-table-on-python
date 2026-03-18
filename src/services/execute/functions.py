from collections.abc import Iterable

from src.domains.value import (
    FunctionsEnum,
    FunctionValue,
    NumberValue,
)
from src.services.exceptions import InvalidFunctionError

FUNCTION_MAP = {
    FunctionsEnum.SUM: sum,
    FunctionsEnum.MAX: max,
    FunctionsEnum.MIN: min,
}


def call_func(function: FunctionValue, args: Iterable) -> NumberValue:
    try:
        return NumberValue(FUNCTION_MAP[function.value](flatten(args)))
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
