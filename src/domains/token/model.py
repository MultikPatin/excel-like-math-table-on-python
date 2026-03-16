from src.domains.value import (
    FormulaCharValue,
    FunctionValue,
    LetterValue,
    NumberValue,
    OperatorValue,
    Value,
)
from src.domains.value.enums import TypeEnum
from src.services.exceptions import InvalidTokenValueError

from ._type import TypeTokenValue


class Token:
    __slots__ = ("_type", "_value")

    _value: TypeTokenValue

    def __init__(self, type_: TypeEnum, value: str | None) -> None:
        self._type = type_

        if value is not None:
            if self._type in (
                TypeEnum.LPAREN,
                TypeEnum.RPAREN,
                TypeEnum.COLON,
                TypeEnum.COMMA,
            ):
                self._value = FormulaCharValue(value)
            else:
                self._sanitize_value(value)
        elif self._type == TypeEnum.EOF:
            self._value = Value()
        else:
            raise InvalidTokenValueError(value)

    def _sanitize_value(self, value: str) -> None:
        match self._type:
            case TypeEnum.NUMBER:
                self._value = NumberValue.from_str(value)
            case TypeEnum.OPERATOR:
                self._value = OperatorValue(value)
            case TypeEnum.FUNCTION:
                self._value = FunctionValue(value)
            case TypeEnum.LETTER:
                self._value = LetterValue(value)

    @property
    def value(self) -> TypeTokenValue:
        return self._value

    @property
    def type(self) -> TypeEnum:
        return self._type

    def is_type_operator(self) -> bool:
        return self._type == TypeEnum.OPERATOR

    def is_type_number(self) -> bool:
        return self._type == TypeEnum.NUMBER

    def is_type_cell(self) -> bool:
        return self._type == TypeEnum.LETTER

    def is_type_function(self) -> bool:
        return self._type == TypeEnum.FUNCTION

    def is_type_lparen(self) -> bool:
        return self._type == TypeEnum.LPAREN

    def is_type_rparen(self) -> bool:
        return self._type == TypeEnum.RPAREN

    def is_type_colon(self) -> bool:
        return self._type == TypeEnum.COLON

    def is_type_comma(self) -> bool:
        return self._type == TypeEnum.COMMA

    def __repr__(self) -> str:
        return f"Token({self._type}: '{self._value.value}')"
