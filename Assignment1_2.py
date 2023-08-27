# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:25:19 2023

@author: airths
"""

import pandas as pn
import numpy as np
import matplotlib.pyplot as plt
import scipy
np.random.seed(1234)
data = pn.read_excel(r"Documents/Courses/MCP261/Exercise1/MCP261 Exercise 1 data.xlsx", sheet_name="Sheet1")
l = []
for i in data:
    #print(data[i])
    arr = []
    for j in data[i]:
        arr+=[j]
    l += [arr]
#print(l)
mu = [sum(i)/(len(i)) for i in l]
print(mu)
# an = (x-x^)*(y-y^)/n
sig = [[0 for _ in range(len(l))] for _ in range(len(l))]
print(sig)
for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l[0])):
           sig[i][j]+=((l[i][k]-mu[i])*(l[j][k]-mu[j])) 
        sig[i][j]/=len(l[0])-1
print(sig)
gamma=0.1
def f(w):
    return -(w.T@mu-gamma*(((w.T)@(sig))@w))
def eq(w):
    return sum(w)-1
n = len(mu)
bnds = scipy.optimize.Bounds([0 for _ in range(n)], [1 for _ in range(n)])
con = {'type': 'eq',
       'fun': lambda w:eq(w)}
x = np.array([0 for _ in range(n)])
x[0]=1;
result = scipy.optimize.minimize(f, x, method='SLSQP', bounds = bnds, constraints = [con])
print(result)