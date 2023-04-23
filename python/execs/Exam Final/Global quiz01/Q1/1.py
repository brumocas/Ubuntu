# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:02:22 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    del df['Customer type']
    return 0
    
solve()
print(df.loc[:,'Invoice ID':'City'].head(3))