# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:32:29 2022

@author: bruco
"""


import pandas as pd 

df = pd.read_csv('gym_q1.csv', sep = ',' ,parse_dates = ['date'])

#age standart deviation

def solve ():
    dfm = df['age'].std()
    print(f"{dfm:.2f}")
    
solve()