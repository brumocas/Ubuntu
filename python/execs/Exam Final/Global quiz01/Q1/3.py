# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:16:40 2022

@author: bruco
"""

import pandas as pd


df = pd.read_csv('supermarket1.csv', sep=';')

def solve ():
    pt = df.pivot_table (index = 'Product line', columns = 'City', values = 'Total',aggfunc = 'sum')
    city = pt.max().idxmax()
    product = pt[city].idxmax()
    total = round(pt[city].max(),2)
    print(f"{city}, {product}, {total}")
    return 0
solve()