from typing import Any

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
    def dump(self) -> dict[str, Any]:
        return {}


class BinaryOpNode(ASTNode):
    __slots__ = ("_left", "_operator", "_right")

    _operator: OperatorValue

    def __init__(self, left: ASTNode, op: Value, right: ASTNode) -> None:
        if not isinstance(op, OperatorValue):
            raise InvalidBinaryOpValueTypeError(op, OperatorValue)

        self._left = left
        self._operator = op
        self._right = right

    @property
    def left(self) -> ASTNode:
        return self._left

    @property
    def operator(self) -> OperatorValue:
        return self._operator

    @property
    def right(self) -> ASTNode:
        return self._right

    def dump(self) -> dict[str, Any]:
        return {
            "BinaryOpNode": {
                "left": self._left.dump(),
                "op": self._operator.value.value,
                "right": self._right.dump(),
            }
        }


class LetterNode(ASTNode):
    __slots__ = ("_letter",)

    _letter: LetterValue

    def __init__(self, letter: Value) -> None:
        if not isinstance(letter, LetterValue):
            raise InvalidLetterValueTypeError(letter, LetterValue)

        self._letter = letter

    @property
    def letter(self) -> LetterValue:
        return self._letter

    def dump(self) -> dict[str, Any]:
        return {"LetterNode": self._letter.value}


class FunctionNode(ASTNode):
    __slots__ = ("_args", "_function")

    _function: FunctionValue

    def __init__(self, function: Value, args: list[ASTNode]) -> None:
        if not isinstance(function, FunctionValue):
            raise InvalidFunctionValueTypeError(function, FunctionValue)

        self._function = function
        self._args = args

    @property
    def function(self) -> FunctionValue:
        return self._function

    @property
    def args(self) -> list[ASTNode]:
        return self._args

    def dump(self) -> dict[str, Any]:
        return {
            "FunctionNode": {
                "func": self._function.value.value,
                "args": [a.dump() for a in self._args],
            }
        }


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

    @property
    def start(self) -> LetterValue:
        return self._start

    @property
    def end(self) -> LetterValue:
        return self._end

    def dump(self) -> dict[str, Any]:
        return {
            "RangeNode": {
                "start": self._start.value,
                "end": self._end.value,
            }
        }


class NumberNode(ASTNode):
    __slots__ = ("_value",)

    _number: NumberValue

    def __init__(self, value: Value) -> None:
        if not isinstance(value, NumberValue):
            raise InvalidNumberValueTypeError(value, NumberValue)

        self._number = value

    @property
    def value(self) -> NumberValue:
        return self._number

    def dump(self) -> dict[str, Any]:
        return {"NumberNode": self._number.value}
