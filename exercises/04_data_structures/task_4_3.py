# -*- coding: utf-8 -*-
"""
Задание 4.3

Получить из строки config такой список VLANов:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config=config.split()
config=config[-1].split(',')
print(config)