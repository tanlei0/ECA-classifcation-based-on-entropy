# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:32:56 2020

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
df_entropy1 = pd.read_csv(ENTROPY_SURFACE1)
df_entropy2 = pd.read_csv(ENTROPY_SURFACE2)

# In[1]
def get_entropy_u(df,rule,crit_str = "mean"):
    D = df[df.rule == rule]["d_ini"].unique().tolist()
    Alpha = df[df.rule == rule].alpha.unique().tolist()
    u = np.empty([len(Alpha), len(D)])
    
    for i, alpha in enumerate(Alpha):
        u[i,:] = df[df.rule == rule][df.alpha == alpha][crit_str].tolist()
    
    return D, Alpha, u


        
# In[2]
rule_list = [138, 170, 184]
fig = plt.figure(figsize=(8,6))
for j in range(2):
    
    for i,rule in enumerate(rule_list):
    
    
        dval = np.linspace(0.2, 0.8, 7)
        A = np.linspace(0.2, 1, 9)
        
        eca_surface_path = ECA_SURFACE+str(rule)+'.csv'
        u1 = pd.read_csv(eca_surface_path)
        x = dval
        y = A
        X, Y = np.meshgrid(x, y)
        Z = u1
        if j==0:
            ax = fig.add_subplot(2,3,1+i,projection='3d')
            ax.plot_wireframe(X, Y, Z, label="density")
            ax.set_xlabel(r"$d_{ini}$")
            ax.set_ylabel(r"$\alpha$")
            ax.set_zlabel("Density")
            ax.set_title("("+str(i*2 + 1)+")"+"AECA "+str(rule))
        if j==1:    
            ax = fig.add_subplot(2,3,4+i,projection='3d')
            x,y,Z = get_entropy_u(df_entropy1, rule)
            X, Y = np.meshgrid(x, y)
            ax.plot_wireframe(X,Y,Z, label="entropy")
            ax.set_xlabel(r"$d_{ini}$")
            ax.set_ylabel(r"$\alpha$")
            ax.set_zlabel(r"$g_{\bar{H}}$")
            ax.set_title("("+str(i*2 + 2)+")"+"AECA "+str(rule))