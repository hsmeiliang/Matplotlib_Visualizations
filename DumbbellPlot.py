# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:07:14 2022

@author: Mei
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import matplotlib.patches as patches
import matplotlib.lines as mlines

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/health.csv")

# Prepare Data
df.sort_values('pct_2014', inplace=True)
df.reset_index(inplace=True)

# Draw line segment
def newline(p1, p2, color = 'black'):
    ax = plt.gca()
    l = mlines.Line2D([p1[0], p2[0]], [p1[1], p2[1]], 
                      color = color)
    ax.add_line(l)
    return l

# Figure and Axes
fig, ax = plt.subplots(1, 1, figsize = (14, 14), facecolor='#f7f7f7', dpi= 80)

# Vertical lines
ax.vlines(x=0.05, ymin=0, ymax=26, color='black', alpha=1, 
          linewidth=1, linestyles='dotted')
ax.vlines(x=0.1, ymin=0, ymax=26, color='black', alpha=1, 
          linewidth=1, linestyles='dotted')
ax.vlines(x=0.15, ymin=0, ymax=26, color='black', alpha=1, 
          linewidth=1, linestyles='dotted')
ax.vlines(x=0.2, ymin=0, ymax=26, color='black', alpha=1, 
          linewidth=1, linestyles='dotted')

# Line Segments
for i, p1, p2 in zip(df['index'], df['pct_2013'], df['pct_2014']):
    newline([p1, i], [p2, i], color = 'skyblue')
    
# Points
ax.scatter(y = df['index'], x = df['pct_2013'], s=50, 
           color='#0e668b', alpha=1)
ax.scatter(y = df['index'], x = df['pct_2014'], s=50, 
           color='#a3c4dc', alpha=1)
    
# Decoration
ax.set_facecolor('#f7f7f7')
ax.set_title("Dumbell Chart: Pct Change - 2013 vs 2014", fontdict={'size':22})
ax.set(xlim=(0,.25), ylim=(-1, 27), ylabel='Mean GDP Per Capita')
ax.set_xticks([.05, .1, .15, .20])
ax.set_xticklabels(['5%', '15%', '20%', '25%'])   
plt.show()

