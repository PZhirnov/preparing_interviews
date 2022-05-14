import os
from os import listdir, path


def print_directory_contents(path_dir):
    """
    Функция принимает имя директории и выводит ее содержимое,
    включая содержимое всех поддиректории (рекурсивно вызывая саму себя)
    :param path_dir: путь к интересующему каталогу
    :return: функция сразу выводит в консоль
    """
    list_obj = listdir(path_dir)
    for obj in list_obj:
        path_obj = path.join(path_dir, obj)
        if path.isfile(path_obj):
            print(path_obj)
        else:
            print(path_obj)
            print_directory_contents(path_obj)


# Проверка - запуск с текущего каталога
print_directory_contents(r".")
