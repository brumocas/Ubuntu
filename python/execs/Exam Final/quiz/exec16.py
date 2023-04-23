# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:44:50 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('fortune1.csv', sep=';',parse_dates=['Foundation'])


def solve():
    res = pd.cut(df['employees'], [1000,10000,50000,100000,1000000,3000000],False,['small','small_medium','medium','medium_large','large'])
    print(res.value_counts())
solve()
