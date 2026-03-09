from dataclasses import dataclass

from ._types import TypeValue
from .enum import TypeEnum


@dataclass(frozen=True, slots=True, kw_only=True)
class Token:
    type: TypeEnum
    value: TypeValue
    position: int
