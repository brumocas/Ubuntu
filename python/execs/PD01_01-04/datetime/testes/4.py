# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 23:55:09 2022

@author: bruco
"""


import datetime
import dateutil
##from dateutil import tz
n = int(input('Number of dates:'))
dates = []
for i in range(n):
    sdate, timezone = input().split(',')
    timezone = timezone.strip()
    date = datetime.datetime.fromisoformat(sdate)
    date = datetime.datetime(date.year,date.month,date.day,date.hour,date.minute,date.second,0,dateutil.tz.gettz(timezone))
    dates.append(date)
dates.sort()
for date in dates:
    print(f'{date}, {date.tzname()}')

