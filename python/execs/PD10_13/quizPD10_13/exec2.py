# -*- coding: utf-8 -*-
"""
Created on Sun May 15 09:00:49 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1_nan.csv', sep = ';', index_col ='id', parse_dates= ['date'])

def solve():
    df1 = df.isna()
    aux = 0
    for i in range(df1.shape[0]):
        for j in range(df1.shape[1]):
            if str(df1.iloc[i][j]) == 'True':
                aux = aux + 1
                break
    v1 = df1.shape[0] - aux
    print(f'[{v1}  {aux}]')
    return 0
    
solve()

##other resolution
print(df.isna().any(axis=1).value_counts().to_numpy())
