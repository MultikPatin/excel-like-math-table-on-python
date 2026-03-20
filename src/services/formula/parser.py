from collections.abc import Callable, MutableSequence
from typing import TYPE_CHECKING

from src.domains.node import (
    AnyNode,
    BinaryOpNode,
    FunctionNode,
    LetterNode,
    NumberNode,
    RangeNode,
)
from src.domains.value import (
    FirstPriorityOperatorsEnum,
    OperatorValue,
    SecondPriorityOperatorsEnum,
    TypeEnum,
)
from src.services.exceptions import (
    UnexpectedTokenError,
    UnexpectedTokenTypeError,
)

if TYPE_CHECKING:
    from src.domains.value import OperatorEnumType

    from .token import Token, TypeTokenValue


INVALID_TYPE = "Invalid token value type, received: {type}"

type MaybeToken = Token | None


class ASTBuilder:
    __slots__ = ["_cursor", "_tokens"]

    def __init__(self) -> None:
        self._cursor = 0
        self._tokens = []

    def build(self, tokens: "MutableSequence[Token]") -> AnyNode:
        self._cursor = 0
        self._tokens = tokens
        ast = self._parse_expression()
        self._expect(TypeEnum.EOF, inc_cursor=False)
        return ast

    def _parse_expression(self) -> AnyNode:
        return self._parse_second_level_operators()

    def _parse_operators(
        self, func: Callable[[], AnyNode], enum: "OperatorEnumType"
    ) -> AnyNode:
        left = func()

        while self._peek().is_type_operator():
            op = self._peek_value()
            if not isinstance(op, OperatorValue):
                raise UnexpectedTokenTypeError(op, OperatorValue)
            if op.value in enum:
                self._cursor += 1
                right = func()
                left = BinaryOpNode.model_validate(left, op, right)
            else:
                break

        return left

    def _parse_second_level_operators(
        self,
    ) -> AnyNode:
        return self._parse_operators(
            self._parse_first_level_operators,
            SecondPriorityOperatorsEnum,
        )

    def _parse_first_level_operators(
        self,
    ) -> AnyNode:
        return self._parse_operators(
            self._parse_elements,
            FirstPriorityOperatorsEnum,
        )

    def _parse_elements(self) -> AnyNode:
        token = self._peek()

        if token.is_type_number():
            self._cursor += 1
            return NumberNode.model_validate(token.value)

        if token.is_type_cell():
            self._cursor += 1
            return LetterNode.model_validate(token.value)

        if token.is_type_function():
            return self._parse_function()

        if token.is_type_lparen():
            self._cursor += 1
            expr = self._parse_expression()
            self._expect(TypeEnum.RPAREN)
            return expr

        raise UnexpectedTokenError(str(token))

    def _parse_function(self) -> FunctionNode:
        function = self._peek_value()
        self._cursor += 1
        self._expect(TypeEnum.LPAREN)

        args = []

        if not self._peek().is_type_rparen():
            while True:
                if self._is_range_start():
                    start = self._peek_value()
                    self._cursor += 1
                    self._expect(TypeEnum.COLON)
                    end = self._peek_value()
                    self._cursor += 1
                    args.append(RangeNode.model_validate(start, end))
                else:
                    args.append(self._parse_expression())

                if self._peek().is_type_comma():
                    self._cursor += 1
                    continue
                break

        self._expect(TypeEnum.RPAREN)
        return FunctionNode.model_validate(function, args)

    def _peek(self) -> "Token":
        return self._tokens[self._cursor]

    def _peek_value(self) -> "TypeTokenValue":
        return self._peek().value

    def _peek_next(self) -> MaybeToken:
        if self._cursor + 1 < len(self._tokens):
            return self._tokens[self._cursor + 1]
        return None

    def _is_range_start(self) -> bool:
        next_ = self._peek_next()
        if next_ is None:
            return False
        return self._peek().is_type_cell() and next_.is_type_colon()

    def _expect(self, expected: TypeEnum, inc_cursor: bool = True) -> "Token":
        actual = self._peek().type
        if actual != expected:
            raise UnexpectedTokenTypeError(actual, expected)
        if inc_cursor:
            self._cursor += 1
        return self._peek()
