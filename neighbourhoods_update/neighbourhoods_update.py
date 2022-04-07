# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:05:48 2022

@author: joaod
"""

import numpy as np
import pandas as pd

df_neigh = pd.read_csv("Neighbourhoods.csv", sep=",")

df_purch = pd.read_excel("Purchase_power_pc.xlsx",sheet_name="Sheet1")
df_crime = pd.read_excel("Crime_rate_pc.xlsx",sheet_name="Sheet1")
df_pop = pd.read_excel("Population_density.xlsx", sheet_name="Sheet1")

list1 = [df_purch, df_crime, df_pop]

for i in range(len(list1)):
    df_neigh= pd.merge(df_neigh, list1[i], how="inner", on="neighbourhood_group")

df_neigh.to_csv("neighbourhoods_update.csv", sep=",")



