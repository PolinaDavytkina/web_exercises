# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
ip=argv[1]
mas=int(argv[2])

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
nw1=str(bin(oct1)[2:])
nw2=str(bin(oct2)[2:])
nw3=str(bin(oct3)[2:])
nw4=str(bin(oct4)[2:])

Network='0'*(8-len(nw1))+nw1+'0'*(8-len(nw2))+nw2+'0'*(8-len(nw3))+nw3+'0'*(8-len(nw4))+nw4
Network=Network[:mas]
Network=Network+"0"*(32-len(Network))

oct1=int(Network[:8], 2)
oct2=int(Network[:16][8:], 2)
oct3=int(Network[:24][16:], 2)
oct4=int(Network[24:], 2)

print("Network:")
print(temp.format(oct1, oct2, oct3, oct4, oct1, oct2, oct3, oct4))
print("Mask")
print(temp.format(octm1, octm2, octm3, octm4, octm1, octm2, octm3, octm4))