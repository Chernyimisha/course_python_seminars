# Создайте список из случайных
# Найдите номер его последнего локального максимума(локальный максимум - это элемент,
# который больше любого из своих соседей)

import random
n = 10
list_number = [random.randint(-100, 100) for _ in range(n)]
print(list_number)
local_max = 0
index_max = 0
for i in range(len(list_number) - 2, 0, -1):
    if list_number[i-1] < list_number[i] > list_number[i+1]:
        local_max = list_number[i]
        index_max = i
        break
print(local_max, index_max)

