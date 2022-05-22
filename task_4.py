# Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
# Необходимо открыть файл и создать два списка: с текстовой и числовой информацией.
# Для создания списков использовать генераторы. Применить к спискам функцию zip().
# Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
# чтобы каждая строка файла содержала текстовое и числовое значение (например example345). Вызвать вторую функцию.
# В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать открытие файла и простой,
# построчный вывод содержимого.
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
                f.write(''.join(line) + '\n')

    except FileExistsError:
        print('File already exists!')
        sys.exit(1)


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    write_to_file('test.txt')
    read_file('test.txt')
