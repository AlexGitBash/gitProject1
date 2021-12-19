# 1.Создать программно файл в текстовом формате,
# записать в него построчно данные,вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

a = open('file.txt', 'w')
line = input('Ваш текст \n')
while line:
    a.writelines(line)
    line = input('Ваш текст \n')
    if not line:
        break

a.close()
a = open('file.txt', 'r')
content = a.readlines()
print(content)
a.close()

# 2.Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file666 = open('file666.txt', 'r')
content = file666.read()
print(f'Содержимое файла: \n {content}')
file666 = open('file666.txt', 'r')
content = file666.readlines()
print(f'Количество строк в файле - {len(content)}')
file666 = open('file666.txt', 'r')
content = file666.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
file666 = open('file666.txt', 'r')
content = file666.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
file666.close()

# 3.Создать текстовый файл (не программно), построчно записать
# фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.

with open('sal.txt', 'r') as file777:
    sal = []
    poor = []
    _list = file777.read().split('\n')
for i in _list:
        i = i.split()
if int(i[1]) < 20000:
    poor.append(i[0])
sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')

# 4.Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file8 = []
with open('file_.txt', 'r') as file_obj:
    content = file_obj.read().split('\n')
for i in file_obj:
    i = i.split(' ', 1)
file8.append(rus[i[0]] + ' ' + i[1])
print(file8)

with open('file__new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(file8)




# 6. Необходимо создать (не программно) текстовый файл, где
# каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика:
# 100(л)   50(пр)   20(лаб).

# Физика:   30(л)   —   10(лаб)
# Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40,
# “Физкультура”: 30}

subj = {}
with open('file_f.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
subj[subject] = int(lecture) + int(practice) + int(lab)
print(f'Общее количество часов по предмету - \n {subj}')

