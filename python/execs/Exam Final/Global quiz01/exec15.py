# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:43:26 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    res = df['Product line'].value_counts()
    res.sort_values(ascending = False, inplace =True)
    print(res)

solve()