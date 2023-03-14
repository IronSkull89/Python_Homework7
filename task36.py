# Задача 36: На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран получившийся кортеж.

str = "house=дом car=машина men=человек tree=дерево"

def str_to_tp_tp(str, delimiter1, delimiter2):
    ls = list(str.split(delimiter1))
    ls_tp = []

    for item in ls:
        ls_tp.append(tuple(item.split(delimiter2)))

    tp_tp = tuple(ls_tp)

    return tp_tp

print(str_to_tp_tp(str, ' ', '='))