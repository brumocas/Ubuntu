# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:01:04 2022

@author: bruco
"""

import datetime as dt 
import time

string = str(input())

l = []

l = string.split(',')

dates = []
new_dates = []

for i in range (len(l)):
    dates.append(time.strptime(l[i],"%Y-%m-%d"))

for i in range(len(dates)):
    new_dates.append(time.strftime("%m-%d-%Y",dates[i]))

dates.sort()

for i in range(len(dates)):
    print(new_dates[i])

    
##resposta / teste 
##2022-09-25,2022-05-30,2021-09-25,2020-09-26