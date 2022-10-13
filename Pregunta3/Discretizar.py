# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 08:29:26 2022

@author: Display
"""

import pandas as pd
import numpy as np

from sklearn.preprocessing import KBinsDiscretizer
filename="Raisin_Dataset.csv" 
data=pd.read_csv(filename, header=0)
x_data=np.array(data)
dis=KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
y_data=dis.fit_transform(x_data)
print(y_data)

