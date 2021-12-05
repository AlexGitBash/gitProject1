# Задание 1.
# example1
aU = 8
bU = 9
print(aU, bU)
# example2
aU = int(input('Введите число: '))
aC = str(input('Выберите слово: '))
print('Ваше число:', aU, 'Ваше слово: ', aC)

# Задание 2

r = int(input('Введите время в секундах: '))
hours = str(r // 3600)
minutes = str((r // 60) % 60)
seconds = str(r % 60)
print(hours + ":" + minutes + ":" + seconds)

# 3. Задание
n = int(input('Введите Ваше число: '))
p = str(n)
p1 = p + p
p2 = p + p + p
vs = n + int(p1) + int(p2)
print('Вывод: ', p, "+", p1, "+", p2, "=", vs)
