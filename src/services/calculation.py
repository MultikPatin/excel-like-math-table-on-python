from src.models import Sheet


class Calculation:
    __slots__ = ["_sheet"]

    def __init__(self, sheet: Sheet) -> None:
        self._sheet = sheet
