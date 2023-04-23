# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:27:15 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve ():
    Qxprice = (df['Unit price'] * df['Quantity'])
    df.insert(7,'QxPrice',Qxprice)
    return 0

solve()

print(df.loc[0:2,'Unit price':'Total'])