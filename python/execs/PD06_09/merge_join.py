# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:05:54 2022

@author: bruco
"""
import pandas as pd 
import numpy as np
import datetime as dt 

df1 = pd.read_csv('gym_1.csv',sep = ',', index_col ='id', parse_dates = ['date'])

df3 = pd.read_csv('gym_3.csv',sep = ',', index_col ='id')

df_merge_left = pd.merge(df1,df3,how = 'left', on='id') ##uses the left key

df_merge_right = pd.merge(df1,df3,how = 'right', on='id') ##uses the left key

df_merge_outer = pd.merge(df1,df3,how = 'outer', on='id')  ##uses 2 keys  

df_merge_inner = pd.merge(df1,df3,how = 'inner', on='id') ##keeps the common from both 

result = pd.merge(df1,df3, how = 'cross')

##join similar to merge but simple 

df_join_left = df1.join(df3, lsuffix = 'df1') ## same as df_merge_left

df_join_right = df1.join(df3, how ='right', lsuffix = 'df1') ## same as df_merge_right

df_join_inner = df1.join(df3, how = 'inner', lsuffix = 'df1') ## same as df_merge_inner

df_join_outer = df1.join(df3, how = 'outer', lsuffix = 'df1') ## same as df_merge_inner



    