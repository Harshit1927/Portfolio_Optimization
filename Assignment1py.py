# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 09:15:31 2023

@author: airths
"""
import pandas as pn
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1234)
data = pn.read_excel(r"Documents/Courses/MCP261/Exercise1/MCP261 Exercise 1 data.xlsx", sheet_name="Sheet1")
l = []
for i in data:
    print(i)
    arr = []
    for j in data[i]:
        arr+=[j]
    l += [arr]
#print(l)
mean = [sum(i)/(len(i)) for i in l]
print(mean)
# an = (x-x^)*(y-y^)/n
an = [[0 for _ in range(len(l))] for _ in range(len(l))]
print(an)
an = np.array(an)
for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l[0])):
           an[i][j]+=((l[i][k]-mean[i])*(l[j][k]-mean[j])) 
        an[i][j]/=len(l[0])
print(an)
sumj = [5, 50, 500, 5000, 50000, 500000]
def sim(w):
    mu = mean
    gamma = 0.1 #given
    cov = an
    return ((w.T@mu) - gamma*(((w.T@cov)@w)))
ar = [1, 2, 3, 4, 5]
def du(inp):
    for i in inp:
        np.random.seed(1234)
        mx = -np.inf;
        portfolio = []
        for j in range(i):
            w = np.random.random(an.shape[0])
            w/=sum(w)
            #w = np.random.dirichlet([1 for _ in range(an.shape[0])])
            # print(w)
            # plt.scatter(ar, w)
            # if (sum(w)!=1):
                # print(w)
            simulate = sim(w)
            if (mx<simulate):
                portfolio = w;
                mx = simulate
        print("Best performing portfolio for " + str(i) + " replications: ", end=" ")
        print(portfolio, end=", with maximum answer = "+str(mx)+"\n");
du(sumj)
# plt.show();


