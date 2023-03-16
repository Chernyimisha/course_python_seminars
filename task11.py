# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = int(input('Введите число A > 1: '))
n = 2
first_count = 0
second_count = 1
count = 0

while count <= a:
    count = first_count + second_count
    n += 1
    if count == a:
        print(n)
        break
    first_count = second_count
    second_count = count
else:
    print(-1)
