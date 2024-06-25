import pytest
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operations():
    """Test various calculation operations"""
    calc = Calculation(Decimal(1), Decimal(2), add)
    assert calc.perform() == 3

    calc = Calculation(Decimal(5), Decimal(3), subtract)
    assert calc.perform() == 2

    calc = Calculation(Decimal(2), Decimal(3), multiply)
    assert calc.perform() == 6

    calc = Calculation(Decimal(10), Decimal(2), divide)
    assert calc.perform() == 5

def test_calculation_repr():
    """Test the string representation (__repr__) of the Calculation class"""
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr

def test_divide_by_zero():
    """Test division by zero to ensure it raises a ValueError"""
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()

