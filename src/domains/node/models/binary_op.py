from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self

from src.domains.node.exceptions import InvalidBinaryOpValueTypeError
from src.domains.value import OperatorValue

if TYPE_CHECKING:
    from src.domains.node import AnyNode

type Operand = AnyNode


@dataclass(frozen=True, slots=True)
class BinaryOpNode:
    op: OperatorValue
    left: Operand
    right: Operand

    @classmethod
    def model_validate(cls, left: Operand, op: Any, right: Operand) -> Self:  # noqa: ANN401
        if not isinstance(op, OperatorValue):
            raise InvalidBinaryOpValueTypeError(op, OperatorValue)
        return cls(op=op, left=left, right=right)
