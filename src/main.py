import logging

from src.dtos import OperationRequest
from src.ex_tables import test_operations
from src.services.calculation_table import CalculationTable

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    sheet_data = [[0 for _ in range(4)] for _ in range(4)]

    operations: list[OperationRequest] = []
    try:
        operations = [OperationRequest(**opr) for opr in test_operations]
    except KeyError:
        logger.exception("Error when prepare operations")

    calculation_table = CalculationTable(sheet_data, operations)
