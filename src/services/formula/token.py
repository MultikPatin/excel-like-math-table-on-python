from dataclasses import dataclass
from typing import Self

from src.domains.value import (
    FormulaCharValue,
    FunctionValue,
    LetterValue,
    NumberValue,
    OperatorValue,
)
from src.domains.value.enums import TypeEnum
from src.services.exceptions import InvalidTokenValueError

type TypeTokenValue = (
    None
    | NumberValue
    | LetterValue
    | FunctionValue
    | OperatorValue
    | FormulaCharValue
)

_FORMULA_CHAR_SET = (
    TypeEnum.LPAREN,
    TypeEnum.RPAREN,
    TypeEnum.COLON,
    TypeEnum.COMMA,
)


@dataclass(frozen=True, slots=True)
class Token:
    value: TypeTokenValue
    type: TypeEnum

    @classmethod
    def model_validate(cls, type_: TypeEnum, value: str | None) -> Self:
        if value is not None:
            if type_ in _FORMULA_CHAR_SET:
                return cls(
                    type=type_, value=FormulaCharValue.model_validate(value)
                )
            match type_:
                case TypeEnum.NUMBER:
                    return cls(type=type_, value=NumberValue(value))
                case TypeEnum.OPERATOR:
                    return cls(
                        type=type_,
                        value=OperatorValue.model_validate(value),
                    )
                case TypeEnum.FUNCTION:
                    return cls(
                        type=type_,
                        value=FunctionValue.model_validate(value),
                    )
                case TypeEnum.LETTER:
                    return cls(
                        type=type_, value=LetterValue.model_validate(value)
                    )
        if type_ == TypeEnum.EOF:
            return cls(type=type_, value=None)
        raise InvalidTokenValueError(value)

    def is_type_operator(self) -> bool:
        return self.type == TypeEnum.OPERATOR

    def is_type_number(self) -> bool:
        return self.type == TypeEnum.NUMBER

    def is_type_cell(self) -> bool:
        return self.type == TypeEnum.LETTER

    def is_type_function(self) -> bool:
        return self.type == TypeEnum.FUNCTION

    def is_type_lparen(self) -> bool:
        return self.type == TypeEnum.LPAREN

    def is_type_rparen(self) -> bool:
        return self.type == TypeEnum.RPAREN

    def is_type_colon(self) -> bool:
        return self.type == TypeEnum.COLON

    def is_type_comma(self) -> bool:
        return self.type == TypeEnum.COMMA
