# -*- coding: utf-8 -*-
"""
Created on Sun May 15 10:27:37 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1.csv', sep = ';', index_col ='id', parse_dates= ['date'])

def solve():
    df['city'] = df['city'].str.upper()
    print(df.head(3))
    return 0
solve()
