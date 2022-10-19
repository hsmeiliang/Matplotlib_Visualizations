# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:00:41 2022

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
import joypy

# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

# Prepare Data
# plt.figure(figsize=(16,20), dpi= 80)
fig, axes = joypy.joyplot(df, column=['hwy', 'cty'], by="class", ylim='own', 
                          figsize=(8, 8))

# Decoration
plt.title('Joy Plot of City and Highway Mileage by Class', fontsize=10)
plt.show()
