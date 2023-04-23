# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:50:02 2022

@author: bruco
"""

import pandas as pd
import numpy as np
df = pd.read_csv('fortune_ex01_01_01_1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    df.dropna(how = 'all', inplace = True)
    df.loc[ (df['prev_rank'] == '') | (df['prev_rank'] == ' ') ] = 0
    df['prev_rank'] = df['prev_rank'].astype('int64')
    
solve()
print(df[df['prev_rank']==0]['prev_rank'].count())
print(df['prev_rank'].dtype)