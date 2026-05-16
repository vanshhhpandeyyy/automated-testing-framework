import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.calculator import Calculator


@pytest.fixture
def calc():
    """Reusable Calculator fixture for all test cases."""
    return Calculator()


class TestAddition:
    def test_add_positive_numbers(self, calc):
        assert calc.add(3, 5) == 8

    def test_add_negative_numbers(self, calc):
        assert calc.add(-4, -6) == -10

    def test_add_zero(self, calc):
        assert calc.add(0, 100) == 100

    def test_add_floats(self, calc):
        assert calc.add(1.5, 2.5) == pytest.approx(4.0)


class TestSubtraction:
    def test_subtract_basic(self, calc):
        assert calc.subtract(10, 3) == 7

    def test_subtract_result_negative(self, calc):
        assert calc.subtract(3, 10) == -7

    def test_subtract_same_numbers(self, calc):
        assert calc.subtract(5, 5) == 0


class TestMultiplication:
    def test_multiply_positive(self, calc):
        assert calc.multiply(4, 5) == 20

    def test_multiply_by_zero(self, calc):
        assert calc.multiply(999, 0) == 0

    def test_multiply_negatives(self, calc):
        assert calc.multiply(-3, -3) == 9

    def test_multiply_float(self, calc):
        assert calc.multiply(2.5, 4) == pytest.approx(10.0)


class TestDivision:
    def test_divide_basic(self, calc):
        assert calc.divide(10, 2) == 5.0

    def test_divide_float_result(self, calc):
        assert calc.divide(7, 2) == pytest.approx(3.5)

    def test_divide_by_zero_raises(self, calc):
        """Edge case: division by zero must raise ValueError."""
        with pytest.raises(ValueError, match="Division by zero"):
            calc.divide(10, 0)

    def test_divide_negative(self, calc):
        assert calc.divide(-10, 2) == -5.0


class TestPowerAndParity:
    def test_power_basic(self, calc):
        assert calc.power(2, 10) == 1024

    def test_power_zero_exponent(self, calc):
        assert calc.power(999, 0) == 1

    def test_is_even_true(self, calc):
        assert calc.is_even(4) is True

    def test_is_even_false(self, calc):
        assert calc.is_even(7) is False

    def test_is_even_zero(self, calc):
        assert calc.is_even(0) is True
