from operator import add, mul, sub, truediv

from src.domains.value import (
    FirstPriorityOperatorsEnum,
    NumberValue,
    OperatorValue,
    SecondPriorityOperatorsEnum,
)
from src.services.exceptions import InvalidOperatorError

OPERATION_MAP = {
    FirstPriorityOperatorsEnum.MUL: mul,
    FirstPriorityOperatorsEnum.DIV: truediv,
    SecondPriorityOperatorsEnum.ADD: add,
    SecondPriorityOperatorsEnum.SUB: sub,
}


def call_op(
    operator: OperatorValue, left: NumberValue, right: NumberValue
) -> NumberValue:
    try:
        return NumberValue(OPERATION_MAP[operator.value](left, right))
    except KeyError as e:
        raise InvalidOperatorError(operator) from e
