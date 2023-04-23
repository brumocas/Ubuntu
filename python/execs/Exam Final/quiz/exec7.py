# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:59:51 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('fortune1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    column = (df['profit']/df['revenue']*100).round(2)
    df.insert(4,'profit_margin',column)

solve()

print(df.loc[0:2,'company':'sector'])