# -*- coding: utf-8 -*-
"""
Created on Thu May  5 13:41:04 2022

@author: bruco
"""
import numpy as np
import pandas as pd

df = pd.read_csv('gym.csv', sep = ',', parse_dates = ['date'])
##print("\ndf:")
##print(df)

print(df.head(3)) ##by parameter is 5 rows

print(df.tail(3)) ##by parameter is 5

print("\nNumber of rows ans columns =",df.shape)

print("\nInfo of df:")
print(df.info())

print("\nColumns types:")
print(df.dtypes)

print("\nRow with label 0:")
print(df.loc[0]) ##returned a series 
print("\nType =",type(df.loc[0]))

s = df.loc[:,'age']
print("\ncolumn 'age' of df:")
print(s.head())
print("\nType =",type(s))

print("\ndf.loc[0,'age] =",df.loc[0,"age"])

print("\n",df.loc[[0,2,4]])

print("\n",df.loc[[0,2],['name','age']])

print("\n",df.loc[0:2,'name':'age']) ##includes 'age', different than normal slicing

print("\ndf.iloc[1,1]=",df.iloc[1,1])

print("\ndf.iloc[1,:]:")
print(df.iloc[1,:])

print("\ndf.iloc[0:2,2:4]:")
print(df.iloc[0:2,2:4])  #just like slicing 4 and 2 not included

print("\nindex=",df.index)
print("\ncolumns=",df.columns)


df.set_index('name',inplace = True)

print("\nAcccess to a certain name:")
print(df.loc['Jose Carvalho'])


print(df.sort_index(ascending = False ))

print(df.sort_values('age').head()) ## sort by age ascending

df.reset_index(inplace = True) ## reset the index by default





