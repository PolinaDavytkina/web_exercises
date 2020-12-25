# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip=input('Введите IP-сети в формате: 10.1.1.0/24: ' )
mas=ip.split("/")
ip=mas[0]
mas=int(mas[1])
maskb="1"*mas+"0"*(32-mas)
octm1=int(maskb[:8], 2)
octm2=int(maskb[:16][8:], 2)
octm3=int(maskb[:24][16:], 2)
octm4=int(maskb[24:], 2)
temp = '''
    {:10} {:10} {:10} {:10}
    {:10b} {:10b} {:10b} {:10b}
    '''
ip=ip.split(".")
oct1=int(ip[0])
oct2=int(ip[1])
oct3=int(ip[2])
oct4=int(ip[3])
print("Network:")
print(temp.format(oct1, oct2, oct3, oct4, oct1, oct2, oct3, oct4))
print("Mask")
print(temp.format(octm1, octm2, octm3, octm4, octm1, octm2, octm3, octm4))