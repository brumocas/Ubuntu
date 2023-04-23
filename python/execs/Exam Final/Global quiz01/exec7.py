# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:52:13 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve ():
    i = df.loc[ (df['City'] == 'Yangon')].index
    df.drop(i,inplace = True)

solve()
print(df.loc[:,'Invoice ID':'Product line'].head(3))