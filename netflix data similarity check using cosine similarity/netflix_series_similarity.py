#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:53:10 2018

@author: abhiyush
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel
import seaborn as sns

datasets = df = pd.read_excel("/home/abhiyush/mPercept/Pandas/netflix data analysis/netflix.xlsx", sheet_name = 'netflix')
datasets.columns

df = datasets[['title','ratingDescription', 'user rating score', 'user rating size']]
df.columns

# =============================================================================
# df1 = datasets[['ratingDescription', 'user rating score', 'user rating size']]
# df1.info()
# df1.dropna(inplace = True)
# =============================================================================

df1 = datasets.loc[:, ['ratingDescription', 'user rating score', 'user rating size']]
df1.info()
df1.dropna(inplace = True)

# Manually applying Min max normalization
df1['ratingDescription'] = df1['ratingDescription'].apply(lambda x : ((x - min(df1['ratingDescription']))/(max(df1['ratingDescription']) - min(df1['ratingDescription']))) * (1-0) + 0)
df1['user rating score'] = df1['user rating score'].apply(lambda x : ((x - min(df1['user rating score']))/(max(df1['user rating score']) - min(df1['user rating score']))) * (1-0) + 0)
#df1['user rating size'] = df1['user rating size'].apply(lambda x : ((x - min(df1['user rating size']))/(max(df1['user rating size']) - min(df1['user rating size']))) * (1-0) + 0)

# =============================================================================
# 
# # Using sklearn to apply min max normalization
# scalar = MinMaxScaler(feature_range = (0,1))
# scalar.fit(np.array((df1['ratingDescription'])).reshape(-1,1))
# df1['rd_sk'] = scalar.transform(np.array((df1['ratingDescription'])).reshape(-1,1))
# 
# =============================================================================


df_norm = df1.loc[:, ['ratingDescription', 'user rating score']]

# calculating the cosine similarity 
def calculate_cosine_similarity(df_norm):
    cs_i = []
    for i in range(0,len(df_norm)):
       cs_j = []
       for j in range(0,len(df_norm)): 
           cs_j.append(float(cosine_similarity(df_norm.iloc[i,:].values.reshape(1,-1), 
                          df_norm.iloc[j,:].values.reshape(1,-1))))
       cs_i.append(cs_j) 
    return cs_i

cosine_similarity_calculation = calculate_cosine_similarity(df_norm)

# Creating dataframe for calculated cosine similarity 
cosine_similarity_df = pd.DataFrame(cosine_similarity_calculation)


#******************************************************************************
# Manually created function for cosine similarity calculation
def manual_cosine_similarity(a,b):
    cs = np.dot(a,b.reshape(-1,1))/(np.sqrt(a[0,0] * a[0,0] + a[0,1] * a[0,1]) * 
            np.sqrt(b[0,0] * b[0,0] + b[0,1] * b[0,1]))
    return cs

# calculating the cosine similarity using manually created cosine similarity function
def calculate_cosine_similarity_manually(df_norm):
    cs_i = []
    for i in range(0,len(df_norm)):
       cs_j = []
       for j in range(0,len(df_norm)): 
           cs_j.append(float(manual_cosine_similarity(df_norm.iloc[i,:].values.reshape(1,-1), 
                          df_norm.iloc[j,:].values.reshape(1,-1))))
       cs_i.append(cs_j) 
    return cs_i

cosine_similarity_calculation_manually = calculate_cosine_similarity_manually(df_norm)

# Creating dataframe for manually calculated cosine similarity 
cosine_similarity_manual_df = pd.DataFrame(cosine_similarity_calculation_manually)

#*******************************************************************************


df_list = cosine_similarity_df.iloc[0:10,0:10]

fig, ax =  plt.subplots(figsize = (10,10))
cmap = sns.diverging_palette(240, 10, s=80, l=45, as_cmap = True)
sns.heatmap(df_list, cmap = cmap, vmin = 0.95, vmax = 1, annot = True)


linear_kernel(df_norm.iloc[0,:].values.reshape(1,-1), 
                      df_norm.iloc[0,:].values.reshape(1,-1))

