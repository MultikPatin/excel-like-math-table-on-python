from src.domains.token import LetterValue


def range_to_cells(
    start: LetterValue, end: LetterValue
) -> list[tuple[int, int]]:
    """Превращает 'A1:B3' в список
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]
    """

    s_alpha, s_digit = split_latter(start.value)
    e_alpha, e_digit = split_latter(end.value)
    return [
        (col, row)
        for col in range(letters_to_num(s_alpha), letters_to_num(e_alpha) + 1)
        for row in range(s_digit, e_digit + 1)
    ]


def split_latter(latter: str) -> tuple[str, int]:
    """Разделяет A1 на (A, 1)"""

    alpha = "".join(c for c in latter if c.isalpha())
    digit = int("".join(c for c in latter if c.isdigit()))
    return alpha, digit


def letters_to_num(col: str) -> int:
    """Конвертирует 'A' -> 1, 'AA' -> 27"""

    num = 0
    for c in col:
        num = num * 26 + (ord(c.upper()) - ord("A") + 1)
    return num


def num_to_letters(num: int) -> str:
    """Конвертирует 1 -> 'A', 27 -> 'AA'"""

    letters = ""
    while num > 0:
        num -= 1
        letters = chr(num % 26 + ord("A")) + letters
        num //= 26
    return letters
