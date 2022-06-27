# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:57:44 2022

@author: user
"""

import pandas as pd
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.stats import norm

dataFrame = pd.read_csv("BankNifty.csv");

dataFrame = dataFrame.dropna(axis=1); # drop null valued columns

dataFrame['time'] = pd.to_datetime(dataFrame['time']);
dataFrame["weekday"] = dataFrame["time"].dt.weekday
dataFrame["range_HL"] = dataFrame["high"]-dataFrame["low"]; # range from high to low
dataFrame["range_OC"] = abs(dataFrame["open"]-dataFrame["close"]); # range from open to close

conditions = [dataFrame["open"] < dataFrame["close"],dataFrame["open"] > dataFrame["close"]]
dataFrame["type"] = np.select(conditions, ['bull','bear'], default='Tie')

Mean = dataFrame['range_HL'].mean();
std = np.std(dataFrame['range_HL']) 
mean = np.mean(dataFrame['range_HL'])    


fig1, ax = plt.subplots(1,1,dpi=100)
#ax.plot(dataFrame['Date'],dataFrame['Range'])
ax.plot(norm.pdf(dataFrame['range_HL'],mean,std))
ax.set_xlabel('time')
ax.set_ylabel('range')
#ax.axhline(Mean,xmin=0,xmax=1, linestyle='--',color='m',alpha=1)

sideways = len(dataFrame[dataFrame['range_HL']<=Mean]);

dataFrame.to_csv('./banknifty_data.csv')