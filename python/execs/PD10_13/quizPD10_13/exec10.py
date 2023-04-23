# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:27:08 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1.csv', sep = ';', index_col ='id', parse_dates= ['date'])


def solve(name):
    df.reset_index(inplace = True)
    df1 =df.set_index('name')

    ts = pd.to_datetime('1/1/2022')
    tn =  df1.loc[name]['date']
    d =  ts -tn
    print(f'{d.days} days')
    
solve('Marisa Martins')