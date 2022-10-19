# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:26:18 2022

@author: Mei
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:33:00 2022

@author: Mei
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")

# Create Fig and gridspec
fig = plt.figure(figsize = (16, 10), dpi = 80)
grid = plt.GridSpec(4, 4, hspace = 0.5, wspace = 0.2)

# Define the axes
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels = [], yticklabels = [])
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels = [], yticklabels = [])

# Scatterplot on main ax
ax_main.scatter('displ', 'hwy', s = df.cty*4, 
                c = df.manufacturer.astype('category').cat.codes,
                alpha = .9, data = df, cmap = 'tab10', edgecolors = 'gray',
                linewidths = 0.5)

# Add a graph in each part
sns.boxplot(df.hwy, ax = ax_right, orient = 'v')
sns.boxplot(df.cty, ax = ax_bottom, orient = 'h')

# Decorations
ax_bottom.set(xlabel='')
ax_right.set(ylabel='')
ax_main.set(title = 'Scatterplot with Histograms \n displ vs hwy', xlabel='displ', ylabel='hwy')
ax_main.title.set_fontsize(20)
for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
    item.set_fontsize(14)

xlabels = ax_main.get_xticks().tolist()
ax_main.set_xticklabels(xlabels)
plt.show()