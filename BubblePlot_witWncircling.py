# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:19:20 2022

@author: j6xul
"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import patches
from scipy.spatial import ConvexHull
import warnings; warnings.simplefilter('ignore')

sns.set_style('white')

# Import dataset
midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")
'''
PID,county,state,area,poptotal,popdensity,popwhite,popblack,popamerindian,
popasian,popother,percwhite,percblack,percamerindan,percasian,percother,
popadults,perchsd,percollege,percprof,poppovertyknown,percpovertyknown,
percbelowpoverty,percchildbelowpovert,percadultpoverty,percelderlypoverty,
inmetro,category,dot_size
'''

# Prepare Data

### Create as a many color as there are unique midwest['category']
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories) - 1)) for i in range(len(categories))]

### Draw Plot for each category
plt.figure(figsize = (16, 10), dpi = 80, facecolor = 'w', edgecolor = 'k')
for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal', data = midwest.loc[midwest.category == category, :], 
                s = 'dot_size', c = colors[i], label = str(category), edgecolors = 'black', linewidths=.5)

# Encircling
def encircle(x, y, ax = None, **kw):
    if not ax: ax = plt.gca()
    p = np.c_[x, y]
    hull = ConvexHull(p)
    poly = plt.Polygon(p[hull.vertices, :], **kw)
    ax.add_patch(poly)

### Select data to be encircled
midwest_encircle_data = midwest.loc[midwest.state == 'IN', :]

### Draw polygon surrounding vertices
encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec = 'k', fc = 'gold', alpha = 0.1)
encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec = 'firebrick', fc = 'none', linewidth = 1.5)

### Decorations
plt.gca().set(xlim = (0.0, 0.1), ylim = (0, 90000), xlabel = 'Area', ylabel = 'Population')
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('Bubble Plot with Encircling', fontsize = 22)
plt.legend(fontsize = 12)

# Show
plt.show()
