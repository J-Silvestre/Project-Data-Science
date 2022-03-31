# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 13:32:53 2022

@author: joaod
"""

# What are the factors that make an airbnb accomodation more attractive?
# External Data: Crime-Rate per municipality (Pordata)
# External Data: Weather per municipality (Openweather)
# External Data: Proximity to Lisbon City Centre, Proximity to Coast (ourselves)

# Measure attractiveness through the number of days an appartment is rented

# Extra: Logistic Regression to predict if our appartment would be rented given a set of regressors


#https://zonamentopf.portaldasfinancas.gov.pt/simulador/default.jsp








# Chapter on Geospatialdata 

# Potential of a Geographic analysis 

# - In which regions is the highest density of appartments 
# - Where are appartments with high ratings? 
# - Where are the most expensive appartments?

import fiona
import geopandas as gpd
import os 
import pandas as pd
import plotly.express as px
import json
import plotly.io as pio


# Working directory 

path = "/Users/marcb/Documents/Studies/ISEG/Semester II /programming/project"

os.chdir(path)


# Load the geojson 
neighbourhoods = gpd.read_file('neighbourhoods.geojson')

print(neighbourhoods)


# Plot the Map

neighbourhoods.plot()


# Listings are containing all the appartments
listings = pd.read_csv('listings.csv')
listings
listings.dtypes


# Aggregate the number of appartments availiable in a certain neighborhood

data = listings.groupby(listings['neighbourhood'],as_index=False).size()

fig = px.choropleth(data, locations='neighbourhood', geojson=neighbourhoods, color="size", scope="europe")

#fig.update_geos(fitbounds='geojson',visible = False)

fig.show()


# testing stuff







