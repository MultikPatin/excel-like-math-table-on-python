from enum import Enum, StrEnum, auto


class LayoutDataTypeEnum(StrEnum):
    # string = auto()
    integer = auto()
    float = auto()
    decimal = auto()
    # date = auto()
    # time = auto()
    # datetime = auto()


class OperationEnum(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
