# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:49:34 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('fortune1.csv', sep=';',parse_dates=['Foundation'])


def solve():
    res = df.loc[ (((df['sector'] == 'Technology') & (df['state'] == 'CA')) | ((df['sector'] == 'Health Care') & (df['state'] == 'WA'))) & (df['profit'] > 10000) ]
    print(res.loc[:,'company':'sector'])

solve()

