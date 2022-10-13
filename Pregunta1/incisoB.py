# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:02:45 2022

@author: Display
"""

import math
def percentile(N, percentaje, key=lambda x:x):
    i=(len(N)-1)*percentaje
    men=math.floor(i)
    may=math.ceil(i)
    if men == may:
        return key(N[int(i)])
    d0 = key(N[int(men)])*(may-i)
    d1 = key(N[int(may)])*(i-men)
    return d0+d1
import numpy as np
import pandas
filename ="Raisin_Dataset.csv"
data =pandas.read_csv(filename, header=0)

print("python - pandas - numpy")
columna=np.array(data['Area'])
columna.sort()
per1=percentile(columna, 0.9) 
per2=percentile(columna, 0.95)
cuar=percentile(columna, 0.25)
print("Percentil 90:\t\t",per1)
print("Percentil 95:\t\t",per2)
print("1cuartil:\t\t\t",cuar)

print("Media: \t\t\t\t",data['Area'].median())
print("1cuartil:\t\t\t",data['Area'].quantile(0.25))   
print("Percentil 90:\t\t",np.percentile(data['Area'],90))  
print("Percentil 95:\t\t",np.percentile(data['Area'],95)) 

print("python - pandas - numpy")
columna=np.array(data['MajorAxisLength'])
columna.sort()
per1=percentile(columna, 0.9) 
per2=percentile(columna, 0.95)
cuar=percentile(columna, 0.25)
print("Percentil 90:\t\t",per1)
print("Percentil 95:\t\t",per2)
print("1cuartil:\t\t\t",cuar)

print("Media:\t\t\t\t",data['MajorAxisLength'].median())
print("1cuartil:\t\t\t",data['MajorAxisLength'].quantile(0.25))   
print("Percentil 90:\t\t",np.percentile(data['MajorAxisLength'],90))  
print("Percentil 95:\t\t",np.percentile(data['MajorAxisLength'],95))

print("python - pandas - numpy")
columna=np.array(data['MinorAxisLength'])
columna.sort()
per1=percentile(columna, 0.9) 
per2=percentile(columna, 0.95)
cuar=percentile(columna, 0.25)
print("Percentil 90:\t\t",per1)
print("Percentil 95:\t\t",per2)
print("1cuartil:\t\t\t",cuar)

print("Media:\t\t\t\t",data['MinorAxisLength'].median())
print("1cuartil:\t\t\t",data['MinorAxisLength'].quantile(0.25))   
print("Percentil 90:\t\t",np.percentile(data['MinorAxisLength'],90))  
print("Percentil 95:\t\t",np.percentile(data['MinorAxisLength'],95)) 

print("python - pandas - numpy")
columna=np.array(data['Eccentricity'])
columna.sort()
per1=percentile(columna, 0.9) 
per2=percentile(columna, 0.95)
cuar=percentile(columna, 0.25)
print("Percentil 90:\t\t",per1)
print("Percentil 95:\t\t",per2)
print("1cuartil:\t\t\t",cuar)

print("Media:\t\t\t\t",data['Eccentricity'].median())
print("1cuartil:\t\t\t",data['Eccentricity'].quantile(0.25))   
print("Percentil 90:\t\t",np.percentile(data['Eccentricity'],90))  
print("Percentil 95:\t\t",np.percentile(data['Eccentricity'],95)) 

print("python - pandas - numpy")
columna=np.array(data['ConvexArea'])
columna.sort()
per1=percentile(columna, 0.9) 
per2=percentile(columna, 0.95)
cuar=percentile(columna, 0.25)
print("Percentil 90:\t\t",per1)
print("Percentil 95:\t\t",per2)
print("1cuartil:\t\t\t",cuar)

print("Media:\t\t\t\t",data['ConvexArea'].median())
print("1cuartil:\t\t\t",data['ConvexArea'].quantile(0.25))   
print("Percentil 90:\t\t",np.percentile(data['ConvexArea'],90))  
print("Percentil 95:\t\t",np.percentile(data['ConvexArea'],95)) 

print("python - pandas - numpy")
columna=np.array(data['Extent'])
columna.sort()
per1=percentile(columna, 0.9) 
per2=percentile(columna, 0.95)
cuar=percentile(columna, 0.25)
print("Percentil 90:\t\t",per1)
print("Percentil 95:\t\t",per2)
print("1cuartil:\t\t\t",cuar)


print("Media:\t\t\t\t",data['Extent'].median())
print("1cuartil:\t\t\t",data['Extent'].quantile(0.25))   
print("Percentil 90:\t\t",np.percentile(data['Extent'],90))  
print("Percentil 95:\t\t",np.percentile(data['Extent'],95)) 

print("python - pandas - numpy")
columna=np.array(data['Perimeter'])
columna.sort()
per1=percentile(columna, 0.9) 
per2=percentile(columna, 0.95)
cuar=percentile(columna, 0.25)
print("Percentil 90:\t\t",per1)
print("Percentil 95:\t\t",per2)
print("1cuartil:\t\t\t",cuar)

print("Media:\t\t\t\t",data['Perimeter'].median())
print("1cuartil:\t\t\t",data['Perimeter'].quantile(0.25))   
print("Percentil 90:\t\t",np.percentile(data['Perimeter'],90))  
print("Percentil 95:\t\t",np.percentile(data['Perimeter'],95)) 