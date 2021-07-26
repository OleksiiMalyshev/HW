import doctest

class Calc:
    @staticmethod
    def plus(a, b):
        """Додавання чисел
        >>> Calc.plus(1,2)
        3

        :param a: перше число яке будемо додавати
        :param b: друге число яке будемо додавати
        :return: повертає суму чисел a і b
        """
        return a + b



    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    @staticmethod
    def percent(a, b):
        return (b*100) / a

    @staticmethod
    def power(a, b):
        return a**b

    @staticmethod
    def root(a, b):
        if a < 0 :

# doctest.testmod()
