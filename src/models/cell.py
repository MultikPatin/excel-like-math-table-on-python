from collections.abc import Callable, MutableSequence
from typing import Self

type Cells = MutableSequence[Cell]
type Formula = Callable | None


class Cell[T]:
    __slots__ = ("_dependencies", "_dependents", "_formula", "_value")

    def __init__(self, value: T | None = None) -> None:
        self._value = value
        self._dependents: Cells = []
        self._formula: Formula = None
        self._dependencies: Cells = []

    @classmethod
    def create_empty(cls) -> Self:
        return cls()

    @property
    def value(self) -> T | None:
        return self._value

    @value.setter
    def value(self, value: T) -> None:
        self._value = value
        self._recalculate_depends()

    def set_formula(self, formula: Formula, dependencies: Cells) -> None:
        self._unlink_dependents()
        self._formula = formula
        self._link_dependents(dependencies)
        self.recalculate()

    def recalculate(self) -> None:
        if self._formula:
            values = [d.value for d in self._dependencies]
            value = self._formula(*values)
            if value != self._value:
                self._value = value
                self._recalculate_depends()

    def _link_dependents(self, dependencies: Cells) -> None:
        self._dependencies = dependencies
        for d in self._dependencies:
            d._dependents.append(self)

    def _unlink_dependents(self) -> None:
        for d in self._dependencies:
            if self in d._dependents:
                d._dependents.remove(self)

    def _recalculate_depends(self) -> None:
        for d in self._dependents:
            d.recalculate()
