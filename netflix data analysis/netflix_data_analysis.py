#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:07:40 2018

@author: abhiyush
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# To read excel file with sheet name as netflix
df = pd.read_excel("/home/abhiyush/mPercept/Pandas/netflix data analysis/netflix.xlsx", sheet_name = 'netflix')
df.head()

# =============================================================================
# df_csv = pd.read_csv("/home/abhiyush/mPercept/Pandas/netflix data analysis/netflix_csv.csv")
# 
# # To read excel file with sheet name as By Year
# df_year = pd.read_excel("/home/abhiyush/mPercept/Pandas/netflix data analysis/netflix.xlsx", sheet_name = 'By Year')
# df_year
# 
# =============================================================================
# To get column name 
df.columns

# To get info of the dataframe
df.info()

# To list the null value in 'user rating score' column
df[df['user rating score'].isnull() == True]

def data_cleaning():
    # To drop a row with null value
    df.dropna(inplace = True)
    
    # To drop a row with duplicate value
    df.drop_duplicates(inplace = True)

data_cleaning()
pair_plot()
def pair_plot():
    # To plot the all the columns
    sns.pairplot(df, hue = 'rating')

df.describe()

#Split-Apply-Combine method

#Split
# Grouping the data by release year
df_by_year = df.groupby('release year')

for name, group in df_by_year:
    print(name)
    print(group)

# Checking the type of group by objects
type(df_by_year)


#Apply
df_by_year.describe().head()

# Casting group as list and check out one year
list(df_by_year)[10]

# To diplay the median values by year
df_median_by_year = df_by_year.median()
df_median_by_year.head()

# Print the index of the original dataframe
df.index

# the index of the dataframe grouped by year
df_median_by_year.index

df.info()

#Slice out user rating and plot the graph using matplotlib 
df_rating_by_year = df_median_by_year['user rating score']
plt.scatter(df_rating_by_year.index, df_rating_by_year)
plt.bar(df_rating_by_year.index, df_rating_by_year)
plt.xlabel("Year of release")
plt.ylabel("Median rating")
plt.title("User median ratings VS Year of release")

# Bar plot using pandas
df_rating_by_year.plot.bar(title = "User median ratings VS Year of release")

# Bar plot using seaborn
sns.barplot(df_rating_by_year.index, df_rating_by_year)


# To list the zeroth row of column 'rating'
list(df_by_year['rating'])[20]

# To print the name and group from the df_by_year['rating']
for name, group in df_by_year['rating']:
    print(name) 
    print(group)
    
name, group = list(df_by_year['rating'])[26]

type(group)
g = group[1:2]
list(g)
# To print the count of the rating according to the year
print(df_by_year['rating'].count())

df.info()

#******************************************************************************
# Grouping the data according to release year and rating
df_year_rating = df.groupby(['release year', 'rating'])
df_year_rating_list = list(df_year_rating)

# To make a list of counts of the rating according to the year
year_rating_count_list = []
for name, group in df_year_rating['rating']:
    name_list = list(name)
    name_list.append(len(group))
    year_rating_count_list.append(name_list)

df_year_rating_count = pd.DataFrame(year_rating_count_list, columns =['Year','Rating','Rating_counts'])
df1 = df_year_rating_count.iloc[60:,:]
sns.set(style="whitegrid")
ax = sns.barplot(x="Year", y="Rating_counts", hue="Rating", data=df1)

# =============================================================================
# #******************************************************************************
# dict_count = {}
# # =============================================================================
# # for name, group in df_year_rating:
# #     dict_count[name] = (group)
# # =============================================================================
# df_year_rating_count = df_year_rating['rating'].count()#[0:10]
# df_year_rating_count_list = list(df_year_rating_count)
# 
# for i in range(len(df_year_rating_list)):
#     #df_year_rating_list[i][0][0]
#     if df_year_rating_list[i][0][0] in dict_count:
#         dict_count[df_year_rating_list[i][0][0]].append((df_year_rating_list[i][0][1], df_year_rating_count_list[i]))
#     else:
#         dict_count[df_year_rating_list[i][0][0]] = [(df_year_rating_list[i][0][1], df_year_rating_count_list[i])]
# 
# df11 = pd.DataFrame(data = df_year_rating)
# 
# x = dict_count.keys()
# type(x)
# x_list = list(x)
# y = dict_count.values()
# y_list = list(y)
# 
# plt.bar(x_list, y_list, color='g')
# 
# #******************************************************************************
# 
# =============================================================================


# making the list of column 'ratings' only of the group 'year' and 'rating'
df_year_rating_count = df_year_rating['rating'].count()#[0:10]
df_year_rating_count.shape
df_year_rating['rating'].count()[20:30].plot.bar()
type(df_year_rating_count)

# Grouping the dataframe by 'rating'
df_by_rating = df.groupby('rating')

# to create a unique list of ratings
rating_list = list(set([ratings for ratings in df['rating']]))

rating_count_list = []
for name, group in df_by_rating:
    print(name)
    name_list = list([name])
    name_list.append(len(group))
    rating_count_list.append(name_list)

df_rating_counts = pd.DataFrame(rating_count_list, columns = ['Rating', 'Rating_counts'])




colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red','blue',
          'green','silver','aqua','azure','brown','coral', 'black']
sizes = list(df_rating_counts['Rating_counts'])
labels = list(df_rating_counts['Rating'])
fig, ax = plt.subplots(figsize = (8,8))
# Plot
plt.pie(sizes, labels=labels, colors = colors, shadow=True)
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.show()
    