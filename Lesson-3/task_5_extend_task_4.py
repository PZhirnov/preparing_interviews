# Задача 5. Создание файла, со значениями из двух генераторов
"""
Порядок доработок:
1. Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений (выбирается случайно)
заменить на значения типа 345example (в обратном порядке, число и строка).

2. Реализовать функцию поиска определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений.

3. Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.
"""


from os import path
from random import randint

NUM_ROWS = 10  # количество записей в генераторах


def create_file(file_name):
    """
    Функция создает файл по условию задачи. Если файл существует,
    то выводится соответствующее сообщение и файл закрывается.
    """
    if path.exists(file_name):
        print(f'Файл с именем \'{file_name}\' существует!')
        return True
    else:
        # Генераторы по условию задачи
        # 1 усл. Рандомно добавляется слово example в списке с числами - пример: 345example.
        add_word = ['', 'for_search_-old_text']
        number_gen = (str(randint(100, 999)) + add_word[randint(0, 1)] for _ in range(NUM_ROWS))
        text_gen = ('example' for _ in range(NUM_ROWS))
        data_zip = list(map(lambda x: ''.join(x) + '\n',
                            zip(text_gen, number_gen)))
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(data_zip)
        print(f'Файл с именем \'{file_name}\' был создан!')
        return True


def read_file(file_name):
    """
    Функция читает данные из файла и делает построчный вывод
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        for i in f:
            print(i, end='')


def find_text(file_name, txt, find_all=False):
    """
    Функция выводит результаты поиска по второму условию задачи - см. п.2
    :param file_name: имя файла
    :param txt: строка, которую ищем
    :param find_all: если True, то выводим все результат поиска
    """
    with open(file_name, 'r', encoding='utf8') as f:
        for line in f:
            if txt in line:
                print(line, end='')
                # find_all = True, то завершаем работу
                if not find_all:
                    break


def replace_txt(file_name, old_txt, new_txt):
    """
    Функция замены строковых значений в файле
    :param file_name: имя файла
    :param old_txt: старый текст
    :param new_txt: новый текст
    """
    with open(file_name, 'r', encoding='utf8') as f:
        f_in_lines = f.readlines()
    f_out_lines = list(map(lambda x: x.replace(old_txt, new_txt), f_in_lines))
    with open(file_name, 'w', encoding='utf8') as f:
        f.writelines(f_out_lines)


# Проверка:

# Первая часть условия - создание файла с данными
create_file('data_file_task5.txt')

# Вывод всех строк из файла
print('--- Вывод всего содержимого файла ---')
read_file('data_file_task5.txt')


# ------ Условие 2 ----
# Поиск определенных подстрок в файле по следующим условиям:
# вывод первого вхождения
print('--- Вывод первого вхождения ---')
find_text('data_file_task5.txt', 'for_search', False)
# вывод всех вхождений.
print('--- Вывод всех вхождений ---')
find_text('data_file_task5.txt', 'for_search', True)

# --- Условие 3 -----
print('--- Замена строковых значений ---')
replace_txt('data_file_task5.txt', 'old_text', 'new_text')
# Выведем еще раз результат после замены:
read_file('data_file_task5.txt')
