# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 18:01:56 2022

@author: bruco
"""

import datetime as dt 
import dateutil

string = str(input("Date:"))

parameters = str(input("Relativedelta parameters:"))

format_date = "%d/%m/%Y %H:%M:%S"
struct = dt.datetime.strptime(string,format_date)

l = []

l = parameters.split(',')

l2 = []

for i in range(len(l)):
    aux = l[i].split('=')
    for i in range (len(aux)):
        l2.append(aux[i])

m = int(l2.index("months")) + 1
d = int(l2.index("days")) + 1
h = int(l2.index("hours")) + 1

m = int(l2[m])
d = int(l2[d])
h = int(l2[h])

result = struct + dateutil.relativedelta.relativedelta(months = m,days = d , hours = h)

print(result.isoformat())