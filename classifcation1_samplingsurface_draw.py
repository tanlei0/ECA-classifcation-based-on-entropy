# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:51:49 2020

@author: Qin Lei
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from util.ECA import ECA
from util.ECA import getInitState

def space2ndarray(space, ndspace):
    for i, row in enumerate(space):
        ndspace[i,:] = list(row)

ECA_SURFACE = 'data/ECAsurface_new/'
ENTROPY_SURFACE = "data/classificaiton1_sampling_Surface_for_draw.csv"
df_entropy = pd.read_csv(ENTROPY_SURFACE)

# In[1]
def get_entropy_u(df,rule,crit_str = "mean"):
    D = df[df.rule == rule]["d_ini"].unique().tolist()
    Alpha = df[df.rule == rule].alpha.unique().tolist()
    u = np.empty([len(Alpha), len(D)])
    
    for i, alpha in enumerate(Alpha):
        u[i,:] = df[df.rule == rule][df.alpha == alpha][crit_str].tolist()
    
    return D, Alpha, u

#list1 = [51, 37, 57, 10, 154]
#list2 = [232,12,136,134,50]
#alist = [list1,list2]
#fig = plt.figure()
#for i,ls in enumerate(alist):
#    for j,rule in enumerate(ls):
#       
#       x,y,Z = get_entropy_u(df_entropy, rule)
#       X, Y = np.meshgrid(x, y)
#       ax = fig.add_subplot(2,5,j+i*5+1,projection='3d')
#       ax.plot_wireframe(X, Y, Z, label="entropy")
#       if rule == 37:
#          ax.set_zlim(0.5,1)
#       if i == 1:
#           ax.set_xlabel(r"$\alpha$")
#           ax.set_ylabel(r"$d_{ini}$")
#       #ax.set_zlabel("Entropy of configuration")
#       ax.set_title("("+str(j+i*5+1)+")"+" AECA " + str(rule)) 
        
# In[2] Class 1
list1 = [51, 37, 57]
alist = ["(a)","(b)","(c)"]
fig = plt.figure(figsize=(8,3))
for i,rule in enumerate(list1):
   x,y,Z = get_entropy_u(df_entropy, rule)
   X, Y = np.meshgrid(x, y)
   ax = fig.add_subplot(1,3,i+1,projection='3d')
   ax.plot_wireframe(X, Y, Z, label="entropy")
   if rule == 37:
      ax.set_zlim(0.5,1)

   ax.set_ylabel(r"$\alpha$")
   ax.set_xlabel(r"$d_{ini}$")
   ax.set_title(alist[i]+" AECA " + str(rule)) 
# In[3] Class 2
list1 = [10, 154]
alist = ["(a)","(b)","(c)"]
fig = plt.figure(figsize=(5.3,3))
for i,rule in enumerate(list1):
   x,y,Z = get_entropy_u(df_entropy, rule)
   X, Y = np.meshgrid(x, y)
   ax = fig.add_subplot(1,2,i+1,projection='3d')
   ax.plot_wireframe(X, Y, Z, label="entropy")
   if rule == 37:
      ax.set_zlim(0.5,1)

   ax.set_ylabel(r"$\alpha$")
   ax.set_xlabel(r"$d_{ini}$")
   ax.set_title(alist[i]+" AECA " + str(rule)) 
# In[4] Class 3
list1 = [232,12,136]
alist = ["(a)","(b)","(c)"]
fig = plt.figure(figsize=(8,3))
for i,rule in enumerate(list1):
   x,y,Z = get_entropy_u(df_entropy, rule)
   X, Y = np.meshgrid(x, y)
   ax = fig.add_subplot(1,3,i+1,projection='3d')
   ax.plot_wireframe(X, Y, Z, label="entropy")
   if rule == 37:
      ax.set_zlim(0.5,1)

   ax.set_ylabel(r"$\alpha$")
   ax.set_xlabel(r"$d_{ini}$")
   ax.set_title(alist[i]+" AECA " + str(rule))
# In[5] Class 4
list1 = [134,50]
alist = ["(a)","(b)","(c)"]
fig = plt.figure(figsize=(5.3,3))
for i,rule in enumerate(list1):
   x,y,Z = get_entropy_u(df_entropy, rule)
   X, Y = np.meshgrid(x, y)
   ax = fig.add_subplot(1,2,i+1,projection='3d')
   ax.plot_wireframe(X, Y, Z, label="entropy")
   if rule == 37:
      ax.set_zlim(0.5,1)

   ax.set_ylabel(r"$\alpha$")
   ax.set_xlabel(r"$d_{ini}$")
   ax.set_title(alist[i]+" AECA " + str(rule)) 
