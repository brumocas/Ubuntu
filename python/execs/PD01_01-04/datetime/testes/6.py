# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 00:05:03 2022

@author: bruco
"""

import time  

Date1 = str(input("Date1:"))
Date2 = str(input("Date2:"))

t1_struct = time.strptime(Date1, '%Y-%m-%d')
t2_struct = time.strptime(Date2, '%Y-%m-%d')

t1 = time.mktime(t1_struct)
t2 = time.mktime(t2_struct)

t3 = t2 - t1

days = float(t3/ (3600*24))

print(f"Number of days between dates={days}")