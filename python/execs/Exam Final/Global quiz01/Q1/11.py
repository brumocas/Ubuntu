# -*- coding: utf-8 -*-
"""
Created on Sat May 21 19:10:54 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')


def solve():
    res = (df['Gender'].value_counts()/len(df))*100
    #res = res.reset_index(drop = True)
    print(res)
    return 0

solve()