#%%
'''emulate notebooks for code testing'''

#%%
# import dependencies
from glob import glob
import os
import glob
import numpy as np
import pandas as pd
# from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt

#%%
'''
changed to universal file name
# load data
file = 'data\FY23Q1 TA Strategic Alignment - April 11th.xlsx'
df = pd.read_excel(file)
'''
#%%
# read input file from directory - name changes week to week
for f in glob.glob('data/input/*'):
    df = pd.read_excel(f)
df
# %%
df.info
# %%
df.describe()
# %%
df.value_counts()
# %%
df.count()
# %%
df.notna()
# %%
df.isna().sum()
# %%
df.isna().sum().sum()
#%%
df.nunique()
# %%
'''# first data visualization
fig, axs = plt.subplots(len(df.columns), figsize = (5,20))
for n, col in enumerate(df.columns):
    a = df[col].hist(ax=axs[n])
    a.set_title(col)

fig.tight_layout()'''
# %%
# drop columns

# drop rows
    # Where <> Asklund
df.drop(df[df['Level 5 Manager'] != 'Asklund, Travis'].index, inplace=True)
    # exempt reqs
# df.drop(df[df['Job Family Group'] != ('Engineering Research & Development' or 'Interns')].index, inplace=True)
# df.drop(df[df['Recruiting Instruction'] == 'Campus'].index, inplace=True)

    # no more fills needed
    # what else
df.info()
# %%
df.columns.values.tolist()
# %%
GOPOdf = df[['REQ Status', 'Requisition NO', 'Hiring Manager Badge', 'Hiring Manager Name', 
 'Job Posting Title', 'Backfill Indicator', 'Replacement for Worker']]
GOPOdf
# %%
# compare new file to old priorities
# %%
# join hiring manager to L6

# add a new column
GOPOdf.insert(4,'L6', 'NaN')
GOPOdf
# %%
GOPOdf
# %%
