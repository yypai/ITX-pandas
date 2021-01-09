# not always this file name:
# 
# macOS: 
# rm ~/.cache/.matplotlib/fontlist-v310.json
#
# Windows: 
# .matplotlib>del fontlist-v330.json

import matplotlib 
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Helvetica']
