from src.domains.node import (
    ASTNode,
    BinaryOpNode,
    FunctionNode,
    LetterNode,
    NumberNode,
    RangeNode,
)
from src.domains.values import FormulaCharsEnum, LetterValue, NumberValue

from .cell import ASTBuilder, Cell, call_func, call_op
from .exceptions import InvalidNodeTypeError


class Sheet:
    __slots__ = ("_ast_builder", "_cells", "_evaluator")

    def __init__(self) -> None:
        self._cells: dict[LetterValue, Cell] = {}
        self._ast_builder = ASTBuilder()

    def _cell(self, letter: LetterValue) -> Cell:
        if letter not in self._cells:
            self._cells[letter] = Cell(NumberValue.from_str("0"))

        return self._cells[letter]

    def set_value(self, letter: str, value: str) -> None:
        _letter = LetterValue(letter)

        if value.startswith(FormulaCharsEnum.EQUALITY):
            self._set_formula(_letter, value)
        else:
            self._set_value(_letter, value)

    def _set_value(self, letter: LetterValue, value: str) -> None:
        cell = self._cell(letter)
        cell.value = NumberValue.from_str(value)

    def _set_formula(self, letter: LetterValue, value: str) -> None:
        cell = self._cell(letter)
        ast = self._ast_builder.build(value)
        cell.value = self._evaluate(ast)

    def _evaluate[Node: ASTNode](self, node: Node):  # noqa: ANN202
        if isinstance(node, NumberNode):
            return node.value

        if isinstance(node, LetterNode):
            cell = self._cell(node.letter)
            return cell.value

        if isinstance(node, RangeNode):
            return [self._cell(cell).value for cell in node.expand()]

        if isinstance(node, FunctionNode):
            return call_func(
                node.function, [self._evaluate(a) for a in node.args]
            )

        if isinstance(node, BinaryOpNode):
            return call_op(
                node.operator,
                self._evaluate(node.left),
                self._evaluate(node.right),
            )

        raise InvalidNodeTypeError(node)
