# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
mac=mac.split(":")
mac1=mac[0]
mac2=mac[1]
mac3=mac[2]
mac1=int(mac1, 16)
mac1=bin(mac1)[2:]
mac2=int(mac2, 16)
mac2=bin(mac2)[2:]
mac3=int(mac3, 16)
mac3=bin(mac3)[2:]

print(mac1+mac2+mac3)
