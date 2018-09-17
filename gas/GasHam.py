'''
This program is only configured to Hamilton, ON.
It does, however, work for any modified version on the below URL.
Ex, Calgary gas price URL is http://www.calgarygasprices.com/

Example of what url will look like for parts of hamilton
http://www.hamiltongasprices.com/GasPriceSearch.aspx?area=Hamilton+-+West
#change to east, north, south etc

Note: All data is webscraped from GasBuddy based on user inputted gas prices.
'''

from urllib.request import Request, urlopen, FancyURLopener
import re
import geocoder
from math import cos, sqrt

# getting access to HTML corresponding to URL
class PlzOpen(FancyURLopener):
    version = "Mozilla/61.0.1"


print("""
Welcome!!
You will be asked which city/neighbourhood in hamilton you want to look for gas in.
""")


city = "Hamilton"
town = input("Enter city/area: ")

# different neighbourhoods of Hamilton 
if town == "hamilton" or town == "Hamilton":
    t = "%20".join(town)
    print("""
    1: Mountain
    2: South
    3: East
    4: West
    """)
    area = int(input("Enter area/neighbourhood of Hamilton: "))
    if area == 4:
        response = PlzOpen().open(
            "http://www.hamiltongasprices.com/GasPriceSearch.aspx?area=Hamilton+-+West")
    elif area == 3:
        response = PlzOpen().open(
            "http://www.hamiltongasprices.com/GasPriceSearch.aspx?area=Hamilton+-+East")
    elif area == 2:
        response = PlzOpen().open(
            "http://www.hamiltongasprices.com/GasPriceSearch.aspx?area=Hamilton+-+South")
    elif area == 1:
        response = PlzOpen().open(
            "http://www.hamiltongasprices.com/GasPriceSearch.aspx?area=Hamilton+mountain")

# another area within Hamilton (e.g: Ancaster)
else:
    town = town.split()
    t = "%20".join(town)
    response = PlzOpen().open('http://www.'+city +
                              'gasprices.com/index.aspx?fuel=A&area='+t+'&dl=Y&intro=Y')

# user entered address (e.g: 1280 Main Street)
my_address = input("Enter your address (# Example Street): ")
my_address += ", Hamilton ON"
print("\nGetting data, might take a few seconds...\n")

# parse through the HTML and find data
gasprices, locations, brands = [], [], []
for line in response:
    if '"price_num"' in str(line):
        line_with_gas = str(line)
        find_gas = re.findall("\d+\.\d+", line_with_gas)
        gasprices.append(float(''.join(find_gas)))
    if "<dd>" in str(line):
        line_with_location = str(line)
        find_location = re.findall("<dd>(.*?)</dd>", line_with_location)
        find_location = "".join(find_location)
        if "&amp;" in find_location:
            find_location = find_location.replace("&amp;", "&")
            locations.append(find_location)
        else:
            if find_location == " " or find_location == '':
                pass
            else:
                locations.append(find_location)
    if "Gas_Stations" in str(line):
        line_with_brand = str(line)
        find_brand = re.findall(
            '<a href="/(.*?)_Gas_Stations', line_with_brand)
        brands.append("".join(find_brand))

# configuring to implement Geocoder
'''
Geocoder requires a specific format of address in order to return a pair
of latitude and longitude coordinates.
'''
for i in range(0, len(locations)):
    locations[i] = locations[i].split()
    locations[i] = locations[i][:3]
    if locations[i][2] == "St":
        locations[i][2] = "Street"
    elif locations[i][2] == "Ave":
        locations[i][2] = "Avenue"
    elif locations[i][2] == "Dr":
        locations[i][2] = "Drive"
    elif locations[i][2] == "Blvd":
        locations[i][2] = "Boulevard"
    elif locations[i][2] == "Rd":
        locations[i][2] = "Road"
    locations[i] = " ".join(locations[i])

# now, to get the coordinates of these addresses
geographic_locations = []
province = "ON"
for address in locations:
    geocoords = geocoder.google(address + " , " + city + province)

    # list of floats corresponding to [lat, lng] of location of gas station
    g = geocoords.latlng
    geographic_locations.append(g)

'''
I've noticed that getting the coords for address sometimes leads to a noneType.
getHomeCoords continues to run the geocoder functions until it properly
gets the coordinates.
'''
def getHomeCoords():
    my_house = geocoder.google(my_address)
    try:
        # lat of my house (float)
        my_house_lat = my_house.latlng[0]
        # lng of my house (float)
        my_house_lng = my_house.latlng[1]
        if type(my_house_lng) != float or type(my_house_lat) != float:
            getHomeCoords()
        else:
            return my_house_lat, my_house_lng
    except:
        getHomeCoords()

'''
Sometimes this sill doesn't catch the noneType which results in quitting and
running the program all over again.
'''
try:
    my_house_lat, my_house_lng = getHomeCoords()
except:
    print("\nSorry, something went wrong: run the program again\n")
    quit()

'''
If there are noneType values, geographic_locations will still have them appended.
Each appended value is of type list.
So to check, iterate through and find which index does not contain a list.
Deleting the corresponding element from the other lists will maintain equal length
I am not completely sure why only sometimes a noneType occurs...but it does.
'''
#pnt = possibleNoneType
noneTypes = 0
for pnt in geographic_locations:
    if type(pnt) != list:
        index_where_it_occurs = geographic_locations.index(pnt)
        del(geographic_locations[geographic_locations.index(pnt)])
        del(locations[index_where_it_occurs])
        del(brands[index_where_it_occurs])
        del(gasprices[index_where_it_occurs])
        noneTypes += 1

# approximate conversions based on:
# https://stackoverflow.com/questions/1253499/simple-calculations-for-working-with-lat-lon-km-distance

'''
Also getting errors saying that noneType is not subscriptable -> throwing in
excpetion to catch this error.
'''
def calcDistance(geog_loca, lat, lng):
    distances = []
    for cord in range(len(geog_loca)):
        try:
            lat_to_gas = (lat - geog_loca[cord][0])*110.574  # km
            lng_to_gas = (lng - geog_loca[cord][1]) * \
                111.320*cos(lat-geog_loca[cord][0])
            distances.append(round(sqrt(lat_to_gas**2 + lng_to_gas**2), 2))
            # doesn't take into account roads -> add a plus/minus buffer
        except:
            pass
    return distances


dist = calcDistance(geographic_locations, my_house_lat, my_house_lng)


def again():
    ask = input("\n\nAgain? Enter yes or no: ")
    if ask == "yes":
        gasloop(dist)
    else:
        print("\nQuitting...\n")
        quit()


def gasloop(d):
    print("""
    1: Gas stations within 5 km of your address
    2: Gas stations within X km of your address
    3: All gas stations
    4: Quit\n""")
    option = int(input("Enter one of the numbers above: "))
    # 3: all""", town, """gas stations

    # write conditions
    if option == 1:
        print("\n")
        for k in range(0, len(d)):
            if dist[k] <= 5.5:  # adding a 500m error
                print(str(gasprices[k]), "-->", brands[k], "at",
                      locations[k], "which is about", dist[k], "km away")
            else:
                pass
        again()

    elif option == 2:
        x = int(input("Enter a distance: "))
        print("Gas stations in", ' '.join(town), "at most", x, "km from you\n")
        for k in range(0, len(d)):
            if dist[k] <= (x+0.5):
                print(str(gasprices[k]), "-->", brands[k], "at",
                      locations[k], "which is about", dist[k], "km away")
            else:
                pass
        again()

    elif option == 3:
        print("\n")
        for k in range(0, len(d)):
            print(str(gasprices[k]), "-->", brands[k], "at",
                  locations[k], "which is about", dist[k], "km away")
        again()

    elif option == 4:
        print("Quitting...\n")
        quit()

    # 5: specific brand gas stations
    # can be extended for many more options
    # ...
    # or locations


gasloop(dist)

'''counts the amount of gas stations that could not be found'''
# if noneTypes > 0:
#print("\nnote: data could not be found for", noneTypes, "gas station(s)\n")

"""proper conversion
https://stackoverflow.com/questions/365826/calculate-distance-between-2-gps-coordinates
"""
