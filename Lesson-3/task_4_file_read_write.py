# Задача 4. Создание файла, со значениями из двух генераторов

from os import path
from random import randint


def create_file(file_name):
    """
    Функция создает файл по условию задачи. Если файл существует, то выводится соответствующее сообщение
    и файл закрывается
    :param file_name:
    :return:
    """
    if path.exists(file_name):
        print(f'Файл с именем \'{file_name}\' существует!')
        return True
    else:
        # Генераторы по условию задачи
        number_gen = (str(randint(100, 999)) for i in range(10))
        text_gen = (f'{chr(randint(97, 122))*5}' for i in range(10))  # рандомный символ повторяется 5 раз для теста
        data_zip = list(map(lambda x: ''.join(x) + '\n', zip(text_gen, number_gen)))
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(data_zip)
        print(f'Файл с именем \'{file_name}\' был создан!')
        return True


def read_file(file_name):
    """
    Функция читает данные из файла по условию задачи
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        for i in f:
            print(i, end='')

# Первая часть условия - создание файла с данными
create_file('data_file.txt')

# Вывод данных
read_file('data_file.txt')
