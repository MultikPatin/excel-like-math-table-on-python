from collections.abc import MutableSet
from typing import TYPE_CHECKING

from src.domains.node import AnyNode
from src.domains.value import FormulaValue

if TYPE_CHECKING:
    from src.domains.value import LetterValue, NumberValue

type TypeCellDependencies = MutableSet[LetterValue]
type TypeCellDependents = MutableSet[LetterValue]


class Cell:
    __slots__ = (
        "_dependencies",
        "_dependents",
        "_formula",
        "_letter",
        "_value",
    )

    def __init__(self, value: "NumberValue", letter: "LetterValue") -> None:
        self._value = value
        self._letter = letter

        self._formula: FormulaValue | None = None

        self._dependents: TypeCellDependents = set()
        self._dependencies: TypeCellDependencies = set()

    @property
    def value(self) -> "NumberValue":
        return self._value

    @value.setter
    def value(self, value: "NumberValue") -> None:
        self._value = value
        # self._recalculate_depends()

    @property
    def formula(self) -> FormulaValue | None:
        return self._formula

    @property
    def dependents(self) -> TypeCellDependents:
        return self._dependents

    @property
    def dependencies(self) -> TypeCellDependencies:
        return self._dependencies

    def set_formula(self, formula: str, ast_tree: AnyNode) -> None:
        # TODO Реализовать сравнение
        self._formula = FormulaValue(formula, ast_tree)

    def remove_dependent(self, letter: "LetterValue") -> None:
        if letter not in self._dependents:
            self._dependents.discard(letter)

    # def set_formula(
    #     self, formula: str, dependencies: TypeCellDependencies
    # ) -> None:
    #     self._unlink_dependencies()
    #     self._formula = formula
    #     self._link_dependencies(dependencies)
    #     self.recalculate()

    # def recalculate(self) -> None:
    #     if self._formula:
    #         values = [d.value for d in self._dependencies]
    #         value = self._formula(*values)
    #         if value != self._value:
    #             self._value = value
    #             self._recalculate_depends()

    # def _link_dependencies(self, dependencies: TypeCellDependencies) -> None:
    #     self._dependencies = dependencies
    #     for d in self._dependencies:
    #         d.dependents.append(self)
    #
    # def unlink_dependencies(self) -> None:
    #     for d in self._dependencies:
    #         if self._letter in d.dependents:
    #             d.dependents.remove(self)

    # def _recalculate_depends(self) -> None:
    #     for d in self._dependents:
    #         d.recalculate()
