# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:07:08 2022

@author: Mei
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

# Prepare Data
cyl_colors = {4:'tab:red', 5:'tab:green', 6:'tab:blue', 8:'tab:orange'}
df['cyl_color'] = df.cyl.map(cyl_colors)

# Mean and Median city mileage by make
data = df[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
data.sort_values('cty', ascending = False, inplace = True)
data.reset_index(inplace = True)
data_median = df[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.median())

# Draw horizontal lines
fig, ax = plt.subplots(figsize = (16, 10), dpi = 80)
ax.hlines(y = data.index, xmin = 0, xmax = 40, color = 'gray', alpha = 0.5, 
         linewidth = 0.5, linestyles = 'dashdot')

# Draw the Dot
for i, make in enumerate(data.manufacturer):
    data_make = (df.loc[df.manufacturer==make, :])
    ax.scatter(y=np.repeat(i, data_make.shape[0]).tolist(), x='cty', data=data_make, 
               s=75, edgecolors='gray', c='w', alpha=0.5)
    ax.scatter(y=i, x='cty', data=data_median.loc[data_median.index==make, :], 
               s=75, c='firebrick')
    
# Annotate    
ax.text(33, 13, "$red \; dots \; are \; the \: median$", 
        fontdict={'size':12}, color='firebrick')

# Decorations
red_patch = plt.plot([],[], marker="o", ms=10, ls="", mec=None, 
                     color='firebrick', label="Median")
plt.legend(handles=red_patch)
ax.set_title('Distribution of City Mileage by Make', fontdict={'size':22})
ax.set_xlabel('Miles Per Gallon (City)', alpha=0.7)
ax.set_yticks(data.index)
ax.set_yticklabels(data.manufacturer.str.title(), 
                   fontdict={'horizontalalignment': 'right'}, alpha=0.7)
ax.set_xlim(1, 40)
plt.xticks(alpha=0.7)

plt.gca().spines["top"].set_visible(False)    
plt.gca().spines["bottom"].set_visible(False)    
plt.gca().spines["right"].set_visible(False)    
plt.gca().spines["left"].set_visible(False)

plt.grid(axis='both', alpha=0.4, linewidth=0.1)

plt.show()
