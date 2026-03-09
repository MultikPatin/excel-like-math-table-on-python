from icecream import ic

from src.services import Sheet, Tokenizer
from src.test_data import values

if __name__ == "__main__":
    sheet = Sheet(values)

    ic(1)
    values = sheet.get_table()
    ic(values)

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize("=SQRT(SUM(A1:B3) * 2 + C5) / A2")
    for token in tokens:
        ic(token)
