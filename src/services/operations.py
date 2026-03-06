from src.models.sheet import Sheet


class OperationTree:
    __slots__ = ["_sheet"]

    def __init__(self, sheet: Sheet) -> None:
        self._sheet = sheet
