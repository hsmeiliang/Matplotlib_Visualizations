# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:25:52 2022

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
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")

# Prepare Data
x = df.loc[:, ['mpg']]
df['mpg_z'] = (x - x.mean())/x.std()
# df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
df['colors'] = 'black'
df.loc[df.cars == 'Fiat X1-9', 'colors'] = 'darkorange'
df.sort_values('mpg_z', inplace = True)
df.reset_index(inplace = True)



# Draw plot
plt.figure(figsize = (14, 16), dpi = 80)
plt.hlines(y = df.index, xmin = 0, xmax = df.mpg_z, 
           color = df.colors, alpha = 0.4, linewidth = .5)
plt.scatter(df.mpg_z, df.index, color = df.colors,
            s = [600 if x == 'Fiat X1-9' else 300 for x in df.cars], alpha = 0.6)

plt.yticks(df.index, df.cars)
plt.xticks(fontsize = 12)

# Annotate
plt.annotate('Mercedes Models', xy = (0.0, 11.0), xytext = (1.0, 11), xycoords = 'data',
             fontsize = 15, ha = 'center', va = 'center', 
             bbox = dict(boxstyle = 'square', fc = 'firebrick'), 
             arrowprops = dict(arrowstyle = '-[, widthB=2.0, lengthB=1.5', 
                           lw = 2.0, color = 'steelblue'), 
             color = 'white')

'''
more details about bbox
    https://blog.csdn.net/dss_dssssd/article/details/84567689
'''

# Add patches
p1 = patches.Rectangle((-2.0, -1), width = 0.3, height = 3, alpha = 0.2, facecolor = 'red')
p2 = patches.Rectangle((1.5, 27), width = 0.8, height = 5, alpha = 0.2, facecolor = 'green')
plt.gca().add_patch(p1)
plt.gca().add_patch(p2)

# Decorate
plt.title('Diverging Bars of Car Mileage', fontdict={'size':20})
plt.grid(linestyle = '--', alpha = 0.5)
plt.show()