class RootError(Exception):
    pass


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
        """Віднімання чисел
        >>> Calc.minus(10,9)
        1

        Від числа a віднімається число b
        :param a: перше число
        :param b: друге число
        :return: результат a - b
        """
        return a - b

    @staticmethod
    def mul(a, b):
        """Множення чисел
        >>> Calc.mul(2,4)
        8

        Число a множиться на число b
        :param a: перше число
        :param b: друге число
        :return: результат a * b
        """
        return a * b

    @staticmethod
    def div(a, b):
        """Ділення чисел
        >>> Calc.div(10, 5)
        2

        Число a ділиться на число b
        :param a: перше число
        :param b: друге число
        :return: результат a / b
        """
        return a / b

    @staticmethod
    def percent(a, b):
        """Відсоток від числа
        >>> Calc.percent(100, 10)
        10.0

        :param a: основне число (100%)
        :param b: друге число (X%)
        :return: Скільки відсотків число b від числа a
        """
        return (b * 100) / a

    @staticmethod
    def power(a, b):
        """Піднесення в степінь
        >>> Calc.power(10, 2)
        100


        :param a: число - основа
        :param b: число - степінь
        :return: Число a ** b
        """
        return a ** b

    @staticmethod
    def root(a, b):
        """Корінь з числа a за основою b
        >>> Calc.root(25, 2)
        5

        Для плюсових чисел використовується формула
        round(pow(a, float(1 / b)))
        Для від'ємних чисел та з основою кратною 3 формула
        round(-pow(abs(a), float(1 / b)))
        :param a: число під коренем
        :param b: основа кореня
        :return: Результат кореня
        """
        if a > 0:
            return round(pow(a, float(1 / b)))
        elif a < 0:
            if b % 2 == 0:
                raise RootError
            else:
                return round(-pow(abs(a), float(1 / b)))
        else:
            return 0
