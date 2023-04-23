# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:53:08 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    df.at[2,'Customer type'] = 'Member'

solve()

print(df.loc[:,'Invoice ID':'Gender'].head(3))