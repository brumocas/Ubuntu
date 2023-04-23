# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:26:12 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    df['Total'] = pd.cut(df['Total'], [0,220,440,660,880,1100], right = False, labels = ['low','fair','good','very_good','excellent'])
    print(df['Total'].value_counts())
solve()