# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:11:18 2022

@author: Rosanna
"""
# !! Important note regarding this code: Directories for files need to be changed first!

# import libraries ---------------------------------------------------------------------
import pandas as pd


# Plots for listingsUpdate------------------------------------------------------------- 

# Load updated Listing File
listingsUpdate = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\listing_update\\listing_update.csv", sep='\t')

# Bar Chart: Top 10 Hosts with most Listings
barPlot_top10Hosts = listingsUpdate['host_id'].value_counts().head(10).plot.bar(title='Top 10 Hosts with most Listings')
barPlot_top10Hosts.set_xlabel("Host ID")
barPlot_top10Hosts.set_ylabel("No. of Listings")

# Horizontal bar chart: Top 5 Neighbourhoods of Listings
barPlotHor_top5Neighbourhoods = listingsUpdate['neighbourhood'].value_counts().head(5).plot.barh(title='Top 5 Neighbourhoods of Listings')
barPlotHor_top5Neighbourhoods.set_xlabel("No. of Listings")
barPlotHor_top5Neighbourhoods.set_ylabel("Neighbourhood")

# Pie Chart: Maximum capacity of Listings
def autopct(pct): # only show the label when it's > 10%
    return ('%.2f' % pct) if pct > 10 else ''

pieChart_Accommodates = listingsUpdate['accommodates'].value_counts().head(10).plot.pie(autopct= autopct,title='Maximum capacity of Listing')
pieChart_Accommodates.set_ylabel("")

# Pie Chart: Review Rating above 4
ReviewScoreAbove4 = listingsUpdate['review_scores_rating'] > 4
pieChart_ReviewScoreAbove4 = ReviewScoreAbove4.value_counts("True").plot.pie(autopct='%1.1f%%',title='Review Rating above 4')
pieChart_ReviewScoreAbove4.set_ylabel("")


'''
!! If we create plots for the review file, this code is helpful, because it merges the review data frames to one.

# Plots for Reviews------------------------------------------------------------- 

# Load updated Review Files & merge them to one dataframe
reviews_update_1 = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_update_1.csv", sep=",")
reviews_update_2 = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_update_2.csv", sep=",")
reviews_update_3 = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_update_3.csv", sep=",")
reviews_update_4 = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\reviews_update\\reviews_update_4.csv", sep=",")

dfs = [reviews_update_1, reviews_update_2, reviews_update_3, reviews_update_4]
reviews_merged_df = pd.concat(dfs)
'''
