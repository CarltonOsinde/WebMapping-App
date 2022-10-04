import folium

#Folium is a python library that allows you to create Maps from python code that are rendered into HTML, JavaScript and CSS
#location's are stored in a list
#-------------------------------------------------------------------------------------------------------------------------#

map = folium.Map(location = [56.1304, -106.3468],zoom_start = 4 ,tiles = "Stamen Terrain")

#Adding Elements to the map object ~ An object allows us to apply method's and functions to do something or show something
#-------------------------------------------------------------------------------------------------------------------------#

##Creating Feature Groups - Allows you to structure code easier by creating one object to pass all your feature groups##
#-------------------------------------------------------------------------------------------------------------------------#

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location = [43.6532, -79.3832], popup="I'm a marker styl", icon=folium.Icon(color ='blue')))

map.add_child(fg)

map.save("Map1.html")    #.save() method creates and generates a world map, zooming in on the longitude and latitude stated above in the .Map() method




