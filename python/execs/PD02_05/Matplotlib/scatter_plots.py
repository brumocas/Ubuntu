# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:42:17 2022

@author: bruco
"""

import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('gym.csv',delimiter = ',')

ages = data['idade']
children = data['filhos']
colors = data['horas']
sizes= data['altura']

plt.scatter(ages, children,s = sizes , c = colors , cmap ='Blues' , edgecolor = 'black')
cbar=plt.colorbar()
cbar.set_label('Hours')

plt.xlabel('age')
plt.ylabel('number of children')
plt.title('age / number of children')

 

