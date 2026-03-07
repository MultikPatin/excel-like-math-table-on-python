from dataclasses import dataclass
from typing import Any

from src.enums.layout import LayoutDataTypeEnum
from src.protocols import TableProtocol


@dataclass(frozen=True, slots=True, kw_only=True)
class Schema:
    key: str
    type: LayoutDataTypeEnum
    default: Any = None


# @dataclass(frozen=True, slots=True, kw_only=True)
# class Validation:
#     gt: int | None = None
#     ge: int | None = None
#     lt: int | None = None
#     le: int | None = None


@dataclass(frozen=True, kw_only=True)
class Layout:
    schemas: list[Schema]
    # validations: list[Validation | None] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.columns < 1:
            msg = "Schemas must contain at least 1 elements"
            raise ValueError(msg)
        # if len(self.validations) > self.columns:
        #     msg = (
        #         f"Number of validations ({len(self.validations)}) must be "
        #         f"less or equal to the number of schemas({self.columns})"
        #     )
        #     raise ValueError(msg)

    @property
    def columns(self) -> int:
        return len(self.schemas)

    def is_valid_table(self, table: TableProtocol) -> None:
        if self.columns != table.columns:
            msg = "Table must have the same number of columns as layout schemas"
            raise ValueError(msg)

        # for i in range(table.columns):
        #     for j in range(table.rows):
