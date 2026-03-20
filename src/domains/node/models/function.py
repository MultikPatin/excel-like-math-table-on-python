from collections.abc import Iterable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self

from src.domains.node.exceptions import InvalidFunctionValueTypeError
from src.domains.value import FunctionValue

if TYPE_CHECKING:
    from src.domains.node import NumberNode

type Args = Iterable[NumberNode]


@dataclass(frozen=True, slots=True)
class FunctionNode:
    func: FunctionValue
    args: Args

    @classmethod
    def model_validate(cls, func: Any, args: Args) -> Self:  # noqa: ANN401
        if not isinstance(func, FunctionValue):
            raise InvalidFunctionValueTypeError(func, FunctionValue)
        return cls(func=func, args=args)
