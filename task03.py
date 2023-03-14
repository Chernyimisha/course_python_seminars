a = int(input('Введите целое число:'))
count = 0

while a != 0:
    a /= 10
    a = int(a)
    count += 1

if count == 4:
    print("YES")
else:
    print("NO")
