# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:53:31 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve ():
    df1 = df.pivot_table(index = 'City', columns = 'Payment' , values = 'Total', aggfunc = 'sum')
    print(df1.round(2))
    return 0
solve()