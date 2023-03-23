# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает количество повторов каждого символа

str_1 = 'a a a b c a a d c d d'

new_dict = {}

for i in str_1:
    if i in new_dict:
        new_dict[i] += 1
    else:
        new_dict[i] = 1
print(new_dict)

