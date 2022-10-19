# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:00:59 2022

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

# Draw plot
plt.figure(figsize = (14, 16), dpi = 80)
plt.scatter(df.mpg_z, df.index, s = 450, alpha = .6, color = df.colors)
# plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z)
for x, y, tex in zip(df.mpg_z, df.index, df.mpg_z):
    t = plt.text(x, y, round(tex, 1), horizontalalignment = 'center',
                 verticalalignment = 'center', fontdict = {'color': 'white'})

# Decorations

# Lighten borders (淡化邊框)
plt.gca().spines['top'].set_alpha(0.3)
plt.gca().spines['bottom'].set_alpha(0.3)
plt.gca().spines['right'].set_alpha(0.3)
plt.gca().spines['left'].set_alpha(0.3)

plt.yticks(df.index, df.cars)
plt.title('Diverging Dotplot of Car Mileage', fontdict={'size':20})
plt.xlabel('$Mileage$')
plt.grid(linestyle='--', alpha=0.5)
plt.xlim(-2.5, 2.5)
plt.show()