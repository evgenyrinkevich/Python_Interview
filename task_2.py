# Реализовать функцию print_directory_contents(path).
# Функция принимает имя директории и выводит ее содержимое,
# включая содержимое всех поддиректории (рекурсивно вызывая саму себя).
# Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile

import os


def print_directory_contents(path):
    for el in os.listdir(path):
        if os.path.isfile(os.path.join(path, el)):
            print(os.path.join(path, el))
        else:
            print(os.path.join(path, el))
            print_directory_contents(os.path.join(path, el))


if __name__ == '__main__':
    print_directory_contents('.')
