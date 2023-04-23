# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:02:49 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('fortune1.csv', sep=';',parse_dates=['Foundation'])
print(df.shape)

def solve():
     i = df.loc[ (df['profit'] < 14000) & ((df['sector'] == 'Technology') | (df['sector'] == 'Retailing')) ].index
     df.drop(i,inplace = True)
     
solve()
print(df.shape)
