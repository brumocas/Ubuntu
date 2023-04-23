# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:17:45 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    d = df.loc[df['City'] == 'Yangon'].index
    df.drop(d,inplace = True)
    return 0
solve()
print(df.loc[:,'Invoice ID':'Product line'].head(3))