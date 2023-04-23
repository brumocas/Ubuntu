# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:35:08 2022

@author: bruco
"""

import numpy as np 
import matplotlib.pyplot as plt

xpoints = np.array([0,1,2,3,4,5])
ypoints1 = np.array([5,10,3,11,12,9])

"""small dots/interrupted line /black """ 
#plt.plot(xpoints,ypoints1,'.--k')  

"""dots/straight line /red """
#plt.plot(xpoints,ypoints1,'o-r') 

plt.plot(xpoints,ypoints1,color='green',marker='o',linestyle='dashed',linewidth=2,markersize=12)



