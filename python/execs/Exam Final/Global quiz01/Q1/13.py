# -*- coding: utf-8 -*-
"""
Created on Sat May 21 19:49:13 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    p = df['Product line'].value_counts()
    ##p = p.sort_values(ascending = True)
    print(p)
    return 0

solve()