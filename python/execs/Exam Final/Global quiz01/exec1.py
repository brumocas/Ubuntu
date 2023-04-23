# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:59:32 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve ():
    print(df.loc[0:2,'Total':'Payment'])
    
solve()