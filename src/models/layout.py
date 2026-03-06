from dataclasses import dataclass, field
from functools import cached_property
from typing import Any

from src.enums.layout import LayoutDataTypeEnum

# from .operations import Operation


@dataclass(frozen=True, slots=True, kw_only=True)
class Schema:
    key: str
    type: LayoutDataTypeEnum
    default: Any = None


@dataclass(frozen=True, slots=True, kw_only=True)
class Validation:
    gt: int | None = None
    ge: int | None = None
    lt: int | None = None
    le: int | None = None


@dataclass(frozen=True, kw_only=True)
class Layout:
    schemas: list[Schema]
    validations: list[Validation | None] = field(default_factory=list)
    # operations: list[Operation] = field(default_factory=list, init=False)
    # rows: int = 0

    def __post_init__(self) -> None:
        if self.columns < 1:
            msg = "Schemas must contain at least 1 elements"
            raise ValueError(msg)
        if len(self.validations) > self.columns:
            msg = (
                f"Number of validations ({len(self.validations)}) must be "
                f"less or equal to the number of schemas({self.columns})"
            )
            raise ValueError(msg)

    @cached_property
    def columns(self) -> int:
        return len(self.schemas)

    # def add_operation(self, opr: Operation) -> None:
    #     for operand in opr.operands:
    #         if operand.col_idx > self.columns:
    #             msg = (
    #                 f"Column index of operand ({operand}) must be "
    #                 f"less or equal to the number of schemas ({self.columns})"
    #             )
    #             raise ValueError(msg)
    #     if opr.result.col_idx > self.columns:
    #         msg = (
    #             f"Column index of result ({opr.result}) must be "
    #             f"less or equal to the number of schemas ({self.columns})"
    #         )
    #         raise ValueError(msg)
    #     self.operations.append(opr)
