from typing import Any


class ServiceError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidTokenValueError(ServiceError):
    def __init__(self, value: str | None) -> None:
        msg = f"Invalid value '{value}' of type: {type(value)}"
        super().__init__(msg)


class InvalidCellError(ServiceError):
    def __init__(self, letter: str) -> None:
        msg = f"Sheet has no cell with that letter: {letter}"
        super().__init__(msg)


class InvalidNodeTypeError(ServiceError):
    def __init__(self, node: Any) -> None:  # noqa: ANN401
        msg = f"Invalid Node type: {type(node)}"
        super().__init__(msg)


class UnexpectedCharError(ServiceError):
    def __init__(self, char: str, position: int) -> None:
        msg = f"Unexpected character '{char}' at position {position}"
        super().__init__(msg)


class UnexpectedTokenError(ServiceError):
    def __init__(self, token: str) -> None:
        msg = f"Unexpected token: {token}"
        super().__init__(msg)


class UnexpectedTokenTypeError(ServiceError):
    def __init__(self, actual: Any, expected: Any) -> None:  # noqa: ANN401
        msg = f"Expected type: {expected}, type received: {actual}"
        super().__init__(msg)
