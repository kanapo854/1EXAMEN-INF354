# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 08:40:30 2022

@author: Display
"""

import pandas
import numpy as np
from sklearn import preprocessing
filename='Raisin_Dataset.csv' 
data=pandas.read_csv(filename, header=0)
x_data=np.array(data['Class'])
etiquetar=preprocessing.LabelEncoder()
la_data=etiquetar.fit_transform(x_data)
print(la_data)