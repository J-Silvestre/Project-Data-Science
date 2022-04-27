#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 13:58:48 2022

@author: marcb
"""

import pandas as pd 
import os 
import numpy as np 
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn import linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.metrics import mean_absolute_error
from numpy import absolute


os.chdir('/Users/marcb/Documents/Studies/ISEG/Semester II /programming/Project-Data-Science')

listings = pd.read_csv("listing_update/listingsUpdateOut.csv")


neighb = pd.read_csv("neighbourhoods_update/neighbourhoods_update.csv", sep = ",")



main = pd.merge(listings, neighb, how="inner", on="neighbourhood_group")
main = main[["price", "number_of_reviews",'minimum_nights', "calculated_host_listings_count", "availability_365", "host_response_rate", "nr_of_bathrooms", "bedrooms", "review_scores_rating", "purchase_power_pc", "crime_rate_pc", "population_density"]]


data = main[['review_scores_rating','price','minimum_nights','number_of_reviews',
             'calculated_host_listings_count','availability_365','bedrooms',"purchase_power_pc", "crime_rate_pc", "population_density"]] 


data['price'].describe()
data['population_density'].describe()


sns.histplot(data=data, x='purchase_power_pc', binwidth=3)

sns.histplot(data=data, x='crime_rate_pc', binwidth=3)



#10  minimum_nights                  10195 non-null  int64  
#11  number_of_reviews               10195 non-null  int64  
#12  reviews_per_month               10195 non-null  float64
#13  calculated_host_listings_count  10195 non-null  int64  
#14  availability_365                10195 non-null  int64  
#15  number_of_reviews_ltm           10195 non-null  int64  
#16  host_response_time              10195 non-null  int64  
#17  host_identity_verified          10195 non-null  int64  
#18  host_response_rate              10195 non-null  float64
#19  host_is_superhost               10195 non-null  int64  
#20  nr_of_bathrooms                 10195 non-null  float64
##21  bedrooms                        10195 non-null  float64
#22  accommodates     



#g = sns.PairGrid(data)
#g.map_diag(sns.histplot)
#g.map_offdiag(sns.scatterplot)
#g.add_legend()



#Removing outliers for all variables
# Outliers are defined as values > 3 standard deviations from mean


data = pd.DataFrame(data)

data_out = data[(np.abs(stats.zscore(data)) < 3).all(axis=1)]


##########

#g = sns.PairGrid(data_out)
#g.map_diag(sns.histplot)
#g.map_offdiag(sns.scatterplot)
#g.add_legend()

###########



#create log-transformed data
data_log = np.log(data_out)

data_log.info()

g = sns.PairGrid(data_log)
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()



########################

## Correlation Matrix 

df = pd.DataFrame(data_log)
corr = df.corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)


########################


### Scatterplots 



sns.scatterplot(data=data_log, y='price', x='bedrooms')

sns.scatterplot(data=data_log, y='price', x='review_scores_rating')


y = (data_log['price']) #target variable

x = data_log[['bedrooms','review_scores_rating']] #predictors


# splitting training and testing data

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3, random_state=1)


#y_train = y_train.reshape(-1,1)
#y_test = y_test.reshape(-1,1)


#x_test = x_test.reshape(-1,1)
#x_train = x_train.reshape(-1,1)

#fitting the model to the training data


model = lm.LinearRegression()
model.fit(x_train, y_train)


#predicting y values
y_pred = model.predict(x_test)

# Mean Squared Error
MSE = mean_squared_error(y_test,y_pred)



R2 = r2_score(y_test,y_pred)

print(R2)
print(model.intercept_)
print(model.coef_)
print(MSE)

##########


# Boosting the Regression with XG-Boost

model = XGBRegressor()
define model evaluation method
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
evaluate model
scores = cross_val_score(model, x, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
force scores to be positive
scores = absolute(scores)

scores_s = (scores)**2

print('Mean MSE: %.3f (%.3f)' % (scores_s.mean(), scores.std())) 











