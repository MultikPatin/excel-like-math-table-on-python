from src.domains.node import (
    ASTNode,
    BinaryOpNode,
    FunctionNode,
    LetterNode,
    NumberNode,
    RangeNode,
)
from src.domains.value import FormulaCharsEnum, LetterValue, NumberValue
from src.protocols import ASTBuilderProtocol, CellProtocol, TokenizerProtocol

from .exceptions import InvalidNodeTypeError
from .functions import call_func, call_op


class Sheet:
    __slots__ = (
        "_ast_builder",
        "_cell_cls",
        "_cells",
        "_evaluator",
        "_tokenizer",
    )

    def __init__(
        self,
        tokenizer: TokenizerProtocol,
        ast_builder: ASTBuilderProtocol,
        cell_cls: type[CellProtocol],
    ) -> None:
        self._cell_cls: type[CellProtocol] = cell_cls
        self._cells: dict[LetterValue, CellProtocol] = {}
        self._tokenizer = tokenizer
        self._ast_builder = ast_builder

    def _cell(self, letter: LetterValue) -> CellProtocol:
        if letter not in self._cells:
            self._cells[letter] = self._cell_cls(NumberValue.from_str("0"))

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
        ast = self._ast_tree(value)
        cell.value = self._evaluate(ast)

    def _ast_tree(self, value: str) -> ASTNode:
        tokens = self._tokenizer.tokenize(value)
        return self._ast_builder.build(tokens)

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
