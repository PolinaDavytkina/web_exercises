# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route=ospf_route.split()
ospf_route1=ospf_route[0]
ospf_route2=ospf_route[1].strip('[]')
ospf_route3=ospf_route[3].strip(',')
ospf_route4=ospf_route[4].strip(',')
ospf_route5=ospf_route[5]

prefix="Prefix"
adm="AD/Metric"
nh="Next-Hop"
lu="Last update"
oi="Outbound Interface"
print("{:20} {:20}".format(prefix, ospf_route1))
print("{:20} {:20}".format(adm, ospf_route2))
print("{:20} {:20}".format(nh, ospf_route3))
print("{:20} {:20}".format(lu, ospf_route4))
print("{:20} {:20}".format(oi, ospf_route5))
