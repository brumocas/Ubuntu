# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:25:47 2022

@author: bruco
"""

import numpy as np 
import matplotlib.pyplot as plt

xpoints = np.array([0,1,2,3,4,5])
ypoints1 = np.array([5,10,3,11,12,9])
ypoints2 = np.array([2,7,12,1,2,6])

plt.plot(xpoints,ypoints1,ypoints2)

plt.grid()

plt.xlabel('Day')

plt.ylabel('Walking  distance(km)')

