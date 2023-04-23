# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:56:19 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1_nan.csv', sep = ';', index_col ='id', parse_dates= ['date'])

def solve ():
    m1 = df['age'].mean()
    df1 = df.fillna(0)
    m2 = df1['age'].mean()
    print(round(m1,2))
    print(round(m2,2))
    return 0


solve()