# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:55:24 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    res = df.pivot_table( index = 'City', columns = 'Payment', values = 'Total', aggfunc = 'sum',margins = False)
    print(res.round(2))

solve()