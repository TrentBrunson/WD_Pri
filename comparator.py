#%%
'''emulate notebooks for code testing'''
#%%
# import dependencies
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt

#%%
# load data
file = 'data\FY23Q1 TA Strategic Alignment - April 11th.xlsx'
df = pd.read_excel(file)
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
# first data visualization
fig, axs = plt.subplots(len(df.columns), figsize = (5,20))
for n, col in enumerate(df.columns):
    a = df[col].hist(ax=axs[n])
    a.set_title(col)

fig.tight_layout()
# %%
# This library captures most of the EDA done above
# https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html
'''data_profile = ProfileReport(df, title="Req Pri Data Profile Report", explorative=True)
data_profile.to_file("HiPri.html")
data_profile.to_notebook_iframe()'''
# %%
