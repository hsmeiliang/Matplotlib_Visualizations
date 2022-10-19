# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:50:23 2022

@author: Mei
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# Load Dataset
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")

# Prepare Data
x = df.loc[:, ['mpg']]
# print(x)
df['mpg_z'] = (x - x.mean())/x.std()
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace = True)
df.reset_index(inplace = True)

# Draw Plot
plt.figure(figsize = (14,14), dpi = 80)
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z)
# plt.hlines(y = df.index, xmin = 0, xmax = df.mpg_z, color = df.colors, alpha = 0.4, linewidth = 5)
for x, y, tex, c in zip(df.mpg_z, df.index, df.mpg_z, df.colors):
    t = plt.text(x, y, round(tex, 2), 
                 horizontalalignment = 'right' if x < 0 else 'left',
                 verticalalignment='center',
                 fontdict={'color': c, 'size': 14})

# Decorations
plt.yticks(df.index, df.cars, fontsize = 12)
plt.title('Diverging Text Bars of Car Mileage', fontdict={'size':20})
plt.grid(linestyle='--', alpha=0.5)
plt.xlim(-2.5, 2.5)
plt.show()