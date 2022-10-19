# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:34:37 2022

@author: Mei
"""

'''
more detail:
    https://zhuanlan.zhihu.com/p/98729226

kind：用於控制非對角線上的圖的類型，可選"scatter"與"reg"

diag_kind：控制對角線上的圖的類型，可選"hist"與"kde"

hue：針對某一字段進行分類

palette：控制色調

markers：控制散點的樣式
    
vars, x_vars, y_vars：選擇數據中的特定字段，以list形式傳入

plot_kws：用於控制非對角線上的圖的樣式

diag_kws：用於控制對角線上圖的樣式
'''

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# Load Dataset
df = sns.load_dataset('iris')

# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="reg", hue="species", diag_kind="hist", palette="husl", markers=["+", "s", "D"])
# sns.pairplot(df, kind="scatter", diag_kind="kde", hue="species", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
plt.show()