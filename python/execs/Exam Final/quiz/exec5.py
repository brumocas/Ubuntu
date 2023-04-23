# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:55:48 2022

@author: bruco
"""

import pandas as pd
import numpy as np
df = pd.read_csv('fortune_ex01_01_01_1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    del df['rank']
    del df['revenue']
    del df['profit']
    del df['employees']
    del df['sector']

solve()

print(df.head(3))