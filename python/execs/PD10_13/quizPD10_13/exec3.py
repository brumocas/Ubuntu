# -*- coding: utf-8 -*-
"""
Created on Sun May 15 10:00:28 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1.csv', sep = ';', index_col ='id', parse_dates= ['date'])

def solve(string):
    df1 = df['name'].str.count(string).sum()
    print(f'Number of ocurrences of {string} :',df1)
    return 0

solve('Martins')
