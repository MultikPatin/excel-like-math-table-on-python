from dataclasses import dataclass, field
from typing import Any

from src.enums.layout import LayoutDataTypeEnum


@dataclass(frozen=True, slots=True)
class Schema:
    key: str
    type: LayoutDataTypeEnum
    default: Any = None


@dataclass(frozen=True, slots=True)
class Validation:
    gt: int | None = None
    ge: int | None = None
    lt: int | None = None
    le: int | None = None


@dataclass(frozen=True, slots=True)
class Layout:
    schemas: list[Schema]
    validations: list[Validation] = field(default_factory=list)

    def __post_init__(self) -> None:
        if len(self.schemas) < 1:
            msg = "Schemas must contain at least 1 elements"
            raise ValueError(msg)
