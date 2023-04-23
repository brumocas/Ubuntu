# -*- coding: utf-8 -*-
"""
Created on Sun May 22 00:10:03 2022

@author: bruco
"""


import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    df.columns = df.columns.str.replace(' ','_',regex=True)  
    return 0

solve()
print(df.loc[:,['Invoice_ID','Customer_type','Product_line','Unit_price','Tax_5%']].head(3))
