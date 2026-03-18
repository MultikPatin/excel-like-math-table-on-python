from .enums import FirstPriorityOperatorsEnum, SecondPriorityOperatorsEnum

type OperatorEnumType = (
    type[FirstPriorityOperatorsEnum] | type[SecondPriorityOperatorsEnum]
)
