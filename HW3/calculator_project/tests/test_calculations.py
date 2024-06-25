from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add

def test_add_calculation():
    calc = Calculation(1, 2, add)
    Calculations.add_calculation(calc)
    assert Calculations.get_last_calculation() == calc

def test_clear_history():
    Calculations.clear_history()
    assert len(Calculations.history) == 0
