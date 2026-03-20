from src.domains.value import FormulaCharsEnum, TypeEnum
from src.services.exceptions import (
    UnexpectedCharError,
    UnexpectedFormulaStartCharError,
)

from .char import Char
from .token import Token


class Tokenizer:
    __slots__ = ("_cursor", "_text", "_tokens")

    def __init__(self) -> None:
        self._text: str = ""
        self._cursor: int = 0
        self._tokens = []

    def _reset(self, text: str) -> None:
        self._sanitize_text(text)
        self._cursor = 0
        self._tokens: list[Token] = []

    def _sanitize_text(self, text: str) -> None:
        if not text.startswith(FormulaCharsEnum.START):
            raise UnexpectedFormulaStartCharError(
                text[:1], FormulaCharsEnum.START
            )
        self._text = text[1:]

    def _in_range(self) -> bool:
        return self._cursor < len(self._text)

    def _peek(self) -> Char:
        return Char(self._text[self._cursor])

    def _set_token(self, type_: TypeEnum, value: str | None = None) -> None:
        self._tokens.append(Token.model_validate(type_=type_, value=value))

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
                self._set_token(TypeEnum.LPAREN, char)
                self._cursor += 1
                continue

            if char.isrparent():
                self._set_token(TypeEnum.RPAREN, char)
                self._cursor += 1
                continue

            if char.iscomma():
                self._set_token(TypeEnum.COMMA, char)
                self._cursor += 1
                continue

            if char.iscolon():
                self._set_token(TypeEnum.COLON, char)
                self._cursor += 1
                continue

            raise UnexpectedCharError(char, self._cursor)

        self._set_token(TypeEnum.EOF)
        return self._tokens

    def _parse_number(self) -> None:
        position = self._cursor

        while self._in_range() and self._peek().isnumber():
            self._cursor += 1

        self._set_token(TypeEnum.NUMBER, self._text[position : self._cursor])

    def _parse_identifier(self) -> None:
        position = self._cursor

        while self._in_range() and self._peek().isalnum():
            self._cursor += 1

        sub = self._text[position : self._cursor]

        if sub.isupper() and self._in_range() and self._peek().islparent():
            type_ = TypeEnum.FUNCTION
        else:
            type_ = TypeEnum.LETTER

        self._set_token(type_, sub)
