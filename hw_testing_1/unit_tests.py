from unittest import TestCase
from calc import Calc


class TestCalc(TestCase):
    """
    Тестування калькулятора з файлу 'calc.py'
    """

    def test_sum(self):
        self.assertEqual(Calc.plus(1, 2), 3)
        self.assertEqual(Calc.plus(2, 2), 4)
        self.assertNotEqual(Calc.plus(5, 4), 10)

    def test_minus(self):
        self.assertEqual(Calc.minus(10, 5), 5)
        self.assertEqual(Calc.minus(100, 2), 98)
        self.assertNotEqual(Calc.minus(10, 1), 10)

    def test_mul(self):
        self.assertEqual(Calc.mul(5, 5), 25)
        self.assertEqual(Calc.mul(11, 11), 121)
        self.assertNotEqual(Calc.mul(5, 5), 10)

    def test_div(self):
        self.assertEqual(Calc.div(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            Calc.div(100, 0)  # Помилка ділення на 0
        self.assertNotEqual(Calc.div(10, 2), 1)

    def test_percent(self):
        self.assertEqual(Calc.percent(100, 10), 10)
        self.assertNotEqual(Calc.percent(100, 10), 1)

    def test_power(self):
        self.assertEqual(Calc.power(2, 4), 16)
        self.assertEqual(Calc.power(2, 5), 32)
        self.assertNotEqual(Calc.power(2, 5), 16)

    def test_root(self):
        self.assertEqual(Calc.root(25, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(Calc.root(10, 0), 10)  # помилка
        self.assertNotEqual(Calc.root(100, 5), 10)
