from src.domains.token import (
    FirstLevelOperatorsEnum,
    FunctionsEnum,
    SecondLevelOperatorsEnum,
)


class ASTNode:
    pass


class NumberNode(ASTNode):
    def __init__(self, value: str) -> None:
        self._value = value

    def __repr__(self) -> str:
        return f"Number({self._value})"


class CellNode(ASTNode):
    def __init__(self, cell: str) -> None:
        self._cell = cell

    def __repr__(self) -> str:
        return f"Cell({self._cell})"


class RangeNode(ASTNode):
    def __init__(self, start_cell: str, end_cell: str) -> None:
        self._start_cell = start_cell
        self._end_cell = end_cell

    def __repr__(self) -> str:
        return f"Range({self._start_cell}:{self._end_cell})"


class FunctionNode(ASTNode):
    def __init__(self, name: FunctionsEnum, args: list[ASTNode]) -> None:
        self._name = name
        self._args = args

    def __repr__(self) -> str:
        return f"Function({self._name}, [{self._args}])"


class BinaryOpNode(ASTNode):
    def __init__(
        self,
        left: ASTNode,
        operator: FirstLevelOperatorsEnum | SecondLevelOperatorsEnum,
        right: ASTNode,
    ) -> None:
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self) -> str:
        return f"BinaryOp({self.left} {self.operator} {self.right})"
