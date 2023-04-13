# Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку, сворачивая
# соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

import random

# list_number = [1, 4, 5, 2, 3, 9, 8, 11, 0]
n = int(input('Введите размер массива: '))
random_list = sorted(set([random.randint(0, 50) for i in range(n)]))
print(random_list)


# def range_number(list_num):
#     if not list_num:
#         return ''
#     list_num = sorted(list_num) + [None]
#
#     start_group = list_num[0]
#     result = ''
#
#     for i in range(1, len(list_num)):
#         if list_num[i] == list_num[i - 1] + 1:
#             continue
#
#         if result:
#             result += ','
#
#         result += str(start_group)
#         if list_num[i - 1] != start_group:
#             result += '-' + str(list_num[i - 1])
#
#         start_group = list_num[i]
#
#     return result
#
#
# print(range_number(random_list))

def range_number(list_num):
    list_num.append(1.9)
    result_temp = []
    result = []
    for i in range(len(list_num) - 1):
        if list_num[i] == list_num[i + 1] - 1:
            result_temp.append(list_num[i])
        else:
            if list_num[i] not in result_temp:
                result_temp.append(list_num[i])
            result.append(result_temp)
            result_temp = []
    print(result)
    result_str = []
    for i in result:
        if len(i) >= 2:
            result_str.append(f"{i[0]}-{i[-1]}")
        else:
            result_str.append(f"{i[0]}")
    return result_str


print(*range_number(random_list), sep=',')
