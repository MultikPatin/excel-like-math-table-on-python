from collections.abc import Callable, MutableSequence

from .model import Cell

type TypeCellDependencies = MutableSequence[Cell]
type TypeCellDependents = MutableSequence[Cell]
type TypeFormula = Callable | None
