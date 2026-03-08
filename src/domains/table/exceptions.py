from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .port import Port


class DomainError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidRowCountError(DomainError):
    def __init__(self) -> None:
        msg = "Table must contain at least 1 row"
        super().__init__(msg)


class InvalidColumnCountError(DomainError):
    def __init__(self) -> None:
        msg = "Table must contain at least 1 column"
        super().__init__(msg)


class InvalidIndexError(DomainError):
    def __init__(self, row: int, col: int, table: "Port") -> None:
        msg = f"Actual shape: {table.shape}. Requested ({row}, {col})"
        super().__init__(msg)
