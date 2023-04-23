# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:21:39 2022

@author: bruco
"""

import numpy as np 
import pandas as pd

print("STATISTICS FROM GYM_CSV\n")

df = pd.read_csv('gym.csv', sep = ',', parse_dates = ['date'])

print("Mean Age=",df['age'].mean())
print("Max Height =",df['height'].max())
print("Min weight =",df['weight'].min())

print("\nSet of statistics:\n",df.describe()) ##just for columns with numerical values 

"""
def avg (col_name): ##function that returns avg of any parameter inserted
    s = 0
    n = len(df[col_name])
    for i in df[col_name]:
        s = s + i
    avg = s/n
    return avg

print(avg('height'))
"""
print("\nNumber of customers in the gym =",df['name'].count())
print("Number of hours that customers workout in the gym =",df['hours'].sum())
print("Median of age of the customers from the gym =",df['age'].median())
print(df['age'].quantile(0.5))

