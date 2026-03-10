from enum import StrEnum


class FirstLevelOperatorsEnum(StrEnum):
    MUL = "*"
    DIV = "/"

    @classmethod
    def values_set(cls) -> set[str]:
        return {item.value for item in cls}


class SecondLevelOperatorsEnum(StrEnum):
    ADD = "+"
    SUB = "-"

    @classmethod
    def values_set(cls) -> set[str]:
        return {item.value for item in cls}


def get_all_operators() -> set[str]:
    return FirstLevelOperatorsEnum.values_set().union(
        SecondLevelOperatorsEnum.values_set()
    )


class FunctionsEnum(StrEnum):
    SQRT = "SQRT"
    SUM = "SUM"

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


class TypeEnum(StrEnum):
    NUMBER = "NUMBER"
    CELL = "CELL"
    FUNCTION = "FUNCTION"
    OPERATOR = "OPERATOR"
    LPAREN = "LPAREN_CHAR"
    RPAREN = "RPAREN_CHAR"
    COMMA = "COMMA_CHAR"
    COLON = "COLON_CHAR"
    EOF = "EOF"
