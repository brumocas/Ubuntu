# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:44:35 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('fortune_ex01_01_01_1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    df1 = df.loc[ df['revenue'] > 180000]
    print(df1.loc[:,['company','revenue']])
    
solve()