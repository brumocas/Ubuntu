# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 23:19:38 2022

@author: bruco
"""

import time

time1 = int(input("Number of seconds since the epoch of the first date:"))
time2 = int(input("Number of seconds since the epoch of the second date:"))

t1 = time.gmtime(time1)
t2 = time.gmtime(time2)

time3 = time2 - time1

t3=time.gmtime(time3)

str1=time.strftime("%Y/%m/%d",t1)
str2=time.strftime("%Y/%m/%d",t2)

print("Number of years between",str1,"and",str2,"=",t3.tm_year-1970)

##1579219200
##1645056000