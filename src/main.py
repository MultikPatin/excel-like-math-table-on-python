from icecream import ic

from src.services import Parser, Sheet, Tokenizer
from src.test_data import values

if __name__ == "__main__":
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
