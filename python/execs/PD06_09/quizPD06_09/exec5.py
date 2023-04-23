# -*- coding: utf-8 -*-
"""
Created on Sun May  8 17:44:37 2022

@author: bruco
"""

import pandas as pd 

df = pd.read_csv('gym2_q1.csv', sep = ';', index_col ='id', parse_dates = ['date'])

def solve():
    df.set_index('rank', inplace=True)
    df1 = df.groupby('rank')['age'].mean().round(2)
    df2 = df.groupby('rank')['age'].std().round(2)
    df3 = pd.concat([df1,df2],axis=1)
    df3.columns = ['mean','std']
    print(df3)
solve()
