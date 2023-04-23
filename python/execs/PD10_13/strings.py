# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:41:48 2022

@author: bruco
"""
import pandas as pd 
import numpy as np

s1 = pd.Series(['a','b','c'],)
print(s1,"\n")

s2 = pd.Series(['a','b','c'], dtype ="string")
print(s2,"\n")

s3 = pd.Series(['a_b_c','d_e_f','g_h_i'], dtype ='string')
print(s3,"\n")

#change series letters to uppercase
print(s3.str.upper(),"\n")

##concatenate all series strings in a string
print(s3.str.cat(sep = ','),"\n") 

#split series by '_' , its returned a list
sl =s3.str.split('_')
print(sl ,"\n")

#access series strings in column 1 
print(sl.str[1],"\n") 

#series transformed in pandas DataFrame separated by '_'
print(s3.str.split('_',expand = True),"\n") 

#slicing can be used to access a certain value
print(s3.str[2:],"\n")

#check if the series has a determinated string
print(s2.str.contains('a'),"\n") 

#counnt certain caracter in the series
print(s2.str.count('a'),"\n")
print(s3.str.count('_'),"\n")

#size of each string from the series
print(s2.str.len())
print(s3.str.len())
