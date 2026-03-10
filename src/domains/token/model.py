import re
from dataclasses import dataclass

from .enums import (
    FirstLevelOperatorsEnum,
    FormulaCharsEnum,
    FunctionsEnum,
    SecondLevelOperatorsEnum,
    TypeEnum,
    get_all_operators,
)
from .exceptions import (
    InvalidCellValueError,
    InvalidFunctionValueError,
    InvalidNumberValueError,
    InvalidOperatorValueError,
    InvalidValueError,
)

type TypeValue = (
    FirstLevelOperatorsEnum
    | SecondLevelOperatorsEnum
    | FunctionsEnum
    | FormulaCharsEnum
    | str
    | None
)

_CELL_PATTERN = re.compile(r"^[A-Z]+[0-9]+$")


@dataclass(frozen=True, kw_only=True)
class Token:
    type: TypeEnum
    position: int
    value: TypeValue = None

    def __post_init__(self) -> None:  # noqa: PLR0912
        match self.type:
            case TypeEnum.LPAREN:
                self.__dict__["value"] = FormulaCharsEnum.LPAREN
            case TypeEnum.RPAREN:
                self.__dict__["value"] = FormulaCharsEnum.RPAREN
            case TypeEnum.COLON:
                self.__dict__["value"] = FormulaCharsEnum.COLON
            case TypeEnum.COMMA:
                self.__dict__["value"] = FormulaCharsEnum.COMMA

        if self.value is not None:
            match self.type:
                case TypeEnum.NUMBER:
                    try:
                        _ = (
                            float(self.value)
                            if FormulaCharsEnum.DOT in self.value
                            else int(self.value)
                        )
                    except Exception as e:
                        raise InvalidNumberValueError(self.value) from e
                case TypeEnum.OPERATOR:
                    operators = get_all_operators()
                    if self.value not in operators:
                        raise InvalidOperatorValueError(self.value, operators)
                case TypeEnum.FUNCTION:
                    functions = FunctionsEnum.values_set()
                    if self.value not in functions:
                        raise InvalidFunctionValueError(self.value, functions)
                case TypeEnum.CELL:
                    if not _CELL_PATTERN.match(self.value):
                        raise InvalidCellValueError(self.value, _CELL_PATTERN)

        elif self.type != TypeEnum.EOF:
            raise InvalidValueError

    def is_type_operator(self) -> bool:
        return self.type == TypeEnum.OPERATOR

    def is_type_number(self) -> bool:
        return self.type == TypeEnum.NUMBER

    def is_type_cell(self) -> bool:
        return self.type == TypeEnum.CELL

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
