from functools import cached_property
from typing import Protocol


class SheetProtocol(Protocol):
    @cached_property
    def shape(self) -> tuple[int, int]: ...
    @cached_property
    def rows(self) -> int: ...
    @cached_property
    def columns(self) -> int: ...
