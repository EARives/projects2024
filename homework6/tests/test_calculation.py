from decimal import Decimal
from typing import Any, Callable
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),  
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),  
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),  
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),  
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
])
def test_calculation_operations(a: Decimal, b: Decimal, operation: Callable[..., Any], expected: Decimal):
    """
    Test calculation operations with various scenarios.

    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.

    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    calc = Calculation(a, b, operation)  
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"  

def test_calculation_repr():
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"  
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    calc = Calculation(Decimal('10'), Decimal('0'), divide)  
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform() 

