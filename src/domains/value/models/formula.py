from dataclasses import dataclass
from typing import TYPE_CHECKING, Self

from src.domains.value.enums import FormulaCharsEnum
from src.domains.value.exceptions import InvalidFormulaValueError

if TYPE_CHECKING:
    from src.domains.node import AnyNode


@dataclass(frozen=True, slots=True)
class FormulaValue:
    text: str
    tree: "AnyNode"

    @classmethod
    def model_validate(cls, text: str, tree: "AnyNode") -> Self:
        if not text.startswith(FormulaCharsEnum.START):
            raise InvalidFormulaValueError(text)
        return cls(text=text, tree=tree)
