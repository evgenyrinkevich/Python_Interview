# Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
# Выполнить перегрузку методов конструктора дочернего класса
# (метод __init__, в который должна передаваться переменная — скидка), и перегрузку метода __str__ дочернего класса.
# В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
# Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
# (вторая и третья строка после объявления дочернего класса).

class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount_percent=0):
        super().__init__(name, price)
        self.discount_percent = discount_percent

    def __str__(self):
        discount_price = self.price - self.price * self.discount_percent / 100
        return f'{self.name} {discount_price:.0f}'

    def get_parent_data(self):
        return f'{self.name} {self.price}'


if __name__ == '__main__':

    item_disc = ItemDiscount('Audi', 50000)
    item_disc_report = ItemDiscountReport('BMW', 70000, 10)

    print(item_disc_report)
