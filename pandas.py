#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 16:07:49 2018

@author: abhiyush
"""

import pandas as pd
import numpy as np
import re

from nltk.stem import WordNetLemmatizer


ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

# To group the dataframe by year
grouped_year = df.groupby('Year')
grouped_team = df.groupby('Team')
grouped_team_year = df.groupby(['Year', 'Team'])
# T0 display the list of index according to group by
df.groupby('Year').groups

# to display the data frame according to the group by
for name,group in grouped_year:
    print (name)
    print (group)
    
for name, group in grouped_team:
    print(name)
    print(group)
    
for name, group in grouped_team_year:
    print(name)
    print(group)
    
# To get the dataframe of specific group
print(grouped_year.get_group(2014))
print(grouped_team.get_group('Devils'))
print(grouped_team_year.get_group(2014, "Devils"))

# To get aggregate mean according to year, team
print(grouped_year['Points'].agg(np.mean))
print(grouped_team['Points'].agg(np.mean))
print(grouped_team_year['Points'].agg(np.mean))

# To see the size of each group
print(grouped_year.agg(np.size))
print(grouped_team.agg(np.size))
print(grouped_team_year.agg(np.size))


#Applying multiple aggregate function
print(grouped_year['Points'].agg([np.sum, np.mean, np.std]))
print(grouped_team['Points'].agg([np.sum, np.mean, np.std]))

#Applying transformation

score = lambda x: (x - x.mean()) / x.std()*10
print (grouped_team['Points'].transform(score))

# Using apply function 
print (grouped_team['Points'].apply(lambda x: (x - x.mean()) / x.std()*10))

for name, group in grouped_team['Points']:
    print(name)
    print(group)

len(df)    
print(grouped_team['Points'].groups)

df1 = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df1.plot.bar()

df1.plot.bar(stacked = True)














lemmatizer = WordNetLemmatizer()
def preprocess(review):
    review = re.sub('[^a-zA-Z]', ' ', review)
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review]
    review = ' '.join(review)
    return review

datasets = pd.read_csv("/home/abhiyush/mPercept/Natural Language Processing/Sentiment Analysis/IMDB reviews/imdb_reviews.csv", delimiter = '\t', quoting = 3, header = None)

# Naming the columns
datasets.columns = ['reviews', 'likes']
df= datasets
df['processed'] = df['reviews'].apply(preprocess)
corpus = []
corpus = df['reviews'].apply(preprocess)

df['split'] = df['processed'].apply(lambda x: x.split())




    