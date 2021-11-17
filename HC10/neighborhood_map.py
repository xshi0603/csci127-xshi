#Name: Xing Tao Shi
#Email: XingTao.Shi50@myhunter.cuny.edu

import folium
import pandas as pd

neighborhood = pd.read_csv('Open_Restaurant_Applications.csv')
grouped_neighborhood = neighborhood.groupby("NTA")
west_concourse = grouped_neighborhood.get_group("West Concourse")

concouse_map = folium.Map(location=[40.768731, -73.964915])

for index,row in west_concourse.iterrows():
  lat = row["Latitude"]
  lon = row["Longitude"]
  name = row["Restaurant Name"]
  newMarker = folium.Marker([lat, lon], popup=name)
  newMarker.add_to(concouse_map)

concouse_map.save(outfile='concourse.html')