# Разработать целочисленный генератор случайных чисел.
# В функцию передавать начальную и конечную границу диапазона генерации (выдавать значения из диапазона включая концы).
# Заполнить этими данными словарь.
# Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”, а значене сгенеренное случайное число.
# Вывести содержимое словаря.
# (Усложненный вариант по желанию*): Не использовать стандартный модуль python random.

from pprint import pprint
import time


def rand_val(start, end):
    """
    Returns a pseudo-random integer in range [start, end]
    introduces a 0.01sec latency, otherwise would return same number if used in a loop
    """
    rand = int(time.time() * 1000)
    rand %= end - start + 1
    time.sleep(0.01)  # Приходиться спать, иначе в цикле все числа одинаковые

    return start + rand


def generate_random(start, end, length=10):
    result = {}
    for i in range(length):
        result[f'elem_{i + 1}'] = rand_val(start, end)

    return result


if __name__ == '__main__':
    pprint(generate_random(-1, 10))
