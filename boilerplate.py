import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import os

#from IPython.core.display import display, HTML
#display(HTML("<style>.container { width:100% !important; }</style>"))

from tqdm import tqdm
import random
import seaborn

from itx_to_pandas_df import all_itx
from itx_to_pandas_df import itx_to_pandas
from itx_to_pandas_df import triangle_range
from itx_to_pandas_df import resample_itx
from itx_to_pandas_df import resamp_helper

#import matplotlib
#matplotlib.rcParams['pdf.fonttype'] = 42
#matplotlib.rcParams['ps.fonttype'] = 42

import getpass
#base_path = '/Volumes/Deneb/Expt/'
base_path = '/Users/' + getpass.getuser() + '/Desktop/'

#device_name = 'SA02703K.20130915'
#device_name = 'SA02703K.20130925'
#device_name = 'SA03092E.20180417'
#device_name = 'SA03094E.20180601'
#device_name = 'SA03094E.20180620'
#device_name = 'SA03094E.20180629'
#device_name = 'SA03092E.20190206'
device_name = 'SA03092E.20190517'

folders = [file for file in os.listdir(base_path + device_name)] 
#folders = [file for file in os.listdir(base_path + device_name) if '.pkl' in file] 
folders.sort()

folders
