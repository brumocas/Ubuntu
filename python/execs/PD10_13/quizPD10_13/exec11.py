# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:06:27 2022

@author: bruco
"""
import pandas as pd 

def solve(datestr,timezone):
    dti = pd.to_datetime(datestr)
    dti = dti.tz_localize('UTC')
    dto = dti.tz_convert(timezone)
    return dto

print(solve('2022-01-25 16:30:45','US/Pacific'))