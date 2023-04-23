# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:42:49 2022

@author: bruco
"""

import pandas as pd 
import numpy as np

df = pd.read_csv('gym2.csv', sep = ',')
print(df.head(3))

df_groupby = df.groupby('class')['name'].count() ##number of participants in each class
print('\n')
print(df_groupby)

df_groupby_1 = df.groupby(['city','class'])['name'].count() ##number of participants in each class
print('\n')
print(df_groupby_1)

df_groupby_2 = df.groupby('class')['name'].count() ##number of participants in each class
print('\n')
print(df_groupby_2)

df_groupby_3 = df.groupby('class')['age'].agg(['mean','max'])  ##number of participants in each class
print('\n')
print(df_groupby_3) 