# -*- coding: utf-8 -*-
"""
Created on Sun May 15 15:01:45 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1.csv', sep = ';', index_col ='id', parse_dates= ['date'])

def solve():
    