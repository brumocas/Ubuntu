# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:41:43 2022

@author: bruco
"""

import numpy as np 
import pandas as pd

df = pd.read_csv('gym.csv', sep = ',', parse_dates = ['date'])

##insert a column in the df /represents number of years at the gym
df.insert(3,'years',2021 - df['date'].dt.year)

##new column added at the end of df with the days at the gym
df['days'] = df['years']*365
df['old_client'] = df['years'] > 7
print(df.head(3))

##remove the added columns
df.drop('years', axis=1, inplace=True) 
del df['days']
old_client = df.pop('old_client') ##removes and returns de column
print(df.head(3))

##set the columns names 
df.columns = ['ID','Name','Date','Height','Weight','Age','Hours','Status','Children','Sex']
print(df.head(3))

##replace columns name
df.columns = df.columns.str.replace('Sex','Gender')
df.rename(columns = {'ID':'id','Name':'name',}, inplace = True)
print(df.head(3))

##change the column names using list comprehension
df.columns = [x.lower() for x in df.columns]
print(df.head(3))

##assinig a new set of values
df.loc[0] = [1354891,'Antonio Costa','2018-05-20',100,20,30,2,'widow',1,'M']
print(df.head(3))

##assinig just some of the values
df.loc[0,['id','status']] = [1234567,'single']
print(df.head(3))

##append a row to  a df
df = df.append({'name':'Xavier Furtado','id':1111111,'height':150},ignore_index=True)
print(df.tail(3))

##delete the row
df.drop(60,inplace = True)
print(df.tail(3))

##select the costumers over 55 y 
over_55 = df.loc[df['age'] > 55]
print(over_55)

##select the costumers over 55 y and weiht over 50
over_55_weight_50 = df.loc[(df['age'] > 55) & (df['weight'] > 50)]
print(over_55_weight_50)

##select the costumers over 55 or under 24. View name and age
over55_24 = df.loc[ (df['age'] > 55) | (df['age'] <24),['name','age']]
print(over55_24)

##select the costumer divorced or widow
div_wid = df.loc[ (df['status'] == 'widow') | (df['status'] == 'divorced')]
print(div_wid)

##select costumer with name Freitas
Freitas = df.loc[df['name'].str.contains('Freitas',na = False)]
print(Freitas)

##aply a function to all the elements of a series
df['status'] = df['status'].apply(str.upper) ##str.lower to lowercase letter 
print(df.head(3))

##Get the unique elementes
unique = df['status'].unique()
print(unique)
unique_count = df['status'].value_counts()
print(unique_count)













