# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:11:18 2022

@author: Rosanna
"""

# import libraries ---------------------------------------------------------------------
import pandas as pd


# Plots for listingsUpdate------------------------------------------------------------- 

listingsUpdate = pd.read_csv("C:\\Users\\Rosan\\Documents\\GitHub\\listing_update\\listing_update.csv", sep='\t')

# Bar Chart: Top 10 Hosts with most accommodations
barPlot_top10Hosts = listingsUpdate['host_id'].value_counts().head(10).plot.bar(title='Top 10 Hosts with most accommodations')
barPlot_top10Hosts.set_xlabel("Host ID")
barPlot_top10Hosts.set_ylabel("No. of accommodations")

