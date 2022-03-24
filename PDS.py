# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 13:32:53 2022

@author: joaod
"""

# hello joao

#rodrigo
import pandas as pd
data = pd.read_csv("C:\\Users\\rodri\\Downloads\\calendar.csv.gz", compression='gzip',
                   error_bad_lines=False)
print(data.tail)