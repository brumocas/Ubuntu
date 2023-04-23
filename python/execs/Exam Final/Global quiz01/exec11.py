# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:00:33 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    print(df['Gender'].value_counts()/len(df)*100)
    
solve()