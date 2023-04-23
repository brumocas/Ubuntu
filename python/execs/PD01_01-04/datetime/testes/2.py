# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 23:11:53 2022

@author: bruco
"""

import time as t

date = str(input("Date:"))

time_struct = t.strptime(date, '%Y-%m-%d %H:%M:%S')

result = t.strftime('%d/%m/%Y %Hh %Mmin %Ss',time_struct)

print(result)

##2022-03-20 18:45:23