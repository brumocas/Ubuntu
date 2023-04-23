# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:30:25 2022

@author: bruco
"""

import pandas as pd 

df = pd.read_csv('gym_q1.csv', sep = ',' ,parse_dates = ['date'])

#sum of children whose parents above over 55 years old 

def solve ():
    dfm = df.loc[ (df['age'] > 55 )]
    res = dfm['children'].sum()
    print(f"{res:.0f}")
    
solve()