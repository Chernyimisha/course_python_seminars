# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random

n = int(input('Сколько оценок у хакера Василия?: '))
random_list = [random.randint(1, 5) for i in range(n)]
print(random_list)


def inverse_max_min(list):
    min_el = min(list)
    max_el = max(list)

    for i in range(len(list)):
        if list[i] == max_el:
            list[i] = min_el
    return list
print(inverse_max_min(random_list))
# print(random_list)
