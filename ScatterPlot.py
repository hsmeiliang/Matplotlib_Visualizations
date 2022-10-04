# import library
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# Import dataset 
midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

'''
PID,county,state,area,poptotal,popdensity,popwhite,popblack,popamerindian,
popasian,popother,percwhite,percblack,percamerindan,percasian,percother,
popadults,perchsd,percollege,percprof,poppovertyknown,percpovertyknown,
percbelowpoverty,percchildbelowpovert,percadultpoverty,percelderlypoverty,
inmetro,category,dot_size
'''

# Prepare Data

### Create as a many color as there are unique midwest['category']
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories) - 1)) for i in range(len(categories))]

### Draw Plot for each category
plt.figure(figsize = (16, 10), dpi = 80, facecolor = 'w', edgecolor = 'k')

for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal', data = midwest.loc[midwest.category == category, :], 
                s = 20, c = colors[i], label = str(category))
    
# Decoratations
plt.gca().set(xlim = (0.0, 0.1), ylim = (0, 90000), xlabel = 'Area', ylabel = 'Population')

plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

plt.title('Sxatterplot of Midwest Area vs Population', fontsize = 12)
plt.legend(fontsize = 12)

# Show
plt.show()