from collections.abc import Sequence
from typing import Any


class Table:
    __slots__ = ("_values",)

    def __init__(self, values: Sequence[Sequence[Any]]) -> None:
        self._values = values
        self._init_validate()

    def _init_validate(self) -> None:
        if len(self._values) < 1:
            msg = "Sheet must contain at least 1 row"
            # Set custom exception
            raise ValueError(msg)
        if len(self._values[0]) < 1:
            msg = "Sheet must contain at least 1 column"
            # Set custom exception
            raise ValueError(msg)

    @property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.columns

    @property
    def rows(self) -> int:
        return len(self._values)

    @property
    def columns(self) -> int:
        return len(self._values[0])

    def get_value(self, row: int, col: int) -> Any:  # noqa: ANN401
        try:
            return self._values[row][col]
        except IndexError:
            msg = (
                f"Index out of range. Table shape: {self.shape}. "
                f"Requested row: {row}, column: {col}"
            )  # Set custom exception
            raise ValueError(msg)  # noqa: B904
