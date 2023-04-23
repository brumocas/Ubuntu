# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:03:18 2022

@author: bruco
"""
import pandas as pd 
df = pd.read_csv('gym_q1.csv', sep = ';', index_col ='id', parse_dates= ['date'])
filename = 'gym_rows_q1.csv'


def solve(df,filename):
    df2 = pd.read_csv(filename, sep = ';', index_col ='id', parse_dates= ['date'])
    res = df.append(df2)
    return res


df = solve(df,filename)
print(df.shape)
print(df.tail(3))

