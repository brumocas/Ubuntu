# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:32:14 2022

@author: bruco
"""

import numpy as np 

a = np.array([[1,2,3],[4,5,6],[7,8,9]])


b = np.array([0,1,0])

print("Array A:\n",a)

print("Array B:\n",b)

print("Array A dimension:",a.ndim)
print("Array A elements sum:",a.sum())
print("Array A elements mean",a.mean())
print("Array A element min",a.min())
print("Array A element max",a.max())
print("Array A element min position",a.argmin())
print("Array A element max position",a.argmax())
print("Array A dimension:",a.shape)
print("Array A total number of elements:",a.size)
print("Array A type:",a.dtype)
print("Array A itemsize(byte):",a.itemsize)

print("Mult AxB:\n",a*b)
print("Mult A+B:\n",a+b)

o = np.ones((4,4))

print("Array of ones:\n",o)

z = np.zeros((4,4))

print("Array of ones:\n",z)

l = np.linspace(0,30,5)

print("Array of radom numbers:\n",l)

r = np.random.rand(5) ##radom numbers between 0 and 1 

print("Array of radom numbers:\n",r)

eye = np.eye(5) ##diagonal ones matrix 

print("Array of diagonal one:\n",eye)


##creating an array 

a = np.arange(1,9,1)

print("Array A:\n",a)

s = np.arange(10)

np.random.shuffle(s)

print("Array A shuflled:\n",s)

a = np.arange(12).reshape(4,3)

print("Array A:\n",a)

data_csv = np.genfromtxt('data.csv',delimiter = ',')

print("Data.csv:\n",data_csv)

print("Check if its bigger than 10:\n",data_csv > 10)










