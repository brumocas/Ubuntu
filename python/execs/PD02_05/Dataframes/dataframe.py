# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:43:05 2022

@author: bruco
"""

import numpy as np
import pandas as pd

##dataframe based on dict

d = { 'one' : pd.Series([1.0,2.0,3.0], index = ['a','b','c']),
     'two' :pd.Series([1.0,2.0,3.0,4.0], index = ['a','b','c','d'])}

print("\ndict d:")
print(d)

df1 = pd.DataFrame(d)
print("\ndf1:")
print(df1)     
print("\ndf1 index =",df1.index)
print("\ndf1 columns =",df1.columns)

print("\nOveride index dataframe from original dict:")
print(pd.DataFrame(d , index = ['d','b','a'] , columns = ['two','three'] ))

f = {'one':[1.0,2.0,3.0,4.0],'two':[4.0,3.0,2.0,1.0]}

df2 = pd.DataFrame(f)

print("\ndf2(default index):")
print(df2)

print("\ndf2 ")
print(pd.DataFrame(f, index = ['a','b','c','d']))
