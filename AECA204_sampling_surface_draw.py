# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:42:43 2020

@author: tanlei0
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
ENTROPY_SURFACE = "data/classificaiton1_sampling_Surface_for_draw.csv"
SYS_ENTROPY_SURFACE = "data/classificaiton2_sampling_Surface_for_draw_temp_version.csv"
df_entropy = pd.read_csv(ENTROPY_SURFACE)
df_sys_entropy = pd.read_csv(SYS_ENTROPY_SURFACE)
# In[1]
def get_entropy_u(df,rule,crit_str = "mean"):
    D = df[df.rule == rule]["d_ini"].unique().tolist()
    Alpha = df[df.rule == rule].alpha.unique().tolist()
    u = np.empty([len(Alpha), len(D)])
    
    for i, alpha in enumerate(Alpha):
        u[i,:] = df[df.rule == rule][df.alpha == alpha][crit_str].tolist()
    
    return D, Alpha, u

rule = 204
fig = plt.figure(figsize = (8,3))
dval = np.linspace(0.2, 0.8, 7)
A = np.linspace(0.2, 1, 9)
eca_surface_path = ECA_SURFACE+str(rule)+'.csv'
u1 = pd.read_csv(eca_surface_path)
x = dval
y = A
X, Y = np.meshgrid(x, y)
Z = u1

ax = fig.add_subplot(1,3,1,projection='3d')
ax.plot_wireframe(Y, X, Z, label="density")
ax.set_ylabel(r"$d_{ini}$")
ax.set_xlabel(r"$\alpha$")
ax.set_zlabel("Density")
ax.set_title("(a)")       

x,y,Z = get_entropy_u(df_entropy, rule)
X, Y = np.meshgrid(x, y)
ax = fig.add_subplot(1,3,2,projection='3d')
ax.plot_wireframe(Y, X, Z, label="entropy")

ax.set_ylabel(r"$d_{ini}$")
ax.set_xlabel(r"$\alpha$")
ax.set_zlabel(r"$g_{\bar{H}}$")
ax.set_title("(b)")

x,y,Z = get_entropy_u(df_sys_entropy, rule,"System_entropy")
X, Y = np.meshgrid(x, y)
ax = fig.add_subplot(1,3,3,projection='3d')
ax.plot_wireframe(Y, X, Z, label="entropy")

ax.set_ylabel(r"$d_{ini}$")
ax.set_xlabel(r"$\alpha$")
ax.set_zlabel(r"$g_{H_s}$")
ax.set_title("(c)")


  