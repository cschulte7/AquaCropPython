# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:01:04 2020

@author: carol
"""

import sys
import csv
_=[sys.path.append(i) for i in ['.', '..']] # finds 'AquaCrop' file

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from aquacrop.core_Guar import *
from aquacrop.classes_Guar import *

weather = pd.read_csv('GuarWeather_Clovis.csv')

print(weather)
Columns = len(list(weather))
print(Columns)

with open('GuarWeather_Clovis.txt', 'w') as f: weather.to_string(f, col_space = 10) # Prepares the weather data that is in the csv to the format that the aquacrop code needs it in (ten spaces between each value)

wdf = prepare_weather('GuarWeather_Clovis.txt')
print(wdf)


# df = pd.read_csv('GuarWeather_Clovis.txt')
# df_new = df[['Day','Month','Year','MinTemp','MaxTemp','Precipitation','ReferenceET']]
# df_new = df[['Day', 'Month', 'Year', 'Tmin(C)', 'Tmax(C)', 'Pcrp(mm)', 'ET0(mm)']]
# df_new.to_csv('sample_text_file_new.txt', header=True, index=None)


soil = SoilClass('ClayLoamGuarClovis2018')

crop = CropClass('Guar2018', PlantingDate='06/15',HarvestDate='05/09')

# Checks that the date is still in the correct location for AquaCrop to read it
print(wdf.Date.iloc[0])


model = AquaCropModel('2018/06/15','2020/06/15', wdf,soil,crop) # (SimStartTime,SimEndTime,wdf,Soil,Crop...)


# Removes first column in the text file (the blank one)

f = open("GuarWeather_Clovis.txt", "r")
g = open("GuarWeather_ClovisFix.txt", "w")

g.writelines('Date    ')

for line in f:
    if line.strip():
        g.write("\t".join(line.split()[1:]) + "\n")
f.close()
g.close()

# Filters the text file columns 
'''
filtered_columns = ['MinTemp','MaxTemp','Precipitation','ReferenceET', 'Date']
wdf_filtered = wdf.reindex(columns = filtered_columns)
print(wdf_filtered)
'''

# Checks the column names in weather file
with open('GuarWeather_ClovisFix.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

wdf = prepare_weather('GuarWeather_ClovisFix.txt')
print(wdf)

model.initialize()

#model.step(till_termination=True)
#final = model.Outputs.Final; final
#final.Yield.plot()
#print(final)
#plt.xlabel('Season') # seaons is the same as year. 2000 = 0, 2001 = 1, etc
#plt.ylabel('Yield')
