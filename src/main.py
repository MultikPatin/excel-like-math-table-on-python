from icecream import ic

from src.services import Parser, Sheet, Tokenizer

_ROWS_COUNT: int = 4
_COLS_COUNT: int = 5
_SCHEMA_COUNT: int = 5

if __name__ == "__main__":
    values: list[list[int]] = [
        [(i * 10 + j) for j in range(_COLS_COUNT)] for i in range(_ROWS_COUNT)
    ]

    sheet = Sheet(values)

    ic(1)
    values = sheet.get_table()
    ic(values)

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize("=SQRT(SUM(A1:B3, C3) * 2.1 + C4) / B1")
    for token in tokens:
        ic(token)

    parser = Parser()
    ast = parser.parse(tokens)
    ic(ast)
