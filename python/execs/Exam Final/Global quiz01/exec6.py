# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:39:06 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')


def solve():
    pt = df.pivot_table( index = 'Product line', values = 'Quantity', aggfunc = 'sum', margins = True)
    print(pt)

"""
def solve():
    dg = df.groupby('Product line')['Quantity'].sum()
    A  = pd.DataFrame(dg)
    B = pd.DataFrame({'Quantity':A['Quantity'].sum()},index = ['All'])
    C = A.append(B)
    C.index.rename('Product line', inplace = True)
    print(C)  
"""
    
solve()