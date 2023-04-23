# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:33:17 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('fortune1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    df1 = df.loc[ ((df['state'] == 'IL') | (df['state'] == 'WA') | (df['state'] == 'NY')) & ((df['sector'] == 'Retailing') | (df['sector'] == 'Industrials') | (df['sector'] == 'Technology')) ]
    res = df1.pivot_table(index = 'state', columns = 'sector', values = 'profit', aggfunc = 'max').round(1)
    print(res)
    
solve() 