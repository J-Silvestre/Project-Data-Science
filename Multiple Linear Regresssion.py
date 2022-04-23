# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 13:45:58 2022

@author: joaod
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler


listings = pd.read_csv("listing_update.csv", sep = "\t")
neighb = pd.read_csv("neighbourhoods_update.csv", sep = ",")

main = pd.merge(listings, neighb, how="inner", on="neighbourhood_group")
main = main[["price", "number_of_reviews", "calculated_host_listings_count", "availability_365", "host_response_rate", "nr_of_bathrooms", "bedrooms", "review_scores_rating", "coefficient_of_location", "purchase_power_pc", "crime_rate_pc", "population_density"]]


y = (main.price) #target variable
x = main.drop(columns=["price"]) #predictors


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

