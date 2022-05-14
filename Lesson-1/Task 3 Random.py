import math
from timeit import timeit


def randint(start, end=None):
    if not end:
        start = 0
        end = start
    len_range = end - start + 1
    get_time = int(str(timeit('"-".join(str(n) for n in range(100))',
                              number=10))[::-1][:6])
    gen_num = int(str(id(get_time))[::-1][:4]) + get_time
    sin = abs(math.sin(round(math.radians(gen_num), 1)))
    delta = int(len_range * sin)
    res_val = start + delta
    return res_val


# Проверка по условию:
# Выведем словарь с порядковым номером и сгенерированным значением
res_dict = {}
f = set()  # множество используется для проверки количества уникальных
for i in range(1000):
    f.add(randint(0, 1000))
    res_dict[i] = randint(0, 1000)
print(res_dict)
print(len(f))

"""
Вывод:
На 1000 вызовов функции генерируется порядка 550-600 уникальных.
Функция randint выдает порядка 630. 
"""

# from random import randint
# f = set()
# for i in range(1000):
#     f.add(randint(1, 1000))
# print(len(f))


# Вариант с генератором в функции
# def rnd():
#     start = 0
#     end = 10
#     len_range = end - start + 1
#     jtime = int(str(timeit('"-".join(str(n) for n in range(100))', number=100))[::-1][:6])
#     gen_num = (int(str(id(i))[::-1][:5]) + jtime for i in range(len_range))
#     res = {}
#     for num, _ in enumerate(range(len_range - 1)):
#         g = next(gen_num)
#         sin = abs(math.sin(round(math.radians(g), 1)))
#         delta = int(len_range * sin)
#         res[num] = start + delta
#     gen_num = delta
#     return res
#
# print(rnd())
# print(rnd())
