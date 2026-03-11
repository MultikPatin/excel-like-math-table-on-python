from src.domains.node.exceptions import (
    InvalidBinaryOpValueTypeError,
    InvalidFunctionValueTypeError,
    InvalidLetterValueTypeError,
    InvalidNumberValueTypeError,
    InvalidRangeEbdValueTypeError,
    InvalidRangeStartValueTypeError,
)
from src.domains.token import (
    FunctionValue,
    LetterValue,
    NumberValue,
    OperatorValue,
    Value,
)


class ASTNode:
    pass


class BinaryOpNode(ASTNode):
    __slots__ = ("_left", "_operator", "_right")

    _operator: OperatorValue

    def __init__(self, left: ASTNode, op: Value, right: ASTNode) -> None:
        if not isinstance(op, OperatorValue):
            raise InvalidBinaryOpValueTypeError(op, OperatorValue)

        self._left = left
        self._operator = op
        self._right = right


class LetterNode(ASTNode):
    __slots__ = ("_letter",)

    _letter: LetterValue

    def __init__(self, letter: Value) -> None:
        if not isinstance(letter, LetterValue):
            raise InvalidLetterValueTypeError(letter, LetterValue)

        self._letter = letter


class FunctionNode(ASTNode):
    __slots__ = ("_args", "_function")

    _function: FunctionValue

    def __init__(self, function: Value, args: list[ASTNode]) -> None:
        if not isinstance(function, FunctionValue):
            raise InvalidFunctionValueTypeError(function, FunctionValue)

        self._function = function
        self._args = args


class RangeNode(ASTNode):
    __slots__ = ("_end", "_start")

    _start: LetterValue
    _end: LetterValue

    def __init__(self, start: Value, end: Value) -> None:
        if not isinstance(start, LetterValue):
            raise InvalidRangeStartValueTypeError(start, LetterValue)
        if not isinstance(end, LetterValue):
            raise InvalidRangeEbdValueTypeError(end, LetterValue)

        self._start = start
        self._end = end


class NumberNode(ASTNode):
    __slots__ = ("_value",)

    _value: NumberValue

    def __init__(self, value: Value) -> None:
        if not isinstance(value, NumberValue):
            raise InvalidNumberValueTypeError(value, NumberValue)

        self._value = value
