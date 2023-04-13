# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                                   Вывод:
# 7                                      3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)


def input_array(len_array):
    new_arr = []
    for _ in range(len_array):
        new_arr.append(input('Введите элемент: '))
    return new_arr


def comparison_array(arr1, arr2):
    new_list = []
    arr2_set = set(arr2)
    for i in range(len(arr1)):
        if arr1[i] in arr2_set:
            new_list.append(arr1[i])
    return new_list


n = int(input('Введите размер массива 1: '))
array1 = input_array(n)
print(array1)
m = int(input('Введите размер массива 2: '))
array2 = input_array(m)
print(array2)
output_list = comparison_array(array1, array2)
print(output_list)
