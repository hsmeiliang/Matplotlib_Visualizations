# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:56:04 2022

@author: Mei
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import matplotlib.patches as patches
import matplotlib.lines as mlines

# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

# Prepare Data
plt.figure(figsize=(16,10), dpi= 80)

sns.distplot(df.loc[df['class'] == 'compact', "cty"], color="dodgerblue", 
             label="Compact", hist_kws={'alpha':0.7}, kde_kws={'linewidth':3})
sns.distplot(df.loc[df['class'] == 'suv', "cty"], color="orange", 
             label="SUV", hist_kws={'alpha':0.7}, kde_kws={'linewidth':3})
sns.distplot(df.loc[df['class'] == 'minivan', "cty"], color="g", 
             label="minivan", hist_kws={'alpha':0.7}, kde_kws={'linewidth':3})

plt.ylim(0, 0.35)

# Decoration
plt.title('Density Plot of City Mileage by Vehicle Type', fontsize=22)
plt.legend()
plt.show()