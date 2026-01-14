import os
import pandas as pd
import numpy as np


Folder="temperatures"

#adds in dictionary
months=["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

#mapping months to seasons
seasons= {"December": "Summer", "January": "Summer", "February": "Summer",
    "March": "Autumn", "April": "Autumn", "May": "Autumn",
    "June": "Winter", "July": "Winter", "August": "Winter",
    "September": "Spring", "October": "Spring", "November": "Spring"}

data=[]
for file in os.listdir(Folder):
    if file.endswith(".csv"):
        data.append(pd.read_csv(os.path.join(Folder,file)))

df= pd.concat(data, ignore_index=True)# merging all the csv files into one single dataframe


# converting the wide data of the csv to long format. There is column for each 
# month which we are changing to month a single column and Temperature with their temperature value.
temp_df= df.melt(
    id_vars="STATION_NAME",
    value_vars=months,
    var_name="Month",
    value_name="Temperature"
).dropna()


temp_df['Season']=temp_df['Month'].map(seasons)

#season average
season_avg= temp_df.groupby("Season")['Temperature'].mean()

with open("average_temp.txt",'w') as f:  # writing output in a txt file
    for season, avg in season_avg.items():
        f.write(f"{season}:{avg:.1f}C\n")


#largest temperature range

station= temp_df.groupby("STATION_NAME")["Temperature"].agg(
    max_temp='max',
    min_temp='min'
) # using groupby to group station name and its temperature to find the max and the min temperature of the station

station["range"]=station['max_temp']-station['min_temp'] # calculating the range

max_range=station['range'].max() # max range
largest_range_station=station[station["range"]==max_range]

with open("largest_temp_rnage_station.txt",'w') as f: # writing in a txt file
    for stations, row in largest_range_station.iterrows():
        f.write(
            f"{stations}: Range {row['range']:.1f}C "
            f"(Max: {row['max_temp']:.1f}C, Min: {row['min_temp']:.1f}C)\n"
        )
        
#temperature stability

sd= temp_df.groupby("STATION_NAME")["Temperature"].std() #calculating standard deviation

min_sd=sd.min()
max_sd=sd.max()


with open("temperature_stability_stations.txt","w")as f: # writing in a file
    f.write("Most Stable:\n")
    for station in sd[sd==min_sd].index:
        f.write(f"{station}:sd {min_sd:.1f}C\n")

    f.write("Most Variable:\n")
    for station in sd[sd==max_sd].index:
        f.write(f"{station}:sd {max_sd:.1f}C\n")