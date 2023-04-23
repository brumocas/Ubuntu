# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:22:53 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    df1 = df.loc[  (((df['Gender'] == 'Male' )&(df['Customer type'] == 'Member')) | ((df['Gender'] == 'Female' )&(df['Customer type'] == 'Normal'))) & (df['Unit price'] > 99) ] 
    print(df1.loc[:,'Customer type':'Unit price'])
    
solve()

