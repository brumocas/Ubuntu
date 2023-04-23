# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:52:28 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1.csv', sep = ';', index_col ='id', parse_dates= ['date'])


def solve (old_cat,new_cat) :
    df['rank'] = df['rank'].replace(old_cat,new_cat,regex=True)
    df['rank'] = df['rank'].astype('category')
    return 0;

solve('fair', 'poor')
print(pd.unique(df['rank']))
