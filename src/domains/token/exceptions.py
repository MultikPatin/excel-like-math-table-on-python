from typing import TYPE_CHECKING

from .enums import get_all_operators

if TYPE_CHECKING:
    from re import Pattern


class DomainError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidOperatorValueError(DomainError):
    def __init__(self, value: str) -> None:
        msg = f"Operator must be one of: {get_all_operators()}, but got {value}"
        super().__init__(msg)


class InvalidFunctionValueError(DomainError):
    def __init__(self, value: str, functions: set[str]) -> None:
        msg = f"Function must be one of: {functions} but got {value}"
        super().__init__(msg)


class InvalidCellValueError(DomainError):
    def __init__(self, value: str, pattern: "Pattern") -> None:
        msg = (
            f"Cell name must be in format {pattern}, "
            f"e.g. A1, ABC123, but got '{value}'"
        )
        super().__init__(msg)


class InvalidNumberValueError(DomainError):
    def __init__(self, value: str) -> None:
        msg = f"Number must convert to int or float, but got {value}"
        super().__init__(msg)


class InvalidFormulaCharValueError(DomainError):
    def __init__(self, value: str, chars: set[str]) -> None:
        msg = f"FormulaChar must be one of: {chars} but got {value}"
        super().__init__(msg)
