# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:58:09 2022

@author: bruco
"""

import pandas as pd
import numpy as np
df = pd.read_csv('fortune_ex01_01_01_1.csv', sep=';',parse_dates=['Foundation'])

def solve():
    print(df['revenue'].describe())

solve()