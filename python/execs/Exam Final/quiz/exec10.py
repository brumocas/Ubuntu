# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:08:59 2022

@author: bruco
"""
import pandas as pd
df = pd.read_csv('fortune1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    i = df.loc[ (df['sector'] == 'Energy') | (df['sector'] == 'Aerospace & Defense') | (df['sector'] == 'Media') ].index
    df.drop(i,inplace = True)
    res = round(100*df['sector'].value_counts()/len(df),1)
    print(res)
    
solve()