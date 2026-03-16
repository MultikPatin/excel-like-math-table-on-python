from collections.abc import Callable, MutableSequence
from typing import Protocol

from src.domains.node import ASTNode
from src.domains.token import Token
from src.domains.value import NumberValue


class ASTBuilderProtocol(Protocol):
    def build(self, tokens: list[Token]) -> ASTNode: ...


class TokenizerProtocol(Protocol):
    def tokenize(self, text: str) -> list[Token]: ...


class CellProtocol(Protocol):
    def __init__(self, value: NumberValue) -> None: ...
    @property
    def value(self) -> NumberValue: ...
    @value.setter
    def value(self, value: NumberValue) -> None: ...
    @property
    def dependents(self) -> "MutableSequence[CellProtocol]": ...
    def set_formula(
        self, formula: Callable, dependencies: "MutableSequence[CellProtocol]"
    ) -> None: ...
    def recalculate(self) -> None: ...
