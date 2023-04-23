# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:31:41 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    print( df.loc[[0,2],['Invoice ID','Total']] )

solve()