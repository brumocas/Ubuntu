# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:07:32 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    res = df['Total'].describe()
    print(res.round(2))
    return 0 
solve()