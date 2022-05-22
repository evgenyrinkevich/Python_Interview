# Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
# (выбирается случайно) заменить на значения типа 345example (в обратном порядке, число и строка).
# Реализовать функцию поиска определенных подстрок в файле по следующим условиям: вывод первого вхождения,
# вывод всех вхождений. Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.
import re
import string
import sys
from random import choices, randint

ALPHABET = list(string.ascii_lowercase)
DIGITS = [str(num) for num in range(10)]
MIN_TEXT_LENGTH = 3
MAX_TEXT_LENGTH = 5
LIST_LENGTH = 10


def make_list(source, min_text_length=MIN_TEXT_LENGTH, max_text_length=MAX_TEXT_LENGTH, list_length=LIST_LENGTH):
    """
    Returns a list of, containing list_length elements, each min_text_length to max_text_length from source list
    :param source: source list
    :param min_text_length: min length of an element
    :param max_text_length: max length of an element
    :param list_length:
    """
    return [''.join(choices(source, k=randint(min_text_length, max_text_length))) for _ in
            range(list_length)]


def write_to_file(filename):
    try:
        with open(filename, 'x', encoding='utf-8') as f:
            text_list = make_list(ALPHABET)
            num_list = make_list(DIGITS)
            for line in zip(text_list, num_list):
                index = randint(0, 1)
                # line is a tuple of 2 elements, so index and not index are 0, 1 or 1, 0
                f.write(''.join([line[index], line[not index]]) + '\n')

    except FileExistsError:
        print('File already exists!')
        sys.exit(1)


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


def find_all(a_str, sub):
    """
    Finds indexes of all occurrences of sub string in a_str
    """
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


def find_substring(substring, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        indexes = [str(el) for el in find_all(f.read(), substring)]
        print(f'Found {substring} on {",".join(indexes)} indexes in {filename}')


def replace_substring(sub_old, sub_new, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        new_text = ''
        for line in f.readlines():
            if sub_old in line:
                line = line.replace(sub_old, sub_new)
                print(f'Changed this line -> {line}')
            new_text += line
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_text)


if __name__ == '__main__':
    find_substring('z', 'test.txt')
    replace_substring('qxl', 'qaw', 'test.txt')
