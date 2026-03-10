import re
from typing import Any

from src.domains.token import TypeEnum


class DomainError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidValueError(DomainError):
    def __init__(self) -> None:
        msg = f"Value can be 'None' only if type is {TypeEnum.EOF}"
        super().__init__(msg)


class InvalidOperatorValueError(DomainError):
    def __init__(self, value: Any, operators: set[str]) -> None:  # noqa: ANN401
        msg = f"Operator must be one of: {operators}, but got {value}"
        super().__init__(msg)


class InvalidFunctionValueError(DomainError):
    def __init__(self, value: Any, functions: set[str]) -> None:  # noqa: ANN401
        msg = f"Operator must be one of: {functions} but got {value}"
        super().__init__(msg)


class InvalidCellValueError(DomainError):
    def __init__(self, value: Any, pattern: re.Pattern) -> None:  # noqa: ANN401
        msg = (
            f"Cell name must be in format {pattern}, "
            f"e.g. A1, ABC123, but got '{value}'"
        )
        super().__init__(msg)


class InvalidNumberValueError(DomainError):
    def __init__(self, value: Any) -> None:  # noqa: ANN401
        msg = f"Number must convert to int or float, but got {value}"
        super().__init__(msg)
