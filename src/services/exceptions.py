class ServiceError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidTokenValueError(ServiceError):
    def __init__(self, value: str | None) -> None:
        msg = f"Invalid value '{value}' of type: {type(value)}"
        super().__init__(msg)
