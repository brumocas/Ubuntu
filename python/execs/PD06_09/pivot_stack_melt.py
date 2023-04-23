# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:39:24 2022

@author: bruco
"""

import pandas as pd

##pivot reshapes the dataframe 

df4 = pd.DataFrame({'class':['cycle','cycle','cycle','pilates','pilates','pilates'],
'day':['0-Mon','2-Wed','5-Sat','0-Mon','1-Tue','4-Fri'],
'hour':[12,10,15,9,10,14],'trainer':['Joao','Maria','Joao','Carlos','Cristina','Cristina']})

df_pivot = df4.pivot(index = 'class', columns = 'day', values = 'hour')
print(df_pivot)

print("\n\n")

df_stack = df_pivot.stack() ##columns go down to rows
print(df_stack)

print("\n\n")

df_unstack = df_stack.unstack()
print(df_unstack)

print("\n\n")

df_melt =   df4.melt(id_vars = 'class', value_vars = 'day')
print(df_melt)