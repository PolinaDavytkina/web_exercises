# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
import re

# d = {}
# vlan = input('Введите номер vlan: ')
# f = open('CAM_table.txt')
# for line in f:
#     if re.search(r'([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4})',line)!=None:
#         v=int(line.split()[0])
#         d.setdefault(v,line)

# print(d[int(vlan)])

dictionary = {}
myvlan = input('Введите номер vlan: ')
file = open('CAM_table.txt')
for line in file:
    if re.search(r'([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4})',line)!=None:
        vlan=int(line.split()[0])
        if vlan in dictionary:
            mylist = dictionary[vlan]
        else:
            mylist = []
        mylist.append(line)
        dictionary[vlan]=mylist
myvlan=int(myvlan)

for line in dictionary[myvlan]:
    print(line.replace('DYNAMIC     ',''),end='')