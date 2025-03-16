import pytest
from main import add, perform_operation, Operator


def test_add():
    assert add(2, 3) == 5, "add 2 and 3 should be 5"


@pytest.mark.parametrize("number1,number2,operation,expected,message", [
    (2, 3, Operator.Add, 5, "2+3 = 5"),
    (4, 5, Operator.Subtract, -1, "4-5 = -1"),
    (4, 5, Operator.Multiply, 20, "4 * 5 = 20"),
])
def test_perform_operation(number1, number2, operation, expected, message):
    assert perform_operation(number1, number2, operator=operation) == expected, message


@pytest.mark.parametrize("number1,number2,expected", [
    (2, 3, 5),
    (4, 5, 9),
    (14, 15, 29),
])
def test_add_multiple_times(number1, number2, expected):
    assert add(number1, number2) == expected
