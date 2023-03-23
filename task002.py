# Создайте список из случайных
# Найдите второй максимум.

# import random
# n = 10
# list_number = [random.randint(-100, 100) for _ in range(n)]
list_number = [10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list_number)

# list_number.sort()
# print(list_number[-2])
first_max = second_max = 0

for i in list_number:
    if i > first_max:
        first_max = i
    elif i > second_max and i != first_max:
        second_max = i
print(second_max)

