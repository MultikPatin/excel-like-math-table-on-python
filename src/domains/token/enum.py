from enum import Enum


class TypeEnum(Enum):
    NUMBER = "NUMBER"  # 123, 45.67
    CELL = "CELL"  # A1, B5, AA100
    FUNCTION = "FUNCTION"  # SUM, AVG, MAX
    OPERATOR = "OPERATOR"  # +, -, *, /
    LPAREN = "LPAREN_CHAR"  # (
    RPAREN = "RPAREN_CHAR"  # )
    COMMA = "COMMA_CHAR"  # ,
    COLON = "COLON_CHAR"  # : (для диапазонов)
    EOF = "EOF"  # Конец формулы
