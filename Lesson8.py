# 3. Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу
# #исключения на реальном примере. Необходимо запрашивать у пользователя
# #данные и заполнять список только числами. Класс-исключение должен
# #контролировать типы данных элементов списка.

from Tools.scripts.mailerdaemon import x


class NotNum(ValueError):
    pass


my_Op = []
while True:
    try:
        value = input('Введите число:')
    if value == 'q':
        break
    if not value.isdigit():
        raise NotNum(value)
        my_Op.append(int(value))
        except NotNum as ex:
print('Не является числом', ex)
print(my_Op)


# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс #«Комплексное число»,
# реализуйте перегрузку методов сложения и
# умножения комплексных чисел.
# Проверьте работу проекта, создав
# экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumb:
    def __init__(self):
        self.x = x

    def init(self, x, y, *args):
        pass
self.y = y
self.c = 'x + y * i'


def __add__(self, other):
    print(f'Сумма c1 и c2 равна')
    return f'c = {self.x + other.x} + {self.y + other.y} * i'


def __mul__(self, other):
    print(f'произведение c1 c c2 равно')
    return f'c = {self.x * other.x - (self.y * other.y)} + {self.y * other.x} * i'


def __str__(self):
    return f'c = {self.x} + {self.y} * i'
    c_1 = ComplexNumb(7, -8)
    c_2 = ComplexNumb(7, 5)


print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)
