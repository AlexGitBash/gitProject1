# 1. Создать класс TrafficLight (светофор) и
# определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time
from os import name


class TrafficLight:
    color = 'Красный'


print('Светофор')


def running(self):
    self.color = ' ☺'
    print(f' ''\033[31m {}'.format(self.color))
    time.sleep(7)

    self.color = ' ☺'
    print(f' ''\033[33m {}'.format(self.color))
    time.sleep(2)

    self.color = ' ☺'
    print(f' ''\033[32m {}'.format(self.color))
    time.sleep(10)

    while True:
        self.running()


trafficLight = TrafficLight()
print(trafficLight.running())


# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:

    def __init__(self, length, width1):
        self._length = length
        self._width = width1
        self.weight = 25
        self.height = 5


def m(self):
    mass = self._length * self._width * self.weight * self.height / 1000
    print(f'Нужно для покрытия - {round(mass)} т')


r = Road(10000, 20)
r.m()


# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self):
        self.name = name

    def of(self, _name, surname, position, wage, bonus):
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def init(self, name, surname, position, wage, bonus):
        super().init(name, surname, position, wage, bonus)


def get_full_name(self):
    return self.name + ' ' + self.surname


def get_total_income(self):
    return self._income.get('wage') + self._income.get('bonus')


c = Position('John', 'The Great', 'Beekeeper', 200000, 30000)
print(c.get_full_name())
print(c.position)
print(c.get_total_income())
