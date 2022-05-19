# Задание №1


class ItemDiscount:
    name = 'Audi A6'
    price = 6000000


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.name} {self.price}'


#  результаты по условию задачи
item_parent = ItemDiscount
print(item_parent.__dict__)

item_child = ItemDiscountReport()
print(ItemDiscountReport.__dict__)
print(item_child.get_parent_data())  # Audi A6 6000000


# изменим атрибут родительского класса и посмотрим на результат
item_parent.name = 'Lada Kalina'
print(item_child.get_parent_data())  # Lada Kalina 6000000
