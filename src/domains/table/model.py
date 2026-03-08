from typing import TYPE_CHECKING, Any

from .exceptions import (
    InvalidColumnCountError,
    InvalidIndexError,
    InvalidRowCountError,
)

if TYPE_CHECKING:
    from ._types import Values


class Model:
    __slots__ = ("_values",)

    def __init__(self, values: "Values") -> None:
        self._values = values
        self._init_validate()

    def _init_validate(self) -> None:
        if len(self._values) < 1:
            raise InvalidRowCountError
        if len(self._values[0]) < 1:
            raise InvalidColumnCountError

    @property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.columns

    @property
    def rows(self) -> int:
        return len(self._values)

    @property
    def columns(self) -> int:
        return len(self._values[0])

    @property
    def values(self) -> "Values":
        return self._values

    def get_value(self, row: int, col: int) -> Any:  # noqa: ANN401
        try:
            return self._values[row][col]
        except IndexError as e:
            raise InvalidIndexError(row, col, self) from e

    def set_value(self, row: int, col: int, value: Any) -> None:  # noqa: ANN401
        try:
            self._values[row][col] = value
        except IndexError as e:
            raise InvalidIndexError(row, col, self) from e
