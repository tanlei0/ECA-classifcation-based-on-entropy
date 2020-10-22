# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 08:09:29 2020

@author: tanlei0
"""


from util.ECA import getInitState
from util.ECA import ECA
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

n_cell = 100
run_num = 100
def space2ndarray(space, ndspace):
    for i, row in enumerate(space):
        ndspace[i,:] = list(row)

# choose the rule_list to draw

#rule_list = [51, 37, 57, 10, 154]
rule_list = [232,12,136,134,50]

cmap = plt.get_cmap("Greys")
fig, ax_list = plt.subplots(len(rule_list),4, sharey="all",figsize=(100,100))

title_list2 = ["(a)","(b)","(c)","(d)","(e)"]
init_state = getInitState(n_cell, 0.5)
for i, rule in enumerate(rule_list):
    
    
    
    eca1 = ECA(rule, init_state=init_state, run_num=run_num, alpha=1)
    eca2 = ECA(rule, init_state=init_state, run_num=run_num, alpha=0.8)
    eca3 = ECA(rule, init_state=init_state, run_num=run_num, alpha=0.5)
    eca4 = ECA(rule, init_state=init_state, run_num=run_num, alpha=0.3)
    
    ca_list = [eca1, eca2, eca3, eca4]
    

    for j,ca in enumerate(ca_list):
        ca.run(isPrint=False)
        
        ndsp = np.zeros([run_num, n_cell])
        
        space2ndarray(ca.space, ndsp)
        ax_list[i][0].set_ylabel("AECA "+str(rule_list[i]))
        ax_list[0][j].set_title(title_list2[j])
        ax_list[i][j].imshow(ndsp, interpolation='none', cmap=cmap)
        ax_list[i][j].set_xticks([])
        ax_list[i][j].set_yticks([])
        
plt.tight_layout(pad=5)  
plt.show()
#plt.savefig("test1.eps", dpi = 600, format= "eps")
