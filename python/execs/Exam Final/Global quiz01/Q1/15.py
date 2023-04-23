# -*- coding: utf-8 -*-
"""
Created on Sat May 21 20:41:51 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    db = df.groupby('Product line')['Quantity'].sum()   
    A = pd.DataFrame(db)
    B = pd.DataFrame({'Quantity':A['Quantity'].sum()} , index =['All'])
    C = A.append(B) ## C = pd.concat([A,B])
    C.index.rename('Product line', inplace = True)
    print(C)
    return 0

solve()

