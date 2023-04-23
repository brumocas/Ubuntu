# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:23:01 2022

@author: bruco
"""

import pandas as pd 

df = pd.read_csv('gym_q1.csv', sep = ',' ,parse_dates = ['date'])

#average height from married people

def solve ():
    dfm = df.loc[ (df['status'] == 'married')]
    res = dfm['height'].count()
    print(f"{res:.0f}")
    
solve()