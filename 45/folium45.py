#Name: Xing Tao Shi
#Email: XingTao.Shi50@myhunter.cuny.edu

import folium
import pandas as pd
'''
inputFile = "NYC_Wi-Fi_Hotspot_Locations.csv"
outputFile = "manhattan.html"
boroughName = "New York" 
'''
inputFile = input("Please enter the name of the input file: ")
outputFile = input("Please enter the name of the output file: ")
boroughName = input("Please enter the name of the borough: ")

hotspots = pd.read_csv(inputFile)
grouped_hotspots = hotspots.groupby("City")
borough = grouped_hotspots.get_group(boroughName)

map = folium.Map(location=[40.768731, -73.964915])

for index,row in borough.iterrows():
  lat = row["Latitude"]
  lon = row["Longitude"]
  name = row["Name"]
  newMarker = folium.Marker([lat, lon], popup=name)
  newMarker.add_to(map)

map.save(outfile=outputFile)