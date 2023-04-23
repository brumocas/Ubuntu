# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:50:38 2022

@author: bruco
"""

import pandas as pd
df = pd.read_csv('supermarket1.csv', sep=';')

def solve():
    df.columns = df.columns.str.replace(' ','_', regex = True)    
    
solve()
print(df.loc[:,['Invoice_ID','Customer_type','Product_line','Unit_price','Tax_5%']].head(3))