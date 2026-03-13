from src.domains.values import FormulaCharsEnum, get_all_operators


class Char(str):
    def isnumber(self) -> bool:
        return self == FormulaCharsEnum.DOT or self.isdigit()

    def isoperator(self) -> bool:
        return self in get_all_operators()

    def islparent(self) -> bool:
        return self == FormulaCharsEnum.LPAREN

    def isrparent(self) -> bool:
        return self == FormulaCharsEnum.RPAREN

    def iscomma(self) -> bool:
        return self == FormulaCharsEnum.COMMA

    def iscolon(self) -> bool:
        return self == FormulaCharsEnum.COLON
