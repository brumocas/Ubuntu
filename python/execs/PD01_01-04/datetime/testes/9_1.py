# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:23:48 2022

@author: bruco
"""

import datetime

dates = list(map(datetime.date.fromisoformat,input().split(',')))

n = len(dates)

for i in range(n-1):
    for j in range(i+1,n):
        if dates[j].month < dates[i].month or \
            dates[j].month == dates[i].month and dates[j].day < dates[i].day or \
                dates[j].month == dates[i].month and dates[j].day == dates[i].day and dates[j].year < dates[i].year:
            dates[i],dates[j] = dates[j],dates[i]

for date in dates:
    print(date.isoformat())

    
##resposta / teste 
##2022-09-25,2022-05-30,2021-09-25,2020-09-26