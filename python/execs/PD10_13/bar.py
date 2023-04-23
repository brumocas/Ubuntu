# -*- coding: utf-8 -*-
"""
Created on Sat May 14 11:30:25 2022

@author: bruco
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#defining the seed
np.random.seed(123456) 

df = pd.DataFrame(np.random.rand(1000,4), index = pd.date_range('1/1/2019', periods = 1000, freq = 'D'), columns = ['A','B','C','D'])
print(df.head(3),"\n")

df = df.cumsum()
plt.figure()
df.plot()

##bar from a chart from a determinated row
print(df.iloc[5].plot.bar(),"\n")

##bar charts
df2 = pd.DataFrame(np.random.rand(10,4), columns = list('abcd'), index =(list(range(1,11))))
print(df2.head(3),"\n")
df2.plot.bar()
df2.plot.barh()
df2.plot.bar(stacked = True)
df2.plot.barh(stacked = True)

