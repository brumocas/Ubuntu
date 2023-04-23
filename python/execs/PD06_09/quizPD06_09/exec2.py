# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:50:38 2022

@author: bruco
"""

import pandas as pd 
df = pd.read_csv('gym2_q1.csv', sep =';', index_col = 'id', parse_dates= ['date'])

def solve():
    pt=df.pivot_table(index='class', columns='city', values='name', aggfunc='count')
    df1=pd.DataFrame(pt.max(), columns=['clients'])
    df2=pd.DataFrame(pt.idxmax(axis=0), columns=['class'])
    df3 = pd.concat([df2,df1],axis=1)
    print(df3)

solve()
