# Задача №2. Проверка числа


def what_a_number(val):
    try:
        val_to_float = float(val)
        if val_to_float % 1 == 0:
            return 'Вы ввели целое число!'
        else:
            parts = val.split('.')
            values_match = ' ' if parts[0] == parts[1] else ' не '
            return f'Введено дробное число!\nЗначения до и после ' \
                   f'запятой{values_match}совпадают'
    except ValueError:
        return 'Вы ввели не число!'


while True:
    val_str = input('Введите число или q для выхода:')
    if val_str == 'q':
        break
    print(what_a_number(val_str))
