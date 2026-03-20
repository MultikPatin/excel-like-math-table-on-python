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
    from src.domains.node import AnyNode

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
            self._cells[letter] = self._cell_cls(
                NumberValue.from_str("0"), letter
            )

        return self._cells[letter]

    def set_value(self, letter: str, value: str) -> None:
        _letter = LetterValue.model_validate(letter)

        if value.startswith(FormulaCharsEnum.START):
            self._set_formula(_letter, value)
        else:
            self._set_value(_letter, value)

    def _set_value(self, letter: LetterValue, value: str) -> None:
        cell = self._cell(letter)
        cell.value = NumberValue.from_str(value)
        self._recalculate_depends(letter)

    def _set_formula(self, letter: LetterValue, formula: str) -> None:
        cell = self._cell(letter)

        if cell.formula is None or cell.formula.text != formula:
            ast_tree = self._ast_builder.build(
                self._tokenizer.tokenize(formula)
            )
        else:
            ast_tree = cell.formula.tree

        self.unlink_dependencies(letter)
        result = self._evaluate(ast_tree)

        if isinstance(result, NumberValue):
            cell.value = result
            # cell.set_formula(formula, ast_tree)
        else:
            raise InvaliCellValueTypeError(result)

        # cell.link_dependencies()
        #

    def _evaluate(self, node: "AnyNode") -> NumberValue | list[NumberValue]:
        if isinstance(node, NumberNode):
            return node.number

        if isinstance(node, LetterNode):
            # Запоминаем зависимость
            # self.dependencies.add(node.cell_ref)
            cell = self._cell(node.letter)
            return cell.value

        if isinstance(node, RangeNode):
            # Для диапазона собираем все ячейки в нем
            # cells = self._expand_range(node.start_cell, node.end_cell)
            # for cell_name in cells:
            #     self.dependencies.add(cell_name)
            return [self._cell(cell).value for cell in node.expand()]

        if isinstance(node, FunctionNode):
            return call_func(node.func, [self._evaluate(a) for a in node.args])

        if isinstance(node, BinaryOpNode):
            left = self._evaluate(node.left)
            right = self._evaluate(node.right)

            if isinstance(left, NumberValue) and isinstance(right, NumberValue):
                return call_op(node.op, left, right)
            raise UnexpectedOperandsToOperationError(left, right)

        raise InvalidNodeTypeError(node)

    def _recalculate_depends(self, letter: LetterValue) -> None:
        cell = self._cell(letter)
        for d in cell.dependents:
            self._recalculate(d)

    def _recalculate(self, letter: LetterValue) -> None:
        cell = self._cell(letter)
        if cell.formula:
            result = self._evaluate(cell.formula.tree)
            if not isinstance(result, NumberValue):
                raise InvaliCellValueTypeError(result)
            if cell.value != result:
                cell.value = result
                self._recalculate_depends(letter)

    def unlink_dependencies(self, letter: LetterValue) -> None:
        for d in self._cell(letter).dependencies:
            self._cell(d).remove_dependent(d)
