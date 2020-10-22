# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:35:25 2020

@author: Qin Lei
"""

from util.ECA import getInitState
from util.ECA import ECA
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

inequivalent = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22,
                23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,40,41,42,43,44,45,
                46,50,51,54,56,57,58,60,62,72,73,74,76,77,78,90,94,104,105,106,108,
                110,122,126,128,130,132,134,136,138,140,142,146,150,152,154,156,
                160,162,164,168,170,172,178,184,200,204,232]

df = pd.read_csv("data/classificaiton2_sampling_Surface_for_draw.csv") 

max_list = []
min_list = []
diff_list = []

for rule in inequivalent:
    max_list.append(df[df.rule == rule]["System_entropy"].max())
    min_list.append(df[df.rule == rule]["System_entropy"].min())
    diff_list.append(df[df.rule == rule]["System_entropy"].max() - df[df.rule == rule]["System_entropy"].min())


df_class2 = pd.DataFrame({"rule":inequivalent}, columns = ["rule", "max", "diff"])
df_class2["max"] = max_list
df_class2["diff"] = diff_list
df_class2["min"] = min_list
for row in df_class2.iterrows():
    plt.scatter(x=row[1][1], y=row[1][2],marker="$"+str(int(row[1][0]))+"$", s=120)
plt.xlabel(r"$H_{ks}$")
plt.ylabel(r"$diff$")