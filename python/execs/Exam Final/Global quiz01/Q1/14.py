# -*- coding: utf-8 -*-
"""
Created on Sat May 21 20:20:36 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve() :
    print(df.loc[[0,2],['Invoice ID','Total']])
    return 0
solve()    