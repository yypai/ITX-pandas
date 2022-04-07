import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Helvetica']
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42


matplotlib.rcParams['image.cmap']='coolwarm'

matplotlib.rcParams.update({'font.size': 10})
matplotlib.rcParams.update({'ytick.minor.visible': True,})
matplotlib.rcParams.update({'xtick.minor.visible': True,})
matplotlib.rcParams.update({'errorbar.capsize': 4})


import os

import random

cmap = plt.get_cmap('rainbow')
plt.figure(figsize=(8, 6))
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)



df.Elastic.astype(float).plot(c = cmap(0.01)) 
df.Electric.astype(float).plot(c = cmap(0.2))
df.Landau.astype(float).plot(c = cmap(0.4))
df.Gradient.astype(float).plot(c = cmap(0.6))
df.total.astype(float).plot(c = cmap(0.9))

legend = plt.legend(loc='lower left', frameon=False)

plt.xlabel('step', fontsize=16)
plt.ylabel('energy', fontsize=16)

for label in legend.get_texts():
    label.set_fontsize(14)

for label in legend.get_lines():
    label.set_linewidth(3)  

plt.savefig('energy.pdf', dpi=300,  transparent=True)
