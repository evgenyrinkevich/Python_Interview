# Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
# Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.get_name()} {self.get_price()}'


if __name__ == '__main__':

    item_disc = ItemDiscount('Audi', 50000)
    item_disc_report = ItemDiscountReport('BMW', 70000)
    try:
        print(item_disc.__name)
    except AttributeError:
        print("Can't access private attribute!")

    print(item_disc_report.get_parent_data())
