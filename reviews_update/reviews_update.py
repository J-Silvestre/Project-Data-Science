# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:34:47 2022

@author: Rosanna
"""

# Import libraries
import pandas as pd  

# Read splitted review files 
df_reviews_1 = pd.read_csv("reviews_1.csv", sep=",")
df_reviews_2 = pd.read_csv("reviews_2.csv", sep=",")
df_reviews_3 = pd.read_csv("reviews_3.csv", sep=",")
df_reviews_4 = pd.read_csv("reviews_4.csv", sep=",")

# Delete in each df rows with missing values
df_reviews_1 = df_reviews_1.dropna()
df_reviews_2 = df_reviews_2.dropna()
df_reviews_3 = df_reviews_3.dropna()
df_reviews_4 = df_reviews_4.dropna()

# Safe each df in one file called "update"
df_reviews_1.to_csv("reviews_update_1.csv", sep=",")
df_reviews_2.to_csv("reviews_update_2.csv", sep=",")
df_reviews_3.to_csv("reviews_update_3.csv", sep=",")
df_reviews_4.to_csv("reviews_update_4.csv", sep=",")

'''
# merge splitted review files
dfs = [df_reviews_1, df_reviews_2, df_reviews_3, df_reviews_4]
merged_df = pd.concat(dfs)

# Delete rows with missing values (Note: In those cases the review is missing)
merged_df = merged_df.dropna()
'''


'''
# Remove "\r<br/>" from column "comments"
# Note: Python gives an error, but removes the "\r<br/>" values correctly! But because of the error it is not possible to save the new file.
comments = df_reviews["comments"]
for i in range (len(comments)):
    comments[i] = comments[i].replace("\r<br/>", "")
'''

df_reviews.to_csv("reviews_update.csv", sep=",")
