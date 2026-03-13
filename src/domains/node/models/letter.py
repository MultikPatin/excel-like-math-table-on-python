from typing import Any

from src.domains.node.exceptions import InvalidLetterValueTypeError
from src.domains.values import LetterValue, Value

from .base import ASTNode


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
        return {"CELL": self._letter}
