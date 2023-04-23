# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:25:31 2022

@author: bruco
"""

import pandas as pd
import numpy as np

# dtype = "category" , helps to save memory
s = pd.Series(['a','b','c','a'], dtype = 'category')
print(s,"\n")

df = pd.DataFrame({'A':['a','b','c','a']})
print(df,"\n")

##add a categorical column equal to the object
df['B'] = df['A'].astype('category')
print(df,"\n")
print(df.dtypes,"\n") ##check Df dtypes

df1 = pd.DataFrame({'value':np.random.randint(0,100,20)})
labels = [f'{i} - {i+9}' for i in range (0,100,10)]
df1['group'] = pd.cut(df1['value'], range(0,105,10), right = False , labels = labels )
print(df1,"\n") 

##count group values
print(df1['group'].value_counts().sort_index(),"\n")

##create a categorical object 
raw_cat = pd.Categorical(['a','b','c','d'] , categories = ['b','c','d'])
print(raw_cat,"\n") 

##covert to Series 
s = pd.Series(raw_cat)
print(s,"\n")