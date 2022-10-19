# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:27:15 2022

@author: Mei
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import matplotlib.patches as patches

# Load Dataset
df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

# Prepare Data
df = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
df.sort_values('cty', inplace = True)
df.reset_index(inplace = True)

# Draw plot
fig, ax = plt.subplots(figsize = (16, 12), facecolor = 'white', dpi = 80)
ax.vlines(x = df.index, ymin = 0, ymax = df.cty, color = 'firebrick', 
          alpha = 0.7, linewidth = 20)

# Annotate Text
for i, cty in enumerate(df.cty):
    ax.text(i, cty + 0.5, round(cty, 1), horizontalalignment = 'center')

# Title
ax.set_title('Bar Chart for Highway Mileage', fontdict={'size':22})
ax.set(ylabel='Miles Per Gallon', ylim=(0, 30))
plt.xticks(df.index, df.manufacturer.str.upper(), rotation = 60, 
           horizontalalignment = 'right', fontsize = 12)

# Add patches to color the X axis labels
p1 = patches.Rectangle((0.57, -0.01), width = 0.33, height = 0.12, 
                       alpha = 0.1, facecolor = 'green', 
                       transform = fig.transFigure)
p2 = patches.Rectangle((0.124, -0.01), width = 0.446, height = 0.12, 
                       alpha = 0.1, facecolor = 'red', 
                       transform = fig.transFigure)
fig.add_artist(p1)
fig.add_artist(p2)
plt.show()