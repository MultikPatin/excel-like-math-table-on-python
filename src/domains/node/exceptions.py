from typing import Any


class DomainError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidValueTypeError(DomainError):
    def __init__(self, act: Any, expect: Any, attr_name: str) -> None:  # noqa: ANN401
        msg = (
            f"Attribute '{attr_name}' must be type: '{type(act)}',  "
            f"but got type: '{type(expect)}'"
        )
        super().__init__(msg)


class InvalidBinaryOpValueTypeError(InvalidValueTypeError):
    def __init__(self, act: Any, expect: Any) -> None:  # noqa: ANN401
        super().__init__(act, expect, "_operator")


class InvalidLetterValueTypeError(InvalidValueTypeError):
    def __init__(self, act: Any, expect: Any) -> None:  # noqa: ANN401
        super().__init__(act, expect, "_letter")


class InvalidFunctionValueTypeError(InvalidValueTypeError):
    def __init__(self, act: Any, expect: Any) -> None:  # noqa: ANN401
        super().__init__(act, expect, "_function")


class InvalidRangeStartValueTypeError(InvalidValueTypeError):
    def __init__(self, act: Any, expect: Any) -> None:  # noqa: ANN401
        super().__init__(act, expect, "_start")


class InvalidRangeEbdValueTypeError(InvalidValueTypeError):
    def __init__(self, act: Any, expect: Any) -> None:  # noqa: ANN401
        super().__init__(act, expect, "_end")


class InvalidNumberValueTypeError(InvalidValueTypeError):
    def __init__(self, act: Any, expect: Any) -> None:  # noqa: ANN401
        super().__init__(act, expect, "_value")
