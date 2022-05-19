# Задание №5
"""
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
нициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать вызов каждой из функции get_info.
"""


class ItemDiscount:
    name = 'Audi A6'
    price = 6000000


class ItemReport(ItemDiscount):

    def get_info(self):
        return self.name


class DiscountReport(ItemDiscount):

    def get_info(self):
        return self.price


# Выводим результат по условию задачи
name = ItemReport().get_info()
price = DiscountReport().get_info()
print(f'{name} {price}')
