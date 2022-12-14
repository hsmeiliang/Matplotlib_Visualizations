# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:41:30 2022

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
          alpha = 0.7, linewidth = 2)
ax.scatter(x = df.index, y = df.cty, s = 75, color = 'firebrick', alpha = 0.7)

# Title
ax.set_title('Lollipop Chart for Highway Mileage', fontdict={'size':22})
ax.set_ylabel('Miles Per Gallon')
ax.set_xticks(df.index)
ax.set_xticklabels(df.manufacturer.str.upper(), rotation = 60, 
                  fontdict = {'horizontalalignment': 'right', 'size': '12'})
ax.set_ylim(0, 30)

# Annotate
for row in df.itertuples():
    ax.text(row.Index, row.cty + 0.5, s = round(row.cty, 2), 
            horizontalalignment = 'center', verticalalignment='bottom', 
            fontsize=14)

plt.show()