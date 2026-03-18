from collections.abc import Callable, MutableSequence
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from src.domains.value import NumberValue
    from src.services.cell import Cell


class CellProtocol(Protocol):
    def __init__(self, value: "NumberValue") -> None: ...
    @property
    def value(self) -> "NumberValue": ...
    @value.setter
    def value(self, value: "NumberValue") -> None: ...
    @property
    def dependents(self) -> "MutableSequence[Cell]": ...
    def set_formula(
        self, formula: Callable, dependencies: "MutableSequence[Cell]"
    ) -> None: ...
    def recalculate(self) -> None: ...
