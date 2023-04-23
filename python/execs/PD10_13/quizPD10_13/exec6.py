# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:02:49 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1a.csv', sep = ';', index_col ='id', parse_dates= ['date'])

def solve():
    df['rank'] = pd.cut(df['years'], [0, 5, 10, 15, 100], right=False, labels=['fair','good','very_good','excellent'])
    print(df.head(5))

solve()

