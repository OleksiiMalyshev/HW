from unittest import TestCase
from calc import Calc


class TestCalc(TestCase):
    """
    Тестування калькулятора з файлу 'calc.py'
    """

    def test_sum(self):
        self.assertEqual(Calc.plus(1, 2), 3)
        self.assertEqual(Calc.plus(2, 2), 4)
        self.assertEqual(Calc.plus(5, 4), 10)

    def test_minus(self):
        pass

    def test_mul(self):
        pass

    def test_div(self):
        pass
