# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:37:40 2022

@author: bruco
"""
"""
2022-02-18 10:00:00
Europe/Lisbon 

2022-02-21 08:00:00
US/Pacific
"""

import dateutil 
import datetime as dt

format_time = "%Y-%m-%d %H:%M:%S"

date1= str(input("Date1:"))
t1 = str(input("Timezone1:"))
date2 = str(input("Date2:"))
t2 = str(input("Timezone2:"))

d1 = dt.datetime.strptime(date1,format_time)
d2 = dt.datetime.strptime(date2,format_time)

d1.astimezone(dateutil.tz.gettz(t1))
d2.astimezone(dateutil.tz.gettz(t2))

d3 = 

