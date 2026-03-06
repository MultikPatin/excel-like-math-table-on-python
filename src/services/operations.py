from src.models.sheet import Sheet


class OperationTree:
    def __init__(self, sheet: Sheet) -> None:
        self._sheet = sheet
