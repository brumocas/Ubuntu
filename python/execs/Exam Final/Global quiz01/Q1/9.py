# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:07:34 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    df.at[2,'Customer type'] = "Member"
    return 0

solve()

print(df.loc[:,'Invoice ID':'Gender'].head(3))