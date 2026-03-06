from src.protocols import LayoutProtocol, SheetProtocol


class CalculationTable:
    __slots__ = ["_layout", "_sheet"]

    def __init__(self, *, sheet: SheetProtocol, layout: LayoutProtocol) -> None:
        layout.is_valid_sheet(sheet)

        self._sheet = sheet
        self._layout = layout
