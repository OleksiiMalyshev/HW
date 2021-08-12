import threading
import logging
import time
import math

format = "%(asctime)s : %(message)s"
logging.basicConfig(format=format, level=logging.INFO)

logging.info('quadratic equation will be in format " ax^2 + bx + c = 0 "')


def thread_func(name, a: float, b: float, c: float):
    logging.info("Thread %s: starting", name)
    logging.info(f'Thread {name}: a={a} b={b} c={c}')
    logging.info(f'Thread {name}: started thinking')
    time.sleep(1)
    d = (b ** 2) - (4 * a * c)
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    logging.info(f'Thread {name}: Discriminant = {d}')
    if d > 0:
        logging.info(f'Thread {name}: There are two solutions')
        logging.info(f'Thread {name}: x1 = {x1:.2f}, x2 = {x2:.2f}')
    elif d == 0:
        logging.info(f'Thread {name}: There is one solution')
        logging.info(f'Thread {name}: x = {x1}')
    elif d < 0:
        logging.info(f'There is no solution')
    logging.info(f'Thread {name}: stopping')


logging.info('Main  : before creating thread')
x = threading.Thread(target=thread_func, args=(1, 3, 13, -10))
logging.info('Main  : before running thread')
logging.info('Main  : before creating thread')
y = threading.Thread(target=thread_func, args=(2, 2, 10, -15))
logging.info('Main  : before running thread')
x.start(), y.start()
logging.info('Main  : wait for the threads to finish')
logging.info('Main  : all done')
