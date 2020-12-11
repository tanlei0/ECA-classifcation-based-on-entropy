# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:20:49 2020

@author: think
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 23:22:57 2020

@author: Qin Lei
"""



from util.ECA import getInitState
from util.ECA import ECA
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

ENTROPY_SURFACE1 = "data/classificaiton2_sampling_Surface_for_draw.csv"
ENTROPY_SURFACE2 = "data/entropy_sys_c10_for_draw.csv"
df_entropy1 = pd.read_csv(ENTROPY_SURFACE1)
df_entropy2 = pd.read_csv(ENTROPY_SURFACE2)

n_cell = 100
run_num = 100
def space2ndarray(space, ndspace):
    for i, row in enumerate(space):
        ndspace[i,:] = list(row)
        
def get_entropy_u(df,rule,crit_str = "mean"):
    D = df[df.rule == rule]["d_ini"].unique().tolist()
    Alpha = df[df.rule == rule].alpha.unique().tolist()
    u = np.empty([len(Alpha), len(D)])
    
    for i, alpha in enumerate(Alpha):
        u[i,:] = df[df.rule == rule][df.alpha == alpha][crit_str].tolist()
    
    return D, Alpha, u


rule_list3 = [23,33]

is_class3 = False

rule_list = rule_list3
cmap = plt.get_cmap("Greys")

fig = plt.figure(figsize = (10.6, 6))

title_list2 = ["(a)","(b)","(c)","(d)","(e)","(f)"]
init_state = getInitState(n_cell, 0.5)
for i, rule in enumerate(rule_list):
    
    
    eca1 = ECA(rule, init_state=init_state, run_num=run_num, alpha=1)
    eca2 = ECA(rule, init_state=init_state, run_num=run_num, alpha=0.8)
    eca3 = ECA(rule, init_state=init_state, run_num=run_num, alpha=0.3)
    
    ca_list = [eca1, eca2, eca3]
    
    ax = fig.add_subplot(2,5,1+i*5,projection='3d')

    #x,y,Z = get_entropy_u(df_entropy2, rule, "System_entropy")
    x,y,Z = get_entropy_u(df_entropy1, rule, "System_entropy")
    X, Y = np.meshgrid(x, y)
    ax.plot_wireframe(X,Y,Z, label="entropy")
    ax.set_xlabel(r"$d_{ini}$")
    ax.set_ylabel(r"$\alpha$")
    ax.set_zlabel(r"$g_{H_N}$")
    ax.set_title("("+str(i+1)+")"" AECA "+ str(rule_list[i]))
    ndsp = np.zeros([run_num, n_cell])
    
    ax = fig.add_subplot(2,5,5+i*5,projection='3d')

    x,y,Z = get_entropy_u(df_entropy2, rule, "System_entropy")
    
    X, Y = np.meshgrid(x, y)
    ax.plot_wireframe(X,Y,Z, label="entropy")
    ax.set_xlabel(r"$d_{ini}$")
    ax.set_ylabel(r"$\alpha$")
    ax.set_zlabel(r"$g_{H_N}$")
    ax.set_title("("+str(i+3)+")"" AECA "+ str(rule_list[i]))
    ndsp = np.zeros([run_num, n_cell])
    
    for j,ca in enumerate(ca_list):
        ca.run(isPrint=False)
        
        
        space2ndarray(ca.space, ndsp)
        ax = fig.add_subplot(2,5,j+2+i*5)
        ax.imshow(ndsp, interpolation='none', cmap=cmap)

        ax.set_title(title_list2[i*3 + j] + " " + r"$\alpha=$"+str(ca.alpha))
        ax.set_xticks([])
        ax.set_yticks([])
        
plt.tight_layout(pad=5)  
plt.show()
#plt.savefig("test1.eps", dpi = 600, format= "eps")
