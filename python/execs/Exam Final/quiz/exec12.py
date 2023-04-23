# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:25:54 2022

@author: bruco
"""

import pandas as pd
import datetime
df = pd.read_csv('fortune1.csv', sep=';',parse_dates=['Foundation'])


def solve():
    df1 = df.copy()
    df1.index = df['company']
    comp = df1['Foundation'].idxmax()
    date = df['Foundation'].max()

    d = pd.Timestamp("2022-1-1")
    days = (d-date).days
    print(f"Number of days since the foundation = {days}")
    print(f"Company: {comp}")

solve()