from enum import StrEnum


class FirstPriorityOperatorsEnum(StrEnum):
    MUL = "*"
    DIV = "/"

    @classmethod
    def values_set(cls) -> set[str]:
        return {item.value for item in cls}


class SecondPriorityOperatorsEnum(StrEnum):
    ADD = "+"
    SUB = "-"

    @classmethod
    def values_set(cls) -> set[str]:
        return {item.value for item in cls}


def get_all_operators() -> set[str]:
    return FirstPriorityOperatorsEnum.values_set().union(
        SecondPriorityOperatorsEnum.values_set()
    )


class FunctionsEnum(StrEnum):
    SUM = "SUM"
    MAX = "MAX"
    MIN = "MIN"

    @classmethod
    def values_set(cls) -> set[str]:
        return {item.value for item in cls}


class FormulaCharsEnum(StrEnum):
    LPAREN = "("
    RPAREN = ")"
    COMMA = ","
    DOT = "."
    COLON = ":"
    SEMICOLON = ";"
    EQUALITY = "="

    @classmethod
    def values_set(cls) -> set[str]:
        return {item.value for item in cls}


class TypeEnum(StrEnum):
    NUMBER = "NUMBER"
    LETTER = "LETTER"
    FUNCTION = "FUNCTION"
    OPERATOR = "OPERATOR"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    COMMA = "COMMA"
    COLON = "COLON"
    EOF = "EOF"
