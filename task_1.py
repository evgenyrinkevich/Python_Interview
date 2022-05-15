# Вывести таблицу умножения в виде.
# 1 x 1 = 1
# 1 x 2 = 2
# ..
# 1 x 10 = 10
# —
# 2 x 1 = 2
# 2 x 2 = 4
# …
# N x 10 = 10N
# Параметр N задается с клавиатуры (или в виде аргумента скрипта, по желанию)
# Между разделами вывести разделитель в виде 5 девисов


def multiplication_table(x, y):
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            print(f'{i} X {j} = {i * j}')
        print('-' * 5)


if __name__ == '__main__':
    while True:
        try:
            n = input('Enter size of multiplication table(q to quit): ')
            if n == 'q':
                break
            multiplication_table(int(n), 10)
        except ValueError as e:
            print('Enter a number please!')

