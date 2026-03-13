from collections.abc import Callable, MutableSequence

from src.domains.values import NumberValue

type TypeCellDependencies = MutableSequence[Cell]
type TypeCellDependents = MutableSequence[Cell]
type TypeFormula = Callable | None


class Cell:
    __slots__ = ("_dependencies", "_dependents", "_formula", "_value")

    def __init__(self, value: NumberValue) -> None:
        self._value = value
        self._dependents: TypeCellDependents = []
        self._formula: TypeFormula = None
        self._dependencies: TypeCellDependencies = []

    @property
    def value(self) -> NumberValue:
        return self._value

    @value.setter
    def value(self, value: NumberValue) -> None:
        self._value = value
        self._recalculate_depends()

    @property
    def dependents(self) -> "TypeCellDependents":
        return self._dependents

    def set_formula(
        self, formula: "TypeFormula", dependencies: "TypeCellDependencies"
    ) -> None:
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

    def _link_dependents(self, dependencies: "TypeCellDependencies") -> None:
        self._dependencies = dependencies
        for d in self._dependencies:
            d.dependents.append(self)

    def _unlink_dependents(self) -> None:
        for d in self._dependencies:
            if self in d.dependents:
                d.dependents.remove(self)

    def _recalculate_depends(self) -> None:
        for d in self._dependents:
            d.recalculate()
