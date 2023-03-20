# Задача №17. Общее обсуждение
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

list_numbers = [1, 1, 2, 0, -1, 2, 3, 4, 4]
# count = 0
# list.sort(list_numbers)
# for i in range(len(list_numbers)):
#     if list_numbers[i] != list_numbers[i-1]:
#         count += 1
set_numbers = set(list_numbers)
print(set_numbers)

print(f'{list_numbers} -> {len(set_numbers)}')





