# -*- coding: utf-8 -*-
"""
Created on Sat May 21 14:19:32 2022

@author: bruco
"""

import calendar 

d = int(input('Day of the week (0-6):'))

calendar.setfirstweekday(d)
res = calendar.firstweekday()

print('First day of the week:',calendar.day_name[res])