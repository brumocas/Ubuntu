# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 19:53:22 2022

@author: bruco
"""

import calendar 

year = int(input("Year:"))
month = int (input("Month:"))
day = int(input("Day:"))

idx = calendar.weekday(year, month, day)

print(calendar.day_name[idx])