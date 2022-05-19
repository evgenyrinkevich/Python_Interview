# Реализовать возможность переустановки значения цены товара в родительском классе.
# Проверить, распечатать информацию о товаре.

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.get_name()} {self.get_price()}'


if __name__ == '__main__':

    item_disc = ItemDiscount('Audi', 50000)
    item_disc.set_name('Mercedes')
    item_disc_report = ItemDiscountReport('BMW', 70000)
    item_disc_report.set_price(90000)

    print(item_disc_report.get_parent_data())
    print(item_disc.get_name())



