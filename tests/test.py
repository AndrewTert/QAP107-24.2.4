import pytest
from app.calculator import Calculator


class TestCalcul:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 2) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 1, 2) == -1

    def test_division_success(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_multiply_success(self):
        assert self.calc.multiply(self, 1, 2) == 2

    # def test_adding_fail(self):
    #     assert self.calc.adding(self, 3, 4) == 8
    #
    # def test_divizion_byzero(self):
    #     with pytest.raises(ZeroDivisionError):
    #         self.calc.division(self, 10, 0)

    def teardown(self):
        print('\nTearDown!')
