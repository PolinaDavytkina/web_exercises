# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
str1=command1.split()
str1=str1[-1].split(',')
set1=set(str1)
str2=command2.split()
str2=str2[-1].split(',')
set2=set(str2)
lists=list(set1 & set2)
print(lists)