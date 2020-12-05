# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:44:35 2020

@author: Qin Lei
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from util.ECA import ECA
from util.ECA import getInitState
from mpl_toolkits.mplot3d import Axes3D

def space2ndarray(space, ndspace):
    for i, row in enumerate(space):
        ndspace[i,:] = list(row)

ECA_SURFACE = 'data/ECAsurface_new/'
ENTROPY_SURFACE1 = "data/classificaiton1_sampling_Surface_for_draw.csv"
ENTROPY_SURFACE2 = "data/entropy_sys_c10_for_draw.csv"
ENTROPY_LOCAL_SURFACE = "data/sp_local_pattern.csv"
df_entropy1 = pd.read_csv(ENTROPY_SURFACE1)
df_entropy2 = pd.read_csv(ENTROPY_SURFACE2)

df_local = pd.read_csv(ENTROPY_LOCAL_SURFACE)
# In[1]
def get_entropy_u(df,rule,crit_str = "mean"):
    D = df[df.rule == rule]["d_ini"].unique().tolist()
    Alpha = df[df.rule == rule].alpha.unique().tolist()
    u = np.empty([len(Alpha), len(D)])
    
    for i, alpha in enumerate(Alpha):
        u[i,:] = df[df.rule == rule][df.alpha == alpha][crit_str].tolist()
    
    return D, Alpha, u


        
# In[2]
rule_list = [1, 90, 178]
fig = plt.figure(figsize = (8,9))
for i,rule in enumerate(rule_list):
    
    
    dval = np.linspace(0.2, 0.8, 7)
    A = np.linspace(0.2, 1, 9)
    
   
    ax = fig.add_subplot(3,3,1+i*3,projection='3d')
    x,y,Z = get_entropy_u(df_entropy1, rule)
    X, Y = np.meshgrid(x, y)
    if rule == 90:
        ax.set_zlim(0,1)
    ax.plot_wireframe(X,Y,Z, label="entropy")
    ax.set_xlabel(r'$d_{ini}$')
    ax.set_ylabel(r'$\alpha$')
    ax.set_zlabel(r'$g_{\bar{M}_1}$')
    ax.set_title("("+str(i*3 + 1)+") "+"AECA "+str(rule))
    
    ax = fig.add_subplot(3,3,2+i*3,projection='3d')
    x,y,Z = get_entropy_u(df_local, rule, "mean_2")
    X, Y = np.meshgrid(x, y)
    if rule == 90:
        ax.set_zlim(1,2)
    ax.plot_wireframe(X,Y,Z, label="entropy")
    ax.set_xlabel(r'$d_{ini}$')
    ax.set_ylabel(r'$\alpha$')
    ax.set_zlabel(r'$g_{\bar{M}_2}$')
    ax.set_title("("+str(i*3 + 2)+") "+"AECA "+str(rule))
    
    ax = fig.add_subplot(3,3,3+i*3,projection='3d')
    x,y,Z = get_entropy_u(df_local, rule, "mean_3")
    X, Y = np.meshgrid(x, y)
    if rule == 90:
        ax.set_zlim(2,3)
    ax.plot_wireframe(X,Y,Z, label="entropy")
    ax.set_xlabel(r'$d_{ini}$')
    ax.set_ylabel(r'$\alpha$')
    ax.set_zlabel(r'$g_{\bar{M}_3}$')
    ax.set_title("("+str(i*3 + 3)+") "+"AECA "+str(rule))