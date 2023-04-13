# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_num_simple(num):
    if num != 2 and num % 2 != 0:
        for i in range(3, num // 2 + 1, 2): # берется диапазон от 3 до середины num, включая послений элемент, с шагом 2
            if num % i == 0:
                print('No')
                break
        else:
            print('yes')
    else:
        print('no')


n = int(input('Введите проверяемое число: '))
is_num_simple(n)
