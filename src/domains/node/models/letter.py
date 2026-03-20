from dataclasses import dataclass
from typing import Any, Self

from src.domains.node.exceptions import InvalidLetterValueTypeError
from src.domains.value import LetterValue


@dataclass(frozen=True, slots=True)
class LetterNode:
    letter: LetterValue

    @classmethod
    def model_validate(cls, letter: Any) -> Self:  # noqa: ANN401
        if not isinstance(letter, LetterValue):
            raise InvalidLetterValueTypeError(letter, LetterValue)
        return cls(letter=letter)
