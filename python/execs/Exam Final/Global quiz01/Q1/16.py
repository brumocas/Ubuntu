# -*- coding: utf-8 -*-
"""
Created on Sun May 22 08:01:53 2022

@author: bruco
"""


import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    A = df.pivot_table(index = 'City', columns = 'Customer type' , values = 'Total', aggfunc = 'count')
    A['All'] = A['Member'] + A['Normal']
    B = pd.DataFrame({'Member': A['Member'].sum(), 'Normal':A['Normal'].sum(),'All':A['All'].sum()}, index = ['All'])
    C = pd.concat    ([A,B])
    C.columns.rename('Customer type',inplace = True)
    print(C)
    return 0
solve()