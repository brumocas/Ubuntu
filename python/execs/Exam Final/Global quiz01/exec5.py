# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:35:09 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    dfem = df.loc[ (df['Gender'] == 'Female')]
    print(round(dfem['Total'].mean(),1))
    
solve()