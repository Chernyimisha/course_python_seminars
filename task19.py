# Задача №19. Общее обсуждение
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

list_numbers = [1, 2, 3, 4, 5]
k = 3
list_numbers = list_numbers[-k:] + list_numbers[:-k]
# for _ in range(k):
#     list_numbers.insert(0, list_numbers[-1])
#     list_numbers.pop(list_numbers[-1])

print(list_numbers)
