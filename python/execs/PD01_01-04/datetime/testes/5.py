# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 23:56:13 2022

@author: bruco
"""

import calendar 

cl = calendar.Calendar()

year = int(input("Year:"))
month = int(input("Month:"))

month_list =list (cl.monthdayscalendar(year,month))

for i in range(len(month_list)):
    if month_list[i][0] == 0 :
        continue;
    else:
        print(month_list[i][0]) #pos = 0 because its monday