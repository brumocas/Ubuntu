# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:38:27 2022

@author: bruco
"""
import pandas as pd 
df = pd.read_csv('gym2_q1_nan.csv', sep = ';', index_col ='id', parse_dates= ['date'])
print(df.shape)
df.dropna(axis = 0 , inplace = True) #delete all nan 
print(df.shape)
