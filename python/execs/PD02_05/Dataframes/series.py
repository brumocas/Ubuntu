# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:04:26 2022

@author: bruco
"""
import pandas as pd 
import numpy as np 


s1 = pd.Series(['Antonio','Joana','Carlos','Barbara'])
print("s1:")
print(s1)
print("s1 index:",s1.index) 

s2 = pd.Series(np.random.randn(4),index=['a','b','c','d'])
print("\ns2:")
print(s2)
print("s2 index:",s2.index)

s3 = pd.Series({'b':20,'a':30,'c':15})
print("\ns3:")
print(s3)
print("s3 index:",s3.index)

d = {'a':10,'b':20,'c':30}
s4 = pd.Series(d,index=['b','c','d','a'])
print("\ns4:")
print(s4)
print("s4 index:",s4.index)


s5 = pd.Series(5,index = ['a','b','c'])
print("\ns5:")
print(s5)
print("s5 index:",s5.index)

print("\ns2[0] =",s2[0])

print("\ns2[:3]:")
print(s2[:3])

print("\ns2 mean =",s2.mean())

print("\n[s2 > s2.mean()]:")
print(s2[s2 > s2.mean()])

print("\ns2 exponencial values:")
print(np.exp(s2))

print("\ns2.dtype =",s2.dtype)

print("\ns2 converted for an pandas array:")
print(s2.array)


print("\ns2 converted for an numpy array:")
print(s2.to_numpy())

print("\ns2['a'] =",s2['a'])

print("\n",s2['b'] == 20 )

print("\n","c" in s2)

print("\ns2[1:] + s2[:-1]:")
print(s2[1:] + s2[:-1])


s6 = pd.Series(np.random.randn(4), name = 'something')
print("\ns6")
print(s6)
s6.rename("different", inplace = True)
print("\ns6 renamed:")
print(s6)
print("\ns6 name =",s6.name)