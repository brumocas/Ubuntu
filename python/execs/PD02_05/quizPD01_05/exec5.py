# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:35:19 2022

@author: bruco
"""

import pandas as pd 

df = pd.read_csv('gym_q1.csv', sep = ',' ,parse_dates = ['date'])

# children value_counts sorted by ascending order 

def solve ():
    s = df['children'].value_counts()
    s = s.sort_index()
    print(s)
    
solve()