# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:29:22 2022

@author: Mei
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# Import Dataset
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")

# Plot
plt.figure(figsize = (12, 10), dpi = 80)
sns.heatmap(df.corr(), xticklabels = df.corr().columns, 
            yticklabels = df.corr().columns, cmap = 'RdYlGn',
            center = 0, annot = True)

# Decorations
plt.title('Correlogram of mtcars', fontsize = 22)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.show()