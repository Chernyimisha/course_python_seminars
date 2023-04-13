# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n= a1+ (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def arithmetic_progression(a1, delta, number):
    new_array = []
    for i in range(number):
        new_array.append(a1+delta*i)
    return new_array


a = int(input('Введите первый элемент прогрессии: '))
n = int(input('Введите разность: '))
d = int(input('Введите количество элементов прогрессии: '))

new_array_ap = arithmetic_progression(a, n, d)
print(new_array_ap)

