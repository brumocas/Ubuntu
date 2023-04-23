# -*- coding: utf-8 -*-
"""
Created on Sun May 15 15:02:34 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1.csv', sep = ';', index_col ='id', parse_dates= ['date'])

gb = df.groupby('date')['date'].count().sort_index(ascending = True)

print(gb)