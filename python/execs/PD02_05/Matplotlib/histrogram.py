# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:30:46 2022

@author: bruco
"""

import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('gym.csv',delimiter = ',')

bins = [20,25,30,35,40,45,50,55,60]

ages = data['idade']

plt.hist(ages,bins=bins,edgecolor='black')

plt.xlabel('Age')

plt.ylabel('Number of persons')

plt.title('Ages distribution')