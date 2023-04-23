# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:20:40 2022

@author: bruco
"""
import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    dp = df.pivot_table(index = 'Product line', columns = 'City', values = 'Total', aggfunc = 'sum')
    city = dp.max().idxmax()
    value = round(dp[city].max(),2)
    product = dp[city].idxmax()
    print(f'{city}, {product}, {value}')
    
solve()
