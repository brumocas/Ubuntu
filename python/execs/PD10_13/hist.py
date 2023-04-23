# -*- coding: utf-8 -*-
"""
Created on Sat May 14 11:49:11 2022

@author: bruco
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#defining the seed
np.random.seed(123456) 

df = pd.DataFrame({'a':np.random.rand(1000)+1, 'b':np.random.rand(1000), 'c':np.random.rand(1000)-1}, columns = list('abc'))
print(df.head(3),"\n")
df.plot.hist(alpha = 0.5)

df1 = pd.DataFrame(np.random.rand(10,5), columns = list('ABCDE'))
print(df1.head(3),"\n")
df1.plot.box()  


 