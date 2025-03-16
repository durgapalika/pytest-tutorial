from enum import Enum


def add(number1: int, number2: int):
    return number1 + number2


class Operator(Enum):
    Add = 1,
    Subtract = 2,
    Multiply = 3,
    Divide = 4


def perform_operation(number1: int, number2: int, operator: Operator):
    match operator:
        case operator.Add:
            return number1 + number2
        case operator.Subtract:
            return number1 - number2
        case operator.Multiply:
            return number1 * number2
