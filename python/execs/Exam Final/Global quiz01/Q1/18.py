# -*- coding: utf-8 -*-
"""
Created on Sun May 22 00:04:27 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    print(df.loc[0:2,'Total':'Payment'])    
    return 0

solve()