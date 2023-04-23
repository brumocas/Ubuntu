# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:03:47 2022

@author: bruco
"""

import pandas as pd 

df = pd.read_csv('gym_q1.csv', sep = ',' ,parse_dates = ['date'])

#average from people that workout 3 < hours < 4 per week 
 
def solve ():
    df34 = df.loc[ (df['hours'] > 2) & (df['hours'] < 5)] 
    res = df34['height'].mean()
    print(f"{res:.2f}")
    
solve()