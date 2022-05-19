# Задание №4
"""
Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод __init__,
в который должна передаваться переменная — скидка),
и перегрузку метода __str__ дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно,
не забудьте инициализировать дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:
    __name = 'Audi A6'
    __price = 6000000

    def __init__(self):
        # см. условие задачи №2
        self.name = self.__name
        self.price = self.__price

    def new_price(self, price):
        self.price = price


class ItemDiscountReport(ItemDiscount):
    
    def __init__(self, discount=0):
        super().__init__()
        self.discount = discount

    def __str__(self):
        self.price = self.price * (1 - self.discount / 100)
        return f'Цена со скидкой {self.discount}% : {self.name} {self.price}'

    def get_parent_data(self):
        return f'{self.name} {self.price}'


# Вывод результатов
item = ItemDiscountReport(10)
print(item)
