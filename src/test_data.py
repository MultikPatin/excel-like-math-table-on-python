_ROWS_COUNT: int = 4
_COLS_COUNT: int = 5
_SCHEMA_COUNT: int = 5

# Values

values: list[list[int]] = [
    [(i * 10 + j) for j in range(_COLS_COUNT)] for i in range(_ROWS_COUNT)
]
