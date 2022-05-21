# Задача №3. Объединить списки в словаре

import itertools

list_one = [1, 2, 3, 4, 5, 6, 7]
list_two = ['один', 'два', 'три', 'четыре', 'пять']

c = itertools.zip_longest(list_one, list_two)
res_dict = {i[0]: i[1] for i in c}

# Вывод результата
print(res_dict)  # {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: None, 7: None}
