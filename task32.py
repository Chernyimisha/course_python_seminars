# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

n = 50
list_number = [random.randint(0, 100) for _ in range(n)]
print(list_number)


def diap_index(list_num, minimum, maximum):
    new_list = []
    for i in range(len(list_num)):
        if minimum <= list_num[i] <= maximum:
            new_list.append(i)
    return new_list


min_el = int(input('Введите минимальный элемент: '))
max_el = int(input('Введите максимальный элемент:'))
indexes = diap_index(list_number, min_el, max_el)
print(indexes)
