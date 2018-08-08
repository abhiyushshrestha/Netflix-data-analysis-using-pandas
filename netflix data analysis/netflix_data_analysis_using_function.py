#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:13:52 2018

@author: abhiyush
"""

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


def pair_plot():
    # To plot the all the columns
    sns.pairplot(df, hue = 'rating')


#Split-Apply-Combine method

def split()
    #Split
    # Grouping the data by release year
    df_by_year = df.groupby('release year')
    
    for name, group in df_by_year:
        print(name)
        print(group)
    return df_by_year

def apply(df_by_year):
    #Apply
    return df_by_year.describe().head()


def combine(df_by_year):
    # To diplay the median values by year
    df_median_by_year = df_by_year.median()
    return df_median_by_year


def plot_scatter_matplotlib(df_rating_by_year):
    plt.scatter(df_rating_by_year.index, df_rating_by_year)
    plt.xlabel("Year of release")
    plt.ylabel("Median rating")
    plt.title("User median ratings VS Year of release")

def plot_bar_matplotlib(df_rating_by_year):
    plt.bar(df_rating_by_year.index, df_rating_by_year)
    plt.xlabel("Year of release")
    plt.ylabel("Median rating")
    plt.title("User median ratings VS Year of release")

def plot_bar_pandas(df_rating_by_year):
    # Bar plot using pandas
    df_rating_by_year.plot.bar(title = "User median ratings VS Year of release")

def plot_bar_seaborn(df_rating_by_year):
    # Bar plot using seaborn
    sns.barplot(df_rating_by_year.index, df_rating_by_year)

def plot_bar_count_ratings_by_year():
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
    ax = sns.barplot(x="Year", y="Rating_counts", hue="Rating", data=df1).set_title("Netflix shows by year by rating")

def plot_pie_count_ratings_by_year():
    # Grouping the dataframe by 'rating'
    df_by_rating = df.groupby('rating')
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
    #patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    #plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.title("Netflix shows by Rating")
    plt.show()

def plot_bar_count_by_year():
    df_by_year = df.groupby('release year')
    total_shows_release_year = []
    for name, group in df_by_year:
        name_list = list([name])
        name_list.append(len(group))
        total_shows_release_year.append(name_list)
    df_movie_count_by_year = pd.DataFrame(total_shows_release_year, columns = ['Year', 'Total shows'])
    df2 = df_movie_count_by_year.iloc[25:, :]
    sns.barplot(x = "Year", y = "Total shows", hue = "Year" , data = df2).set_title("Netflix shows Release date by Year")
# Using functions
    
# Cleaning the data 
data_cleaning()

# Grouping the data by year
df_by_year = split()

# Checking the type of group by objects
type(df_by_year)

# Looking desciption of df_by_year
apply(df_by_year)

df.describe()

# Casting group as list and check out one year
list(df_by_year)[10]

# calculating medain for each release year
df_median_by_year = combine(df_by_year)
df_median_by_year.head()

# Print the index of the original dataframe
df.index

# the index of the dataframe grouped by year
df_median_by_year.index

df.info()

#Slice out user rating and plot the graph using matplotlib 
df_rating_by_year = df_median_by_year['user rating score']

# Plotting the pair plot using sea born
pair_plot()
plot_scatter_matplotlib(df_rating_by_year)
plot_bar_matplotlib(df_rating_by_year)
plot_bar_pandas(df_rating_by_year)
plot_bar_seaborn(df_rating_by_year)
plot_bar_count_ratings_by_year()
plot_pie_count_ratings_by_year()
plot_bar_count_by_year()

# To list the zeroth row of column 'rating'
list(df_by_year['rating'])[20]

# To print the name and group from the df_by_year['rating']
for name, group in df_by_year['rating']:
    print(name) 
    print(group)
    
name, group = list(df_by_year['rating'])[26]

# To print the count of the rating according to the year
print(df_by_year['rating'].count())

df.info()


# to create a unique list of ratings
rating_list = list(set([ratings for ratings in df['rating']]))

# making the list of column 'ratings' only of the group 'year' and 'rating'
df_year_rating_count = df_year_rating['rating'].count()#[0:10]
df_year_rating_count.shape
df_year_rating['rating'].count()[20:30].plot.bar()
type(df_year_rating_count)