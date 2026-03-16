from src.domains.value import (
    FormulaCharValue,
    FunctionValue,
    LetterValue,
    NumberValue,
    OperatorValue,
    Value,
)

type TypeTokenValue = (
    NumberValue
    | LetterValue
    | FunctionValue
    | OperatorValue
    | FormulaCharValue
    | Value
)
