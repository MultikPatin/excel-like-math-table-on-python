from typing import TYPE_CHECKING

from src.domains.node import (
    BinaryOpNode,
    FunctionNode,
    LetterNode,
    NumberNode,
    RangeNode,
)
from src.domains.value import FormulaCharsEnum, LetterValue, NumberValue

from .exceptions import (
    InvaliCellValueTypeError,
    InvalidNodeTypeError,
    UnexpectedOperandsToOperationError,
)
from .execute import call_func, call_op

if TYPE_CHECKING:
    from src.domains.node import ASTNode

    from .cell import CellProtocol
    from .formula import ASTBuilderProtocol, TokenizerProtocol


class Sheet:
    __slots__ = (
        "_ast_builder",
        "_cell_cls",
        "_cells",
        "_evaluator",
        "_tokenizer",
    )

    _cells: "dict[LetterValue, CellProtocol]"

    def __init__(
        self,
        tokenizer: "TokenizerProtocol",
        ast_builder: "ASTBuilderProtocol",
        cell_cls: "type[CellProtocol]",
    ) -> None:
        self._cell_cls = cell_cls
        self._cells = {}
        self._tokenizer = tokenizer
        self._ast_builder = ast_builder

    def _cell(self, letter: LetterValue) -> "CellProtocol":
        if letter not in self._cells:
            self._cells[letter] = self._cell_cls(NumberValue.from_str("0"))

        return self._cells[letter]

    def set_value(self, letter: str, value: str) -> None:
        _letter = LetterValue(letter)

        if value.startswith(FormulaCharsEnum.START):
            self._set_formula(_letter, value)
        else:
            self._set_value(_letter, value)

    def _set_value(self, letter: LetterValue, value: str) -> None:
        cell = self._cell(letter)
        cell.value = NumberValue.from_str(value)

    def _set_formula(self, letter: LetterValue, value: str) -> None:
        cell = self._cell(letter)
        ast = self._ast_tree(value)
        result = self._evaluate(ast)

        if isinstance(result, NumberValue):
            cell.value = result
        else:
            raise InvaliCellValueTypeError(result)

    def _ast_tree(self, value: str) -> "ASTNode":
        tokens = self._tokenizer.tokenize(value)
        return self._ast_builder.build(tokens)

    def _evaluate(self, node: "ASTNode") -> NumberValue | list[NumberValue]:
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
            left = self._evaluate(node.left)
            right = self._evaluate(node.right)

            if isinstance(left, NumberValue) and isinstance(right, NumberValue):
                return call_op(node.operator, left, right)
            raise UnexpectedOperandsToOperationError(left, right)

        raise InvalidNodeTypeError(node)
