#20190627-3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

def itx_to_pandas(path):

    file = open(path,'r')
    a = file.read().splitlines()
    file.close()

    key = []
    values = []
    cur = 0
    while cur < len(a) - 1 :

        if 'WAVES/D/N=' in a[cur]:
            key.append(a[cur].split('\'')[1].split('.')[0])
            loc_len = int(a[cur].split(')')[0].split('(')[1])
            value = a[cur + 2 : cur + 2 + loc_len]
            value = [float(line) for line in value]
            values.append(value)
            cur += loc_len
            cur += 2

        cur += 1

    dfn = pd.DataFrame(values).T
    dfn.columns = key
    return dfn



def all_itx(wd):
    #cwd = os.getcwd()
    itxs = [wd + file for file in os.listdir(wd) if file.endswith(".itx")]
    itxs.sort()

    keys = ['%s.itx' %i for i in range(0,len(itxs))]
    frames = [itx_to_pandas(itxs[i]) for i in tqdm(range(0, len(itxs)))]
    df_all = pd.concat(frames, keys = keys)
    df_all.index.names = ['page','row']

    return df_all


def triangle_range(df, page, wave):
    start_index =  min(df.loc[page, wave].idxmax(),
                       df.loc[page, wave].idxmin())

    end_index   =  max(df.loc[page, wave].idxmax(),
                       df.loc[page, wave].idxmin())

    return start_index, end_index

def resample_itx(df_all, current_array, page, voltage_wave, current_wave, start_index, end_index):
    #making tmp df
    df_tmp  = pd.DataFrame({'voltage':df_all.loc['%s.itx' %page, voltage_wave][start_index:end_index],
                            'current':df_all.loc['%s.itx' %page, current_wave][start_index:end_index]})

    df_tmp.sort_values(by = 'current', inplace = True)
    upper, lower = df_tmp.current.max(), df_tmp.current.min()

    #making target df
    df_target = pd.DataFrame(current_array)
    df_target.columns = ['current']
    df_target['voltage'] = np.nan

    #resample
    df_tmp = pd.concat([df_target, df_tmp], sort=False)
    df_tmp = df_tmp.reset_index(drop = True)
    df_tmp = df_tmp.sort_values(by = 'current')
    df_tmp = df_tmp.interpolate()
    df_tmp = df_tmp.sort_index()
    df_tmp = df_tmp[:len(current_array)]

    #padding zero
    df_tmp.at[df_tmp.loc[df_tmp.current<lower].index.tolist(), 'voltage'] = np.nan
    df_tmp.at[df_tmp.loc[df_tmp.current>upper].index.tolist(), 'voltage'] = np.nan

    return df_tmp

def resamp_helper(df_target, df_source, name):
    df_tmp = pd.concat([df_target, df_source], sort=False)
    df_tmp = df_tmp.reset_index(drop = True)
    df_tmp = df_tmp.sort_values(by = name)
    df_tmp = df_tmp.interpolate()
    df_tmp = df_tmp.sort_index()
    df_tmp = df_tmp[:len(df_target)]
    return df_tmp
