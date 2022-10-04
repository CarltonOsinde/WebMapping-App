import pandas as pd
import folium

raw_data1 = pd.read_csv("/Volcanoes.txt")
Lat = list(raw_data1["lat"])
Lon = list(raw_data1["lon"])
elv = list(raw_data1["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation <=3000:
        return 'yellow'
    else:
        return 'red'


#Folium is a python library that allows you to create Maps from python code that are rendered into HTML, JavaScript and CSS
#location's are stored in a list
#-------------------------------------------------------------------------------------------------------------------------#

m = folium.Map(location = [56.1304, -106.3468],zoom_start = 4 ,tiles = "Stamen Terrain")

#Adding Elements to the map object ~ An object allows us to apply method's and functions to do something or show something
#-------------------------------------------------------------------------------------------------------------------------#

##Creating Feature Groups - Allows you to structure code easier by creating one object to pass all your feature groups##
#-------------------------------------------------------------------------------------------------------------------------#

fg = folium.FeatureGroup(name="My Map")


for lt, ln, el in zip(Lat, Lon, elv):
    fg.add_child(folium.Marker(location = [lt,ln], popup=str(el) + "m", icon=folium.Icon(color = color_producer(el))))

m.add_child(fg)






#Rendering Python code to HTML, CSS and JavaScript ~ something the browser can understand 
#NOTE:  #.save() method creates and generates a world map, zooming in on the longitude and latitude stated above in the .Map() method
#-------------------------------------------------------------------------------------------------------------------------#

m.save("Map1.html")   




