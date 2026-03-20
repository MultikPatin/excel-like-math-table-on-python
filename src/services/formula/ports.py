from collections.abc import MutableSequence
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from src.domains.node import AnyNode

    from .token import Token


class ASTBuilderProtocol(Protocol):
    def build(self, tokens: "MutableSequence[Token]") -> "AnyNode": ...


class TokenizerProtocol(Protocol):
    def tokenize(self, text: str) -> "list[Token]": ...
