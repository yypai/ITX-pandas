import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import os

#from IPython.core.display import display, HTML
#display(HTML("<style>.container { width:100% !important; }</style>"))

from tqdm import tqdm
import random

from itx_to_pandas_df import *

import matplotlib 
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Helvetica']
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42


from glob import glob

file_list = glob('../2-lockinBsweep/*')
file_list.sort()



e = 1.6e-19
h = 6.626e-34
G0 = e**2/h






# plot 1: G vs Vsg
fig = plt.figure(figsize=(8, 5))
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)

cmap = plt.get_cmap('rainbow')

plt.xlabel('$V_{sg}$ (mV)', fontsize=18)
plt.ylabel('Conductance ($e^2/h$)', fontsize=18)
#plt.xlim(0, 40)
#plt.ylim(-1, 43)


for i, file in enumerate(file_list):
    color = cmap(float(i)/len(file_list)/1)
    
    dfs = itx_to_pandas(file)
    plt.plot(dfs.Vsg*1000 + i/4, dfs.Gcalc/G0, c = color)
    
plt.savefig('conductance_offset.pdf', dpi = 300, bbox_inches='tight', transparent=True)



# plot 2: G (Vsg, B)
df_all = all_itx('../2-lockinBsweep/')
plt.figure(figsize = (16, 7))
plt.subplot(121)

x = - df_all.xs(slice(0), axis=0, level='row', drop_level=True).B/10000
y = np.linspace(0, 40, 401)
X, Y = np.meshgrid(x, y)

plt.pcolormesh(X, Y, df_all.Gcalc.values.reshape(95, 401).T/G0, cmap='rainbow', rasterized = True)

plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)

cb = plt.colorbar()
cb.ax.set_ylabel('Conductance ($e^2/h$)', rotation=270,  fontsize=14, labelpad= 27)


plt.xlabel('B (T)', fontsize=14)    
plt.ylabel('V$_{sg}$ (mV)', fontsize=14)

plt.subplot(122)

x = - df_all.xs(slice(0), axis=0, level='row', drop_level=True).B/10000
y = np.linspace(0, 40, 401)
X, Y = np.meshgrid(x, y)

plt.pcolormesh(X, Y, df_all.groupby(level = 0).diff(periods = 6).fillna(0)\
                .Gcalc.values.reshape(95, 401).T/G0/0.006, cmap='rainbow', rasterized = True)

plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)

cb = plt.colorbar()
cb.ax.set_ylabel('Transconductance ($e^2/Vh$)', rotation=270,  fontsize=14, labelpad= 27)


plt.xlabel('B (T)', fontsize=14)    
plt.ylabel('V$_{sg}$ (mV)', fontsize=14)

plt.ylim(2, 40)
plt.savefig('transconductance.pdf', dpi = 300, bbox_inches='tight', transparent=True)
