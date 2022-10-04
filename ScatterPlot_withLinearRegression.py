# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:43:18 2022

@author: j6xul
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# Import dataset
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_select = df.loc[df.cyl.isin([4, 8]), :]
'''
"manufacturer","model","displ","year","cyl","trans","drv","cty","hwy","fl","class"
'''

# Plot
sns.set_style('white')
gridobj = sns.lmplot(x = 'displ', y = 'hwy', hue = 'cyl', data = df_select, 
                     height = 7, aspect = 1.6, robust = True, palette = 'tab10', 
                     scatter_kws = dict(s = 60, linewidths = .7, edgecolors = 'black'))

p = sns.lmplot(x = 'displ', y = 'hwy', data = df_select, 
               height = 7, robust = True, palette = 'Set1', col = 'cyl', 
               scatter_kws = dict(s = 60, linewidths = .7, edgecolors = 'black'))

# Decorations
gridobj.set(xlim = (0.5, 7.5), ylim = (0, 50))
p.set(xlim = (0.5, 7.5), ylim = (0, 50))
plt.title('Scatterplot with line of best fit grouped by number of cylinders', fontsize = 20)

# Show
plt.show()
