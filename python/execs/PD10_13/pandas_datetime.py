# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:11:51 2022

@author: bruco
"""

import pandas as pd 
import numpy as np 
import datetime 

#generate a datetime /3 different ways
dt = pd.to_datetime(['25/12/2021', np.datetime64('2021-12-25'),datetime.datetime(2021, 12,25)])
print(dt,"\n")

dti = pd.date_range('2021-12-25', periods = 3, freq='H')
print(dti,"\n")

#define date timezone
dti = dti.tz_localize('UTC')
print(dti,"\n")

#convert to another timezone
dti = dti.tz_convert('US/Pacific') #less 8 hours than UTC
print(dti,"\n")

idx = pd.date_range('2021-12-25', periods = 5, freq = 'H')
idx = idx.tz_localize('WET')
print(idx,"\n")

#define a series with datetime
ts = pd.Series(range(len(idx)), index = idx)
print(ts,"\n")

#resample freq
print(ts.resample('2H').mean(),"\n")

friday = pd.Timestamp('2021-12-24')
print(friday,"\n")
print(friday.day_name(),"\n")

saturday = friday + pd.Timedelta('1 day')
print(saturday,"\n")
print(saturday.day_name(),"\n")

monday = friday + pd.offsets.BDay()  
print(monday,"\n")
print(monday.day_name(),"\n")

#create timestamp
ts = pd.to_datetime('25-12-2021 00:00', format = '%d-%m-%Y %H:%M')
print(ts,"\n")

##period frequency of M
a = pd.Period('2021-12')
print(a,"\n ")

##change period frequency of D
a = pd.Period('2021-12', freq='D')
print(a,"\n")

##dateoffset
ts = pd.Timestamp('2021-10-30 16:00:00', tz='Europe/Lisbon')
print(ts,"\n")

##add 1 day 
print(ts + pd.Timedelta(days = 1),"\n")##1 hour less

##using friday 
print(friday,"\n") 
print(ts + pd.DateOffset(days = 1),"\n") ##dont counts daylight saving time

two_business_days = 2 * pd.offsets.BDay()

print(two_business_days.apply(friday)) ## or Friday + two_business_days




