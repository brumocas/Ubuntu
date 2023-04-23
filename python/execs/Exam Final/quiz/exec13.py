# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:29:55 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('fortune1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    dg = df.groupby('state')['revenue'].mean().round(1)
    dg.sort_values(ascending = False, inplace = True)
    print(pd.DataFrame(dg))

solve()
