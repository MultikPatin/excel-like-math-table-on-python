from src.models import Sheet
from src.services.calculation import Calculation
from src.test_data import layout, matrix

if __name__ == "__main__":
    sheet = Sheet(
        matrix=matrix,
        layout=layout,
    )
    calculation = Calculation(sheet)
