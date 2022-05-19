# Задание №3
# Реализовать возможность переустановки значения цены товара в родительском классе.
# Проверить, распечатать информацию о товаре.


class ItemDiscount:
    __name = 'Audi A6'
    __price = 6000000

    def __init__(self):
        self.name = self.__name
        self.price = self.__price

    def new_price(self, price):
        self.price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.name} {self.price}'
        # return f'{self._ItemDiscount__name} {self._ItemDiscount__price}'


item = ItemDiscountReport()
print(item.get_parent_data())

# Переустановим цену товара и выведем опять результат
item.new_price(7777777)
print(item.get_parent_data())

# Результат:
'''
Audi A6 6000000
Audi A6 777
'''
