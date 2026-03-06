from dataclasses import dataclass
from functools import cached_property

from src._types import AnyMatrix


@dataclass(frozen=True, kw_only=True)
class Sheet:
    matrix: AnyMatrix

    def __post_init__(self) -> None:
        if len(self.matrix) < 1:
            msg = "Sheet must contain at least 1 row"
            raise ValueError(msg)
        if len(self.matrix[0]) < 1:
            msg = "Sheet must contain at least 1 column"
            raise ValueError(msg)

    @cached_property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.columns

    @cached_property
    def rows(self) -> int:
        return len(self.matrix)

    @cached_property
    def columns(self) -> int:
        return len(self.matrix[0])
