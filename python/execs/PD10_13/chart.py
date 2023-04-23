# -*- coding: utf-8 -*-
"""
Created on Sat May 14 09:40:27 2022

@author: bruco
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#defining the seed
np.random.seed(123456) 

#generating 1000 random values from normal distributuion
ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2019', periods = 1000, freq = 'D'))
print(ts.head(3),"\n")

ts = ts.cumsum()
ts.plot();

df = pd.DataFrame(np.random.randn(1000,4), index = ts.index, columns = ['A','B','C','D'])
print(df.head(3),"\n")

df = df.cumsum()
plt.figure()
df.plot()

df3 = (pd.DataFrame(np.random.randn(1000,2), columns = list('BC')).cumsum())
df3['A'] = pd.Series(list(range(len(df3))))
print(df3.head(3),"\n")

##plot by choosing columns in axis
df3.plot(x='A',y='B')

