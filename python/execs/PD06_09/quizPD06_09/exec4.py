# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:11:17 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1.csv', sep =';', index_col = 'id', parse_dates= ['date'])


def solve():
    df_pilates = df.loc[ df['class'] == 'pilates']
    pos = df_pilates['hours'].max()
    beast = df_pilates.loc[ df['hours'] == pos]
    print(beast.iloc[0,0])

"""
def solve():
    pt=df.pivot_table(index='name',columns = 'class', values='hours', aggfunc='sum')
    print(pt[pt['pilates'] == pt['pilates'].max()].index[0])  
"""
    
solve()
