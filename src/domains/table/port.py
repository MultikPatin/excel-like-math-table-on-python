from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from ._types import Values


class Port(Protocol):
    @property
    def shape(self) -> tuple[int, int]: ...
    @property
    def rows(self) -> int: ...
    @property
    def columns(self) -> int: ...
    @property
    def values(self) -> "Values": ...
    def get_value(self, row: int, col: int) -> Any: ...  # noqa: ANN401
