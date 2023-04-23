# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:54:54 2022

@author: bruco
"""

import numpy as np 
import matplotlib.pyplot as plt

"""importing data"""

xpoints = np.array([0,1,2,3,4,5])
ypoints1 = np.array([5,10,3,11,12,9])
ypoints2 = np.array([2,7,12,1,2,6])

"""Creating bar chart"""

x_index = np.arange(len(xpoints))

plt.bar(x_index - 0.2 , ypoints1, width = 0.4 , label = 'Person 1')

plt.bar(x_index + 0.2 , ypoints2, width = 0.4 , label = 'Person 1')


plt.xlabel('Day')

plt.ylabel('Walking  distance(km)')

font1 = {'family':'serif','color':'blue','size':20}

plt.title('Persons workout',fontdict =  font1)

plt.legend()

##bars in the y axis

"""

x_index = np.arange(len(xpoints))

plt.barh(x_index - 0.2 , ypoints1, height = 0.4 , label = 'Person 1')

plt.barh(x_index + 0.2 , ypoints2, height = 0.4 , label = 'Person 1')

plt.yticks(ticks = x_index,labels = xpoints)

plt.xlabel('Day')

plt.ylabel('Walking  distance(km)')

font1 = {'family':'serif','color':'blue','size':20}

plt.title('Persons workout',fontdict =  font1)

plt.legend()

"""




