# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:48:23 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    df1 =df.loc[df['Gender'] == 'Female']
    res = df1['Total'].mean()
    print(round(res,1))
    return 0

solve()