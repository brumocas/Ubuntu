# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:21:20 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('fortune1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    df.sort_values('employees', axis = 0,ascending = False, inplace = True)
    res = df.tail(5)
    print(res.loc[:,['company','employees']])
solve()
