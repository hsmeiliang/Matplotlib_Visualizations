# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:53:02 2022

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

sns.kdeplot(df.loc[df['cyl'] == 4, "cty"], shade=True, color="g", 
            label="Cyl=4", alpha=0.7)
sns.kdeplot(df.loc[df['cyl'] == 5, "cty"], shade=True, color='deeppink', 
            label="Cyl=5", alpha=0.7)
sns.kdeplot(df.loc[df['cyl'] == 6, "cty"], shade=True, color="dodgerblue", 
            label="Cyl=6", alpha=0.7)
sns.kdeplot(df.loc[df['cyl'] == 8, "cty"], shade=True, color="orange", 
            label="Cyl=8", alpha=0.7)

# Decoration
plt.title('Density Plot of City Mileage by n_Cylinders', fontsize=22)
plt.legend()
plt.show()