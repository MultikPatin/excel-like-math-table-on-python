from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, kw_only=True)
class Table:
    values: list[list[Any]]

    def __post_init__(self) -> None:
        if len(self.values) < 1:
            msg = "Sheet must contain at least 1 row"
            raise ValueError(msg)
        if len(self.values[0]) < 1:
            msg = "Sheet must contain at least 1 column"
            raise ValueError(msg)

    @property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.columns

    @property
    def rows(self) -> int:
        return len(self.values)

    @property
    def columns(self) -> int:
        return len(self.values[0])

    def get_value(self, row_idx: int, col_idx: int) -> Any:  # noqa: ANN401
        return self.values[row_idx][col_idx]
