# Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
# целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.

def digits_count(num):
    try:
        int(num)
        print('The number is integer')
    except ValueError:
        try:
            float(num)
            print('The number is float')
            fraction, integer = num.split('.')
            return sum(int(el) for el in integer) == sum(int(el) for el in fraction)
        except ValueError:
            return 'Wrong data'


if __name__ == '__main__':
    n = input('Enter a number: ')
    print(digits_count(n))
