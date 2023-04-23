# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:10:33 2022

@author: bruco
"""

import pandas as pd 
import numpy as np

df = pd.read_csv('gym2.csv', sep = ',')
print(df.head(3))

pivot_table = round(df.pivot_table(index='city', columns='status', values='age', aggfunc='mean'),2)
print('\n')
print(pivot_table)


##2rows
pivot_table_rows = round(df.pivot_table(index=['city','sex'], columns='status', values='age', aggfunc='mean'),2)
print('\n')
print(pivot_table_rows)

##2columns
pivot_table_columns= round(df.pivot_table(index='city', columns=['status','sex'], values='age', aggfunc='mean'),2)
print('\n')
print(pivot_table_columns)

##2values
pivot_table_values = round(df.pivot_table(index='city', columns='status', values=['age','height'], aggfunc='mean'),2)
print('\n')
print(pivot_table_values)

##2aggfunc
pivot_table_values = round(df.pivot_table(index='city', columns='status', values='age', aggfunc=['mean','max']),2)
print('\n')
print(pivot_table_values)
