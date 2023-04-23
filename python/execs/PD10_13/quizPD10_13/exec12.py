# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:49:46 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1.csv', sep = ';', index_col ='id', parse_dates= ['date'])

def solve():
    gb = df.groupby('rank')['rank'].count().sort_values(ascending = False)
    print(gb)
    return 0

solve()
