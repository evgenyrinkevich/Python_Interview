# Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
# При вызове функции в качестве аргумента должно передаваться путь и имя файла с расширением.
# В функции необходимо реализовать поиск имени файла (с расширением), а затем «выделение» имени файла (без расширения).
# Расширений может быть несколько (например testfile.tar.gz).

import os


def file_name_extension(path):
    try:
        filename = os.path.basename(path).split('.')
        return filename[0], filename[1:]
    except TypeError:
        print('Invalid path')
        return


if __name__ == '__main__':
    cwd_path = os.getcwd()
    test_path = os.path.join(cwd_path, 'testfile.tar.gz')
    print(file_name_extension(test_path))
    print(file_name_extension(__file__))
