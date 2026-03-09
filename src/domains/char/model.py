from .constants import (
    COLON_CHAR,
    COMMA_CHAR,
    DOT_CHAR,
    LPAREN_CHAR,
    OPERATORS_CHARS,
    RPAREN_CHAR,
)


class Char(str):
    def isnumber(self) -> bool:
        return self == DOT_CHAR or self.isdigit()

    def isoperator(self) -> bool:
        return self in OPERATORS_CHARS

    def islparent(self) -> bool:
        return self == LPAREN_CHAR

    def isrparent(self) -> bool:
        return self == RPAREN_CHAR

    def iscomma(self) -> bool:
        return self == COMMA_CHAR

    def iscolon(self) -> bool:
        return self == COLON_CHAR
