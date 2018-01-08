#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:44:04 2018

@author: sorellana
"""

'''
# ----------------------------PART 1----------------------------

'''

#Importing JSON data
import json

with open('precipitation.json') as Data: 
    Precipitation_Data = json.load(Data) 

#Define Seattle Station Code:
SeattleStation = 'GHCND:US1WAKG0038'

# --- Selecting Seattle measurements

SeattleData= []
for item in Precipitation_Data[0:]:
   if item['station'] == SeattleStation: #Select measurements
     SeattleData.append(item) #store them in a llist
   #print(SeattleData) #Visual check


''' 
--- Small scale version of the exercise - Summing PRP for january

sum_jan=[] 
for item in SeattleData[0:]:
    if item['date'][-5:-3] == '01':
        sum_jan.append(item['value'])
sum_jan = sum(sum_jan)
#print(sum_jan)
       
'''

 #---- Summing PRP for PER MONTH 
list_ofMonths = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11','12']
PPM= [] # list to store month & total preicipitation as key-value pairs in
#PPM = Precipitation per month

for month in list_ofMonths:
    Temporary_List =[]
    for item in SeattleData[0:]: #loop through seattle data
        if item['date'][-5:-3] == month: 
            Temporary_List.append(item['value']) #Store
    PPM.append(sum(Temporary_List))  #sum daily values, add them to list
   # Precip_PMonth.append({'%s' %(month): sum(Temporary_List)})  #Alternative version

print(PPM) # see output 

#---- Saving to a JSON file

import json
with open('PART1_PPM.json', 'w') as JsonFile:
    json.dump(PPM, JsonFile)

        
        
        
        
        
        
        
        
        
        
        
   
   