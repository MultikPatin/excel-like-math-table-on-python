from collections.abc import Callable

from src.domains.node import (
    ASTNode,
    BinaryOpNode,
    FunctionNode,
    LetterNode,
    NumberNode,
    RangeNode,
)

from .converters import range_to_cells
from .functions import _call_func, _call_op


class Evaluator:
    def __init__(self, cell_lookup_function: Callable) -> None:
        """
        cell_lookup_function - функция, которая по имени ячейки
        возвращает ее объект
        Например: lambda cell_name: workbook.get_cell(cell_name)
        """
        self.cell_lookup = cell_lookup_function
        self.dependencies = set()  # Множество ячеек, от которых зависит формула

    def evaluate[Node: ASTNode](self, node: Node):  # noqa: ANN201
        if isinstance(node, NumberNode):
            return node.value

        if isinstance(node, LetterNode):
            # Запоминаем зависимость
            self.dependencies.add(node.letter)
            # Получаем значение ячейки
            cell = self.cell_lookup(node.letter)
            return cell.value if cell else 0

        if isinstance(node, RangeNode):
            # Для диапазона собираем все ячейки в нем
            cells = range_to_cells(node.start, node.end)
            for cell_name in cells:
                self.dependencies.add(cell_name)
            # Возвращаем список значений (для функций вроде SUM)
            return [self.cell_lookup(cell).value for cell in cells]

        if isinstance(node, FunctionNode):
            return _call_func(
                node.function, [self.evaluate(a) for a in node.args]
            )

        if isinstance(node, BinaryOpNode):
            return _call_op(
                node.operator,
                self.evaluate(node.left),
                self.evaluate(node.right),
            )

        # TODO Custom exception!
        msg = f"Invalid Node: {type(node)}"
        raise ValueError(msg)
