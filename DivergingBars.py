# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:31:50 2022

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
df['mpg_z'] = (x - x.mean()) / x.std()
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace = True)
df.reset_index(inplace =  True)

# Draw plot
plt.figure(figsize = (14, 10), dpi = 80)
plt.hlines(y = df.index, xmin = 0, xmax = df.mpg_z, color = df.colors, alpha = 0.4, linewidth = 5)

# Decorations
plt.gca().set(ylabel = '$Model$', xlabel = '$Mileage$')
plt.yticks(df.index, df.cars, fontsize = 12)
plt.title('Diverging Bars of Car Mileage', fontdict = {'size': 20})
plt.grid(linestyle = '--', alpha = 0.5)
plt.show()

