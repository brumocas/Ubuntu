# -*- coding: utf-8 -*-
"""
Created on Sun May 15 10:32:04 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym_q1.csv', sep = ';', index_col ='id', parse_dates= ['date'])

def solve():
    df1 = df.copy()
    ts = pd.to_datetime('1/1/2022')
    df1['years'] =  ((((ts - df1['date']).astype('timedelta64[D]')))/365).round(0).astype(int)
    print(df1.head(3))
    return 0

solve()

