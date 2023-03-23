# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = '''She sells sea shells on the sea shore The shells that she sells are sea ''' \
       '''shells I'm sure. So if  she sells sea shells on the sea shore I'm sure that ''' \
       '''the shells are sea shore shells'''

text = text.lower()
temp_str = ''
set_str = set()

for i in text:
    if i == ' ' or i == '.':
        if temp_str != '':
            set_str.add(temp_str)
            temp_str = ''
    else:
        temp_str += i
set_str.add(temp_str)
print(set_str)
print(len(set_str))

