# -*- coding: utf-8 -*-
"""
Created on Sun May 15 12:45:20 2022

@author: bruco
"""


import pandas as pd 
df = pd.read_csv('gym2_q1.csv', sep = ';', index_col ='id', parse_dates= ['date'])

def solve(col_name,col_dtype): 
    df[col_name] = df[col_name].astype(col_dtype)
    print(df.dtypes)
    return 0
 
solve('height',float)