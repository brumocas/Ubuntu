# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:05:27 2022

@author: bruco
"""

import pandas as pd
import numpy as np 

##generated numbers from a normal distribution
df = pd.DataFrame(np.random.randn(3,2), index = ['a','c','e'], columns = ['one','two'])
df['three'] = 'bar'
df['four'] = df['one'] > 0 
print(df,"\n")

df2 = df.reindex(['a','b','c','d','e'])
print(df2,"\n")

##check if is empty cell
print(df2['one'].isna(),"\n")
##check if is a not empty cell
print(df2['three'].notna(),"\n")

print(df2.isna(),"\n")##check empty

print(df2.notna(),"\n")##check fullfield


df3 = df.copy()
df3['timestamp'] = pd.Timestamp('2022/03/02') 
df3.loc['c','timestamp'] = np.nan
print(df3,"\n")
##count number of datetypes in df3 by columns
print(df3.dtypes.value_counts())

##replace missind data
df4 = df2.copy()
df4[['one','two']] = df4[['one','two']].fillna(0)
print(df4,"\n")

df4['three'] = df4['three'].fillna('bar')
print(df4,"\n")

df4['four'] = df4['four'].fillna('False')
print(df4,"\n")

print("NaN values fully replaced\n")



