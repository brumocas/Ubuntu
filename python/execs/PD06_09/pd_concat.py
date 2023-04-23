# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:54:05 2022

@author: bruco
"""

import pandas as pd 

df1 = pd.read_csv('gym_1.csv', sep = ',' ,index_col = 'id', parse_dates = ['date'])
print("\n",df1)
df2 = pd.read_csv('gym_2.csv', sep = ',' ,index_col = 'id', parse_dates = ['date'])
print("\n",df2)
df3 = pd.read_csv('gym_3.csv', sep = ',' , index_col = 'id')
print("\n",df3)


df_concat = pd.concat([df1,df2,df3])

df_concat_cols_outer = pd.concat([df1,df3], axis = 1 , join = 'outer')

df_concat_cols_inner = pd.concat([df1,df3], axis = 1 , join = 'inner' )


result = df1.append([df2,df3])


