# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:53:54 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve ():
    del df['Customer type']

solve()

print(df.loc[:,'Invoice ID':'City'].head(3))