# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:31:34 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')


def solve():
    A = df.pivot_table( index = 'City', columns = 'Customer type', values = 'Total', aggfunc = 'count',margins = True)
    ##A['ALL'] = A['Member'] + A['Normal'] 
    print(A)
    ## = pd.DataFrame( {'Member':A['Member'].sum(), 'Normal':A['Normal'].sum(),'ALL':A['ALL'].sum()}, index = ['ALL'] )
    ##C = A.append(B)
    ##C.columns.rename('City', inplace = True)
    ##print(C)
solve()