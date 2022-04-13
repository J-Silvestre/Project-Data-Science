# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:34:47 2022

@author: Rosanna
"""

# Import libraries
import pandas as pd  

# Read splitted review files -> Important: Directory needs to be changed!
df_reviews_1 = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_1.csv", sep=",")
df_reviews_2 = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_2.csv", sep=",")
df_reviews_3 = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_3.csv", sep=",")
df_reviews_4 = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_4.csv", sep=",")

# Delete in each df rows with missing values 
df_reviews_1 = df_reviews_1.dropna()
df_reviews_2 = df_reviews_2.dropna()
df_reviews_3 = df_reviews_3.dropna()
df_reviews_4 = df_reviews_4.dropna()


# Eliminate \r<br/>
df_reviews_1["comments"] = df_reviews_1["comments"].str.replace('\r<br/>', '')
df_reviews_2["comments"] = df_reviews_2["comments"].str.replace('\r<br/>', '')
df_reviews_3["comments"] = df_reviews_3["comments"].str.replace('\r<br/>', '')
df_reviews_4["comments"] = df_reviews_4["comments"].str.replace('\r<br/>', '')

# Safe each df in one file called "update" -> Important: Directory needs to be changed!
df_reviews_1.to_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_update_1.csv", sep=",")
df_reviews_2.to_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_update_2.csv", sep=",")
df_reviews_3.to_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_update_3.csv", sep=",")
df_reviews_4.to_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_update_4.csv", sep=",")


'''
# merge splitted review files
dfs = [df_reviews_1, df_reviews_2, df_reviews_3, df_reviews_4]
merged_df = pd.concat(dfs)

# Delete rows with missing values (Note: In those cases the comment is missing)
merged_df = merged_df.dropna()
'''

