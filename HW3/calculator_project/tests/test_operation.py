import pytest
from calculator.operations import add, subtract, multiply, divide

def test_add():
    """Test add operation"""
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    """Test subtract operation"""
    assert subtract(2, 1) == 1
    assert subtract(-1, -1) == 0
    assert subtract(2.5, 1.5) == 1.0

def test_multiply():
    """Test multiply operation"""
    assert multiply(2, 3) == 6
    assert multiply(-1, -1) == 1
    assert multiply(2.5, 2) == 5.0

def test_divide():
    """Test divide operation"""
    assert divide(6, 3) == 2
    assert divide(-4, -2) == 2
    assert divide(2.5, 2.5) == 1.0
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)

