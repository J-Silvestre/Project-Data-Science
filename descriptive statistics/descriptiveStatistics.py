# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:11:18 2022

@author: Rosanna
"""
# !! Important note regarding this code: Directories for files need to be changed first!

# import libraries ---------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Plots for listingsUpdate------------------------------------------------------------- 

# Load updated Listing File
#listingsUpdate = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\listing_update\\listing_update.csv", sep='\t')
listingsUpdate = pd.read_csv("C:\\Users\\rodri\\OneDrive\\Documentos\\GitHub\\Project-Data-Science\\listing_update\\listing_update.csv", sep='\t')
reviews= pd.read_csv("C:\\Users\\rodri\\OneDrive - ISEG\\iseg 22092021\\Iseg\\Master\\2semester\\Programing for Data Science\\trabalho\\reviews.csv.gz", compression= "gzip")
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
#Rodrigo part---------------------------------

#Analyzing price before removing outliers
listingsUpdate["price"].describe()

#Boxplot for prices of the listings, clearly shows some outliers
#BoxplotPrice
fig= plt.figure()

BoxplotPrice= fig.add_subplot(111)
BoxplotPrice.boxplot(listingsUpdate["price"])

BoxplotPrice.set_ylabel("price")
BoxplotPrice.set_title("Price of the listings with outliers")

plt.show()


#Removing outliers
PriceQuantileLow = listingsUpdate["price"].quantile(0.01)
PriceQuantileHigh = listingsUpdate["price"].quantile(0.99)
listingsUpdateOut= listingsUpdate[(listingsUpdate["price"]< PriceQuantileHigh) & (listingsUpdate["price"] >PriceQuantileLow)]


#Boxplot without outliers
fig1= plt.figure()

BoxplotPriceOut= fig1.add_subplot(111)
BoxplotPriceOut.boxplot(listingsUpdateOut["price"])

BoxplotPriceOut.set_ylabel("price")
BoxplotPriceOut.set_title("Price of the listings without outliers")

plt.show()

#Analyzing price after removing outliers
listingsUpdateOut["price"].describe()



#Compares the number of super hosts(1) with normal hosts(0)
HostType= listingsUpdate["host_is_superhost"].value_counts().plot.bar(title="Types of hosts")
HostType.set_ylabel("Count")
HostType.set_xlabel("Host")


#Creating a pie chart for top 10 listings with more reviews 
reviewsListing= reviews.groupby("listing_id")

reviewsListing= reviewsListing["comments"].count().reset_index().sort_values("comments", ascending=False).head(10)
reviewsListingPie = reviewsListing.plot(kind='pie', y='comments', autopct="%1.1f%%",
                                 title='Top 10 listings with more reviews')
reviewsListingPie.get_legend().remove()
