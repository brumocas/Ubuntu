# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:40:03 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('fortune_ex01_01_01_1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    print(df.loc[[0,2,4],'company':'revenue'])
solve()