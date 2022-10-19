# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:51:31 2022

@author: Mei
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")

# Draw Stripplot
fig, ax = plt.subplots(figsize = (16, 10), dpi = 80)
sns.stripplot(x = df.cty, y = df.hwy, jitter = 0.25, size = 8, ax = ax, linewidth = .5)

# Decorations
plt.title('Use jittered plots to avoid overlapping of points', fontsize = 22)
plt.show()

