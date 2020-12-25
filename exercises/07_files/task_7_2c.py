# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

file0=input()
#from sys import argv
#file0 = argv[2]

file2 = open(file0,'w')
file1 = open('config_sw1.txt')

for line in file1:
    if (line.strip()):
        flag = True
        for x in ignore:
            if line.find(x)!=-1:
                flag = False
                break
        if flag:
            file2.write(line)