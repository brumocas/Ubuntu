# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:18:46 2022

@author: bruco
"""

import numpy as np 

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([0,1,0])

print("Matrix A:\n",a)
print("Matrix B:\n",b)

print("Matrix Multiplication AxB:\n",np.dot(a,b))

print("Matrix Multiplication AxB:\n",a @ b )

c = np.array([[1,1],[-1,1]])

print("Matrix C:\n",c)

print("Matrix C transpose:\n",c.T)

print("Matrix C inverse:\n",np.linalg.inv(c))

print("Matrix C determinant:\n",np.linalg.det(c))

print("Matrix C flatten:\n",c.flatten())