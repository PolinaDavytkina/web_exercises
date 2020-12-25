# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]

file = open('C:/Users/Полина/Desktop/Учеба 3 семестр/Веб-программирование/web_exercises/exercises/07_files/config_sw1.txt')
for line in file:
    if (line.strip()) and (line[0]!='!'):
        flag = True
        for x in ignore:
            if line.find(x)!=-1:
                flag = False
                break
        if flag:
            print(line,end='')
file.close()