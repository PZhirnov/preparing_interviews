# Задание №2


class ItemDiscount:
    __name = 'Audi A6'
    __price = 6000000

    def __init__(self):
        self.name = self.__name
        self.price = self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.name} {self.price}'
        # return f'{self._ItemDiscount__name} {self._ItemDiscount__price}'


item = ItemDiscountReport()
# print(ItemDiscount.__dict__)
print(item.get_parent_data())
