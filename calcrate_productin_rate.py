#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


base_path = '.'
files_data = [
    'qt_conditions.txt',
    'qt_densities.txt',
    'qt_rates.txt'
]

files_head = [
    'qt_conditions_list.txt',
    'qt_species_list.txt',
    'qt_reactions_list.txt'
]

file_matrix = 'qt_matrix.txt'


# In[5]:


dfs = []
for file in files_data:
    path = os.path.join(base_path, file)
    dfs.append(pd.read_csv(path, delim_whitespace=True))

headers = []
for file in files_head:
    path = os.path.join(base_path, file)
    headers.append(pd.read_csv(path, delim_whitespace=True, header=None))

path = os.path.join(base_path, file_matrix)
mtx = pd.read_csv(path, delim_whitespace=True, header=None)


# In[6]:


species = headers[1].loc[:, 1].tolist()
reactions = headers[2].loc[:, 1].tolist()


# In[7]:


dfs[1].columns = ['Time [s]'] + species
dfs[2].columns = ['Time [s]'] + reactions
mtx.columns = reactions
mtx.index = species


# # Calcrate Production rate of one species

# In[22]:


tim_nd = dfs[2].iloc[:, 0].to_numpy()
rop_nd = dfs[2].iloc[:, 1:].to_numpy()
mtx_nd = mtx.to_numpy()


# In[27]:


prod_nd = rop_nd.dot(mtx_nd.T)
prod_nd = np.concatenate((tim_nd.reshape(-1, 1), prod_nd), axis=1)
columns=['Time [s]'] + species
prod_df = pd.DataFrame(prod_nd, columns=columns)


# In[28]:


prod_df.to_csv('Productin_rate_of_each_species.csv')

