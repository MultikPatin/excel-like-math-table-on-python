from typing import Protocol


class TableRepository(Protocol):
    def get(self, id_: str) -> None: ...
