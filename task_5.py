# Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
# Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
# которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
# Далее реализовать вызов каждой из функции get_info.

class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountName(ItemDiscount):
    def get_info(self):
        return self.name


class ItemDiscountPrice(ItemDiscount):
    def get_info(self):
        return self.price


if __name__ == '__main__':

    item_name = ItemDiscountName('Audi', 50000)
    item_price = ItemDiscountPrice('BMW', 70000)

    [print(obj.get_info()) for obj in (item_name, item_price)]
