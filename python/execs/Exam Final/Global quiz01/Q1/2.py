# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:08:49 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    df1 = df.loc[ df['Total'] > 1030]
    print(df1.iloc[:,4:9])
    return 0

solve()


