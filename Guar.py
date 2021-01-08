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

weather = pd.read_csv('GuarWeather_Clovis_2018.csv')

with open('GuarWeather_Clovis_2018.txt', 'w') as f: weather.to_string(f, col_space = 10, index=False, justify = 'left') # Prepares the weather data that is in the csv to the format that the aquacrop code needs it in (ten spaces between each value)

wdf = prepare_weather('GuarWeather_Clovis_2018.txt')

print(wdf)

soil = SoilClass('ClayLoamGuarClovis2018')

crop = CropClass('Guar2018', PlantingDate='06/15',HarvestDate='11/16')

model = AquaCropModel('2018/06/15','2018/11/16', wdf,soil,crop) # (SimStartTime,SimEndTime,wdf,Soil,Crop...)

# print(wdf.Date.iloc[0])


model.initialize() # Had to change the inputs to be GDD... even though they definitely are not in GDD but that is what Maize used and it worked

model.step(till_termination=True)
# final = model.Outputs.Final; final
# final.Yield.plot()
# print(final)
# plt.xlabel('Season') # seaons is the same as year. 2000 = 0, 2001 = 1, etc
# plt.ylabel('Yield')
