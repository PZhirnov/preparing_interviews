# Задача 4. Создание файла, со значениями из двух генераторов

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
        number_gen = (str(randint(100, 999)) for i in range(NUM_ROWS))
        text_gen = ('example' for i in range(NUM_ROWS))
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


# Первая часть условия - создание файла с данными
create_file('data_file.txt')

# Вывод данных
read_file('data_file.txt')
