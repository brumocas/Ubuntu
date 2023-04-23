# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:38:34 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('fortune1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    df1 = df.pivot_table(index = 'sector', columns = 'state', values = 'profit' , aggfunc = 'sum')
    state = df1.min().idxmin()
    value = df1[state].min()
    sector = df1[state].idxmin()
    print(f'{sector}, {state}, {value}')
    
solve()