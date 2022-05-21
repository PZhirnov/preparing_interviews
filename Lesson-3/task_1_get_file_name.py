# Задача №1. Вывести имя файла без расширения

from os.path import basename, splitext


def get_file_name(path):
    name_file = splitext(basename(path))[0]
    return name_file


test_path = r'C:\Users\Pavel\YandexDisk\_GeekBrains_Обучение' \
            r'\Lesson-3\name.kz.py'

res = get_file_name(test_path)
print(res)
