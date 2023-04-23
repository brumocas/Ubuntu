# -*- coding: utf-8 -*-
"""
Created on Sun May 15 08:36:37 2022

@author: bruco
"""
import pandas as pd 
df = pd.read_csv('gym2_q1_nan.csv', sep = ';', index_col ='id', parse_dates= ['date'])

def solve():
    print(df.shape)
    df.dropna(how = 'all',inplace = True) #delete nan in fully rows
    print(df.shape)
    return 0
solve()

