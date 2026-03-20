from collections.abc import Iterable
from typing import TYPE_CHECKING

from src.domains.value import FunctionsEnum, NumberValue
from src.services.exceptions import InvalidFunctionError

if TYPE_CHECKING:
    from src.domains.value import FunctionValue

type Args = Iterable[NumberValue | Iterable[NumberValue]]


FUNCTION_MAP = {
    FunctionsEnum.SUM: sum,
    FunctionsEnum.MAX: max,
    FunctionsEnum.MIN: min,
}


def call_func(function: "FunctionValue", args: Args) -> NumberValue:
    try:
        return NumberValue(FUNCTION_MAP[function.value](flatten(args)))
    except KeyError as e:
        raise InvalidFunctionError(function) from e


def flatten(args: Args) -> list[NumberValue]:
    """
    Рекурсивно "расплющивает" вложенный список в одномерный.
    Все элементы из подсписков перемещаются в один общий список.

    Пример:
        [[1, 2], [3, [4, 5]], 6] → [1, 2, 3, 4, 5, 6]
    """
    result = []
    for arg in args:
        if isinstance(arg, list):
            result.extend(flatten(arg))
        else:
            result.append(arg)
    return result
