from functools import cached_property
from typing import Protocol

from .sheet import SheetProtocol


class LayoutProtocol(Protocol):
    @cached_property
    def columns(self) -> int: ...
    def is_valid_sheet(self, sheet: SheetProtocol) -> None: ...
