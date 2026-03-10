from src.domains.token import (
    FirstLevelOperatorsEnum,
    FormulaCharsEnum,
    FunctionsEnum,
    SecondLevelOperatorsEnum,
    Token,
    TypeEnum,
    TypeValue,
)

from .char import Char


class Tokenizer:
    __slots__ = ["_cursor", "_length", "_text", "_tokens"]

    def __init__(self) -> None:
        self._text: str = ""
        self._length: int = 0
        self._cursor: int = 0
        self._tokens: list[Token] = []

    def _reset(self, text: str) -> None:
        self._sanitize_text(text)
        self._cursor = 0
        self._tokens: list[Token] = []

    def _sanitize_text(self, text: str) -> None:
        self._text = (
            text[1:] if text.startswith(FormulaCharsEnum.EQUALITY) else text
        )

    def _in_range(self) -> bool:
        return self._cursor < len(self._text)

    def _peek(self) -> Char:
        return Char(self._text[self._cursor])

    def _set_token(
        self,
        type_: TypeEnum,
        value: str | None = None,
        position: int | None = None,
    ) -> None:
        if position is None:
            position = self._cursor
        if value is not None:
            value = self._sanitize_token_value(type_, value)

        self._tokens.append(Token(type=type_, value=value, position=position))

    @staticmethod
    def _sanitize_token_value(type_: TypeEnum, value: str) -> TypeValue:
        result = None

        if type_ == TypeEnum.OPERATOR:
            if value in FirstLevelOperatorsEnum:
                result = FirstLevelOperatorsEnum(value)
            elif value in SecondLevelOperatorsEnum:
                result = SecondLevelOperatorsEnum(value)
        elif type_ in (TypeEnum.NUMBER, TypeEnum.CELL):
            result = value
        elif type_ == TypeEnum.FUNCTION:
            if value in FunctionsEnum:
                result = FunctionsEnum(value)
        else:
            # TODO Custom exception!
            msg = f"Invalid value '{value}'for type '{type_}'"
            raise SyntaxError(msg)

        return result

    def tokenize(self, text: str) -> list[Token]:
        self._reset(text)

        while self._in_range():
            char = self._peek()

            if char.isspace():
                self._cursor += 1
                continue

            if char.isnumber():
                self._parse_number()
                continue

            if char.isalpha():
                self._parse_identifier()
                continue

            if char.isoperator():
                self._set_token(TypeEnum.OPERATOR, char)
                self._cursor += 1
                continue

            if char.islparent():
                self._set_token(TypeEnum.LPAREN)
                self._cursor += 1
                continue

            if char.isrparent():
                self._set_token(TypeEnum.RPAREN)
                self._cursor += 1
                continue

            if char.iscomma():
                self._set_token(TypeEnum.COMMA)
                self._cursor += 1
                continue

            if char.iscolon():
                self._set_token(TypeEnum.COLON)
                self._cursor += 1
                continue

            msg = f"Unexpected character '{char}' at position {self._cursor}"
            # TODO Custom exception!
            raise SyntaxError(msg)

        self._set_token(TypeEnum.EOF)
        return self._tokens

    def _parse_number(self) -> None:
        position = self._cursor

        while self._in_range() and self._peek().isnumber():
            self._cursor += 1

        self._set_token(
            TypeEnum.NUMBER, self._text[position : self._cursor], position
        )

    def _parse_identifier(self) -> None:
        position = self._cursor

        while self._in_range() and self._peek().isalnum():
            self._cursor += 1

        sub = self._text[position : self._cursor]

        if sub.isupper() and self._in_range() and self._peek().islparent():
            type_ = TypeEnum.FUNCTION
        else:
            type_ = TypeEnum.CELL

        self._set_token(type_, sub, position)
