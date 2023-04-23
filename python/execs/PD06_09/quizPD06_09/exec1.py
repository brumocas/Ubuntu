# -*- coding: utf-8 -*-
"""
Created on Sun May  8 09:03:28 2022

@author: bruco

"""
import pandas as pd 

df = pd.read_csv('gym2_q1.csv', sep = ';', index_col ='id', parse_dates = ['date'])


def solve():
    df['month'] = df['date'].dt.month
    df.rename(columns = {'name':'clients'}, inplace = True)  
    df_groupby = df.groupby('month')[['clients']].count()
    print(df_groupby)      

solve() 

""" ##Sol from prof

def solve():
    df['month'] = df['date'].apply(lambda x: x.month)
    df1=df.groupby('month')[['name']].count()
    df1.rename(columns={'name':'clients'},inplace=True)
    print(df1)

solve()
"""