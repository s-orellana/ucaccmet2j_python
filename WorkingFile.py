#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:44:04 2018

@author: sorellana
"""
import json
import csv

#Bring in data
with open('precipitation.json') as Data: 
    Precipitation_Data = json.load(Data) 

with open('stations.csv') as csvfile:
    StationData = csv.reader(csvfile, delimiter=',')
    Station_Location = []
    Station_Code =[]
    for row  in  StationData: #Makings sperate lists for station name & code
        Station_Location.append(row[0])
        Station_Code.append(row[2])
        
print(Station_Location)
print(Station_Code)

MetaList={}

#Attaching Location name to the precipitation data - Allows selection. 
#Creates four groups of data (one per city)
for item, code in zip(Station_Location[1:], Station_Code[1:]):
    MetaList[item] = []
    for point in Precipitation_Data[0:]:
        if point['station'] == code:
            MetaList[item].append(point)
    
#print(MetaList)



#--- Getting precipitation 
list_ofMonths = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11','12']
PPM = []
Daily_values= []

for name in Station_Location[1:]:
    Temp_City = MetaList[name] #subsets data for the city in current loop
    for month in list_ofMonths: # run through a month
        for datapoint in Temp_City:
            if datapoint['date'][-5:-3] == month:  # does your data match?
                Daily_values.append(datapoint['value'])
                
# From here on: I wanted to create a list of rain per month, per city (as in a list two levels deep: city - 
# and the a list of per month measurements.)
            
    
print(Daily_values)
   
   
   


        
       
        
        
        
        
   
   