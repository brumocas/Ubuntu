# -*- coding: utf-8 -*-
"""
Created on Sat May 21 19:27:31 2022

@author: bruco
"""


import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    df['Total'] = pd.cut(df['Total'], [0, 220,440,660,880,1100], right=False, labels=['low','fair','good','very_good','excellent'])
    res = df['Total'].value_counts()
    ##res = res.reset_index(drop = True)
    print(res)
    return 0

solve()