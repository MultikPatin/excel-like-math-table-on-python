from collections.abc import Callable, MutableSequence

from .port import Port

type TypeCellDependencies = MutableSequence[Port]
type TypeCellDependents = MutableSequence[Port]
type TypeFormula = Callable | None
