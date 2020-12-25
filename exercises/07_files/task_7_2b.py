# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


ignore = ["duplex", "alias", "Current configuration"]

file1 = open('C:/Users/Полина/Desktop/Учеба 3 семестр/Веб-программирование/web_exercises/exercises/07_files/config_sw1.txt')
file2 = open('C:/Users/Полина/Desktop/Учеба 3 семестр/Веб-программирование/web_exercises/exercises/07_files/config_sw1_cleared.txt','w')
for line in file1:
    
    if (line.strip()):
        
        flag = True
        for x in ignore:
            if line.find(x)!=-1:
                flag = False
                break
        if flag:
            file2.write(line)