# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:11:18 2022

@author: bruco
"""

"""importing data"""

import numpy as np 
import matplotlib.pyplot as plt

xpoints = np.array([0,1,2,3,4,5])
ypoints = np.array([5,10,3,11,12,9])

"""creating pie chart"""

explode = [0,0,0,0,0.1,0]

plt.pie(ypoints,labels=xpoints,explode=explode,autopct='%1.1f%%')

plt.title('Person 1 workout by day')

