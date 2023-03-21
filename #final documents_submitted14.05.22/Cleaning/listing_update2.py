#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 23:04:51 2022

@author: marcb
"""

import pandas as pd 
import numpy as np 
import os 


os.chdir('/Users/marcb/Documents/Studies/ISEG/Semester II /programming/Project-Data-Science')


listing_summary = pd.read_csv('listing_summary.csv')
listings = pd.read_csv('listings.csv')


listing_summary = pd.DataFrame(listing_summary)
listings = pd.DataFrame(listings)


# Select variables needed from listings

listings = listings[['id','host_response_time','host_identity_verified','host_response_rate','host_is_superhost','bathrooms_text','bedrooms','accommodates','review_scores_rating','review_scores_cleanliness','review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value']]


# Merge both data sources 
listing_update = pd.merge(listing_summary,listings, on="id")



# Remove missing values 
listing_update= listing_update.dropna()

len(listing_update)

# 11094 observations without missing values 



# Transform 

listing_update['bathrooms_text'] = listing_update['bathrooms_text'].str.split(' ').str[0]

listing_update['bathrooms_text'].unique()


# 'Private','Shared','Half-bath'

rem = ['Private','Shared','Half-bath']

listing_update['bathrooms_text'] = listing_update['bathrooms_text'].replace(rem, np.nan)

listing_update= listing_update.dropna()

listing_update['bathrooms_text'] = pd.to_numeric(listing_update['bathrooms_text'])

listing_update.rename(columns = {'bathrooms_text':'nr_of_bathrooms'}, inplace = True)



len(listing_update)

# 11060 observations without missing values 


# Room Type

listing_update['room_type'].unique()

# Recoding scheme 

# 'Shared room' = 1
# 'Private room' = 2
# 'Hotel room' = 3
# 'Entire home/apt' =4 

code = [1,2,3,4]
typeI = ['Shared room','Private room','Hotel room','Entire home/apt']

listing_update['room_type'] = listing_update['room_type'].replace(typeI , code)


# host response time
listing_update['host_response_time'].unique()
typeII = ['a few days or more','within a day','within a few hours', 'within an hour']

listing_update['host_response_time'] = listing_update['host_response_time'].replace(typeII , code)


# 'within an hour' = 4
# 'within a few hours'  = 3
# 'within a day' = 2
# 'a few days or more' =1




# Superhost 
# True = 1 & False = 0 

code2 = [1,0]
typeIII = ['t','f']

listing_update['host_is_superhost'] = listing_update['host_is_superhost'].replace(typeIII , code2)



# Host identity verified 
# True = 1 & False = 0 

listing_update['host_identity_verified'] = listing_update['host_identity_verified'].replace(typeIII , code2)



# Host response rate to decimal 

listing_update['host_response_rate'] = pd.to_numeric(listing_update['host_response_rate'].str.split('%').str[0])
listing_update['host_response_rate'] = (listing_update['host_response_rate']/100)


listing_update.pop('name')
listing_update.pop('license')
listing_update.pop('host_name')
listing_update.pop('last_review')



listing_update.to_csv('listing_update.csv', sep='\t')





