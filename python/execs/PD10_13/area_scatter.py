# -*- coding: utf-8 -*-
"""
Created on Sat May 14 11:57:41 2022

@author: bruco
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#defining the seed
np.random.seed(123456) 

df = pd.DataFrame(np.random.rand(10,4), columns = list('abcd'))
print(df.head(3),"\n")
df.plot.area()

df1 = pd.DataFrame(np.random.rand(50,4), columns = list('abcd'))
print(df1.head(3),"\n")
df1.plot.scatter(x='a', y = 'b')

