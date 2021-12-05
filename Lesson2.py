# 1.Задание
a_list = [4, 5, 6, 76, True, 4.6, None]


def a_type():
    for f in range(len(a_list)):
        print(type(a_list[f]))

    return


a_type()

# 2.Задание
my_l = input("Введите элементы списка: ").split()
my_l[:-1:2], my_l[1::2] = my_l[1::2], my_l[:-1:2]
print(my_l)

# 3.Задание
mouth = int(input("Введите число месяца от 1-12: "))

_list = ['Зима', 'Весна', 'Лето', 'Осень']
_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
         10: 'Осень', 11: 'Осень', 12: 'Зима'}

if mouth < 4:
    print(_list[0])
elif mouth > 7:
    print(_list[1])
elif mouth > 9:
    print(_list[3])
else:
    print(_list[2])

    print(_dict[mouth])

# 4.Задание
uS = input('Введите слова через пробел: ')
uS = uS.split(' ')
for i, uS in enumerate(uS):
    print(i + 1, uS[:10])

# 5.Задание

n = [9, 7, 5, 5, 3]
userN = int(input('Введите число рейтинга: '))
for i in range(0, len(n)):
    if userN >= n[i]:
        n.insert(i, userN)
        break
    if userN not in n:
        n.append(userN)
        print(n)
