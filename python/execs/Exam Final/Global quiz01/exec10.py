# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:58:07 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    res = df.loc[ df['Total'] > 1030]
    print(res.loc[:,'Product line':'Total'])

solve()