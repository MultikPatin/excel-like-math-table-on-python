from src.domains.token import (
    FirstLevelOperatorsEnum,
    FunctionsEnum,
    SecondLevelOperatorsEnum,
    Token,
    TypeEnum,
    TypeValue,
)

from .nodes import (
    ASTNode,
    BinaryOpNode,
    CellNode,
    FunctionNode,
    NumberNode,
    RangeNode,
)

INVALID_TOKEN_VALUE_TYPE = "Invalid token value type, received: {type}"  # noqa: S105


class Parser:
    def __init__(self) -> None:
        self.position = 0
        self._tokens: list[Token] = []

    def parse(self, tokens: list[Token]) -> ASTNode:
        self.position = 0
        self._tokens = tokens
        ast = self._parse_expression()
        self._expect(TypeEnum.EOF, inc_position=False)
        return ast

    def _parse_expression(self) -> ASTNode:
        return self._parse_second_level_operators()

    def _parse_second_level_operators(self) -> ASTNode:
        left = self._parse_first_level_operators()

        while self._peek().is_type_operator():
            op = self._peek_value()
            if op in SecondLevelOperatorsEnum:
                self.position += 1
                right = self._parse_first_level_operators()
                left = BinaryOpNode(left, SecondLevelOperatorsEnum(op), right)
            else:
                break

        return left

    def _parse_first_level_operators(self) -> ASTNode:
        left = self._parse_elements()

        while self._peek().is_type_operator():
            op = self._peek_value()
            if op in FirstLevelOperatorsEnum:
                self.position += 1
                right = self._parse_elements()
                left = BinaryOpNode(left, FirstLevelOperatorsEnum(op), right)
            else:
                break

        return left

    def _parse_elements(self) -> ASTNode:
        token = self._peek()

        if token.is_type_number():
            self.position += 1

            if not isinstance(token.value, str):
                # TODO Custom exception!
                raise SyntaxError(
                    INVALID_TOKEN_VALUE_TYPE.format(type=type(token.value))
                )

            return NumberNode(token.value)

        if token.is_type_cell():
            self.position += 1

            if not isinstance(token.value, str):
                # TODO Custom exception!
                raise SyntaxError(
                    INVALID_TOKEN_VALUE_TYPE.format(type=type(token.value))
                )

            return CellNode(token.value)

        if token.is_type_function():
            return self._parse_function()

        if token.is_type_lparen():
            self.position += 1
            expr = self._parse_expression()
            self._expect(TypeEnum.RPAREN)
            return expr

        msg = f"Unexpected token: {token}"
        # TODO Custom exception!
        raise SyntaxError(msg)

    def _parse_function(self) -> FunctionNode:
        function = self._peek_value()
        self.position += 1
        self._expect(TypeEnum.LPAREN)

        args = []

        if not self._peek().is_type_rparen():
            while True:
                if self._is_range_start():
                    start = self._peek_value()
                    if not isinstance(start, str):
                        # TODO Custom exception!
                        raise SyntaxError(
                            INVALID_TOKEN_VALUE_TYPE.format(type=type(start))
                        )
                    self.position += 1

                    self._expect(TypeEnum.COLON)

                    end = self._peek_value()
                    if not isinstance(end, str):
                        # TODO Custom exception!
                        raise SyntaxError(
                            INVALID_TOKEN_VALUE_TYPE.format(type=type(end))
                        )
                    self.position += 1

                    args.append(RangeNode(start, end))
                else:
                    args.append(self._parse_expression())

                if self._peek().is_type_comma():
                    self.position += 1
                    continue
                break

        self._expect(TypeEnum.RPAREN)

        if isinstance(function, FunctionsEnum):
            return FunctionNode(function, args)

        # TODO Custom exception!
        raise SyntaxError(INVALID_TOKEN_VALUE_TYPE.format(type=type(function)))

    def _peek(self) -> Token:
        return self._tokens[self.position]

    def _peek_type(self) -> TypeEnum:
        return self._peek().type

    def _peek_value(self) -> TypeValue:
        return self._peek().value

    def _peek_next(self) -> Token | None:
        if self.position + 1 < len(self._tokens):
            return self._tokens[self.position + 1]
        return None

    def _is_range_start(self) -> bool:
        next_ = self._peek_next()
        if next_ is None:
            return False
        return self._peek().is_type_cell() and next_.is_type_colon()

    def _expect(self, expected: TypeEnum, inc_position: bool = True) -> Token:
        if self._peek().type != expected:
            msg = (
                f"Expected type: {expected}, type received: {self._peek().type}"
            )
            # TODO Custom exception!
            raise SyntaxError(msg)
        if inc_position:
            self.position += 1
        return self._peek()
