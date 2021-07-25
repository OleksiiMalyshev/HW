import logging
import math

template = "%(levelname)s: %(asctime)s: %(filename)s: - %(message)s"

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="a", format=template)


class RootError(Exception):
    pass


def plus(a, b):
    logging.info(f"Plus function with args {a} , {b}")
    return f'{a} + {b} = {a + b}'


def minus(a, b):
    logging.info(f"Minus function with args {a} , {b}")
    return f'{a} - {b} = {a - b}'


def division(a, b):
    logging.info(f"Division function with args {a} , {b}")
    return f'{a} / {b} = {a / b}'


def multiply(a, b):
    logging.info(f"Multiply function with args {a} , {b}")
    return f'{a} * {b} = {a * b}'


def power(a, b):
    logging.info(f"Power function with args {a} , {b}")
    return f'{a} в степені {b} = {pow(a, b)}'


def root(a, b):
    logging.info(f"Root function with args {a} , {b}")
    if a > 0:
        return f'Корінь з {a} за основи - {b} = {round(math.pow(a, float(1 / b)))}'
    elif a < 0:
        if b % 2 == 0:
            raise RootError
        else:
            return f'Корінь з {a} за основи - {b} = {round(-math.pow(abs(a), float(1 / b)))}'
    else:
        return f'Корінь з {a} за основи - {b} = 0'


def percent(a, b):
    logging.info(f"Percent function with args {a} , {b}")
    return f'Від числа {a} число {b} це {(b * 100) / a}%'


logging.info("Programm started")


def calc():
    sym = ['+', '-', '/', '*', '**', 'root', '%']
    while True:
        try:
            num1 = float(input('\nВведіть перше число '))
            logging.info(f'num1 got {num1} value')
        except ValueError:
            print("НЕ ПРАВИЛЬНИЙ ФОРМАТ, ОЧІКУЄТЬСЯ INT")
            logging.error("Value error")
            calc()

        symbol = input(f"Введіть знак якій відповідає одній з операцій:\n"
                       f"        {sym[0]} для додавання\n"
                       f"        {sym[1]} для віднімання\n"
                       f"        {sym[2]} для ділення\n"
                       f"        {sym[3]} для множення\n"
                       f"        {sym[4]} для піднесення в степінь\n"
                       f"        {sym[5]} для взяття з під кореня\n"
                       f"        {sym[6]} для пошуку відсотку від числа\n"
                       f"        Ваш вибір - ")
        logging.info(f'User chose {symbol} operation')
        # if symbol not in sym:
        #     raise MyException("НЕ ВІРНА ДІЯ")
        try:
            assert symbol in sym
            if symbol == sym[0]:  # +
                try:
                    num2 = int(input('Введіть друге число '))
                    logging.info(f'num2 got {num2} value')
                    print(plus(num1, num2))
                    logging.info(f"Plus func returned {plus(num1, num2)}")
                except ValueError:
                    print("НЕ ПРАВИЛЬНИЙ ФОРМАТ, ОЧІКУЄТЬСЯ INT")
                    logging.error("Value error")
            if symbol == sym[1]:  # -
                try:
                    num2 = int(input('Введіть друге число '))
                    logging.info(f'num2 got {num2} value')
                    print(minus(num1, num2))
                except ValueError:
                    print("НЕ ПРАВИЛЬНИЙ ФОРМАТ, ОЧІКУЄТЬСЯ INT")
                    logging.error("Value error")
            if symbol == sym[2]:  # /
                try:
                    num2 = int(input('Введіть друге число '))
                    logging.info(f'num2 got {num2} value')
                    print(division(num1, num2))
                except ValueError:
                    print("НЕ ПРАВИЛЬНИЙ ФОРМАТ, ОЧІКУЄТЬСЯ INT")
                    logging.error("Value error")
                except ZeroDivisionError:
                    print("НЕ МОЖНА РОБИТИ ДІЛЕННЯ НА 0 ЧЕРЕЗ ЦЕЙ КАЛЬКУЛЯТОР")
                    logging.error("ZeroDivisionError")
            if symbol == sym[3]:  # *
                try:
                    num2 = int(input('Введіть друге число '))
                    logging.info(f'num2 got {num2} value')
                    print(multiply(num1, num2))
                except ValueError:
                    print("НЕ ПРАВИЛЬНИЙ ФОРМАТ, ОЧІКУЄТЬСЯ INT")
                    logging.error("Value error")
            if symbol == sym[4]:  # **
                try:
                    num2 = int(input('Введіть друге число '))
                    logging.info(f'num2 got {num2} value')
                    print(power(num1, num2))
                except ValueError:
                    print("НЕ ПРАВИЛЬНИЙ ФОРМАТ, ОЧІКУЄТЬСЯ INT")
                    logging.error("Value error")
            if symbol == sym[5]:  # root
                try:
                    num2 = float(input('Введіть друге число '))
                    logging.info(f'num2 got {num2} value')
                    print(root(num1, num2))
                except ValueError:
                    print("НЕ ПРАВИЛЬНИЙ ФОРМАТ, ОЧІКУЄТЬСЯ INT")
                    logging.error("Value error")
                except RootError:
                    print("Якщо num1 - від'ємне - то основа кореня може бути лише непарне число")
                    logging.error("RootError")
                except ZeroDivisionError:
                    print("НЕ МОЖНА БРАТИ ЗА ОСНОВУ ЧИСЛО 0")
                    logging.error("Zero division error")
            if symbol == sym[6]:  # %
                try:
                    num2 = int(input('Введіть друге число '))
                    logging.info(f'num2 got {num2} value')
                    print(percent(num1, num2))
                except ValueError:
                    print("НЕ ПРАВИЛЬНИЙ ФОРМАТ, ОЧІКУЄТЬСЯ INT")
                    logging.error("Value error in percent")
        except AssertionError:
            print("НЕ ВІРНА ДІЯ")
            logging.error("Wrong operator given by user")

        z = int(input("Напишіть [1] щоб вийти з программи"
                      "\nНапишіть [2] щоб продовжити - "))
        if z == 1:
            logging.info('Program closed')
            break
        if z == 2:
            logging.info('Program continue with users command')
            continue


calc()
