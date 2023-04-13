# Задача №37. Общее обсуждение
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

import random


def inverse(list_num):
    if len(list_num) > 0:
        print(list_num[-1], end=' ')
        del list_num[-1]
        inverse(list_num)


n = int(input('Введите количество элементов: '))
list_number = [random.randint(0, 50) for i in range(n)]
print(list_number)
inverse(list_number)
