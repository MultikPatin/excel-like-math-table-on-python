from dataclasses import dataclass
from typing import Any

from ._types import TypeTableValues
from .exceptions import (
    InvalidColumnCountError,
    InvalidIndexError,
    InvalidRowCountError,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class Table[T]:
    values: TypeTableValues[T]

    def __post_init__(self) -> None:
        if len(self.values) < 1:
            raise InvalidRowCountError
        if len(self.values[0]) < 1:
            raise InvalidColumnCountError

    @property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.columns

    @property
    def rows(self) -> int:
        return len(self.values)

    @property
    def columns(self) -> int:
        return len(self.values[0])

    def get_value(self, row: int, col: int) -> Any:  # noqa: ANN401
        try:
            return self.values[row][col]
        except IndexError as e:
            raise InvalidIndexError(row, col, self) from e

    def set_value(self, row: int, col: int, value: Any) -> None:  # noqa: ANN401
        try:
            self.values[row][col] = value
        except IndexError as e:
            raise InvalidIndexError(row, col, self) from e
