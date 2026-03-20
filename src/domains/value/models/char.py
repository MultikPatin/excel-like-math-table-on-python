from dataclasses import dataclass
from typing import Self

from src.domains.value.enums import FormulaCharsEnum
from src.domains.value.exceptions import InvalidFormulaCharValueError


@dataclass(frozen=True, slots=True)
class FormulaCharValue:
    value: FormulaCharsEnum

    @classmethod
    def model_validate(cls, value: str) -> Self:
        functions = FormulaCharsEnum.values_set()
        if value not in functions:
            raise InvalidFormulaCharValueError(value, functions)
        return cls(value=FormulaCharsEnum(value))
