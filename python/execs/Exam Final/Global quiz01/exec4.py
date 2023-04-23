# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:33:36 2022

@author: bruco
"""
import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    print(round(df['Total'].describe(),2))

solve()
