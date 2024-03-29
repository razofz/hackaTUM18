import csv
from math import sin, cos, sqrt, atan2, radians, acos, pi

class Car:

    def __init__(self, type, gasPerKm, insurancePrize, loseValue):
        self.id = id
        self.type = type
        self.gasPerKm = gasPerKm
        self.insurancePrize = insurancePrize
        self.loseValue = loseValue

    def getMonthlyPriceGas(self, km):
        return self.gasPerKm * km * 22 * 2 * 1.55

    def getMonthlyLossofValue(self, km):
        return self.loseValue * km * 22 * 2

    def getDailyPriceGas(self, km):
        return self.gasPerKm * km * 2 * 1.55

    def getDailyLossofValue(self, km):
        return self.loseValue * km * 2

class Station:
    def __init__(self, name, longitude, latitude, ring):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.ring = ring


def getStations():

    with open('alldata.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        array = []
        for row in spamreader:
            a = ''.join(row).split(";")
            ring = a[6].split(",")
            if (a[3] == "München"):
                i = i + 1

                try:
                    b = a[10]
                    if a[10][-1:] == ",":
                        b = a[10][:-1]
                    array.append(Station(a[1], float(a[9].replace(',','.')), float(b.replace(',','.')), int(ring[0])))
                    #print(b)
                except ValueError:
                    y = 0
                # print(float(a[9])/pow(10,8))
                # print(ring[0])

        return array

'''
#previous get Stations
def getStations():
    ifile = open('alldata.csv', "r")
    read = csv.reader(ifile)
    i = 0
    array = []
    for row in read:
        a = ''.join(row).split(";")
        ring = a[6].split(",")
        if (a[3] == "München"):
            i = i + 1
            try:
                array.append(Station(a[1], float(a[9])/pow(10,8), float(a[10])/pow(10,8), ring[0]))
            except ValueError:
                y = 0
            #print(float(a[9])/pow(10,8))
            #print(ring[0])
    return array
'''
#get the distance between stations (KM)
def getStationsDistance(station1, station2):
    #xDif = abs(station1.latitude - station2.latitude)
    #yDif = abs(station1.longitude - station2.longitude)

    R = 6373.0

    lat1 = radians(station1.latitude)
    lon1 = radians(station1.longitude)
    lat2 = radians(station2.latitude)
    lon2 = radians(station2.longitude)

    dlon = abs(lon2 - lon1)
    dlat = abs(lat2 - lat1)

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    #print("Result:", distance)
    return distance * 1.2

#get Monthly ticket price of 2 different stations
def getMonthlyPriceTransportation(station1, station2):
    array = [55.20, 66.60, 79.10, 90.40, 103.70, 116.50, 127.80, 140.50, 152.50, 163.40, 175.10, 188.00, 201.30, 212.50, 225.60]
    dist = getStationsDistance(station1,station2)
    marien = Station("Mrienplatz", 48.13643422, 11.57765115, 1)
    disttoMarien = getStationsDistance(station1,marien)
    if disttoMarien<dist:
        return max(station1.ring, station2.ring)
    elif (abs(station1.ring - station2.ring) == 0):
        return array[0]
    else:
        return array[abs(station1.ring - station2.ring) - 1]


def getCar(name):
    if name == "Small Car":
        return Car("Small Cars", 0.052, 30, 0.338)
    elif name == "Family Car":
        return Car("Family Car", 0.055, 30, 0.572)
    elif name == "SUV":
        return Car("SUV", 0.0661, 30, 0.868)
    elif name == "Family Bus":
        return Car("Family Bus", 0.0701, 30, 0.764)
    elif name == "Pickup":
        return Car("Pickup", 0.0801, 30, 0.745)

#adac.de for loss of value
def getAllCars():
    array = [Car("Small Cars", 0.052, 30, 0.338),Car("Family Car", 0.055, 30, 0.572), Car("SUV", 0.0661, 30, 0.868), Car("Family Bus", 0.0701, 30, 0.764), Car("Pickup", 0.0801, 30, 0.745)]

    return array

def getDailyPrice(station1, station2):


    dist = getStationsDistance(station1, station2)
    marien = Station("Mrienplatz", 48.13643422, 11.57765115, 1)
    disttoMarien = getStationsDistance(station1, marien)
    if disttoMarien < dist:
        rings = max(station1.ring, station2.ring)
    elif (abs(station1.ring - station2.ring) == 0):
        rings = 1
    else:
        rings = abs(station1.ring - station2.ring)

    if (station1.ring%4 == 0):
        if rings<=4:
            prize = 2.90
        elif rings <= 8:
            prize = 5.80
        elif rings <= 12:
            prize = 8.70
        elif 1==1:
            prize = 11.60
    else:
        if rings<4:
            prize = 2.90
        elif rings < 8:
            prize = 5.80
        elif rings < 12:
            prize = 8.70
        elif 1==1:
            prize = 11.60

    return prize
    '''
    print(a)
    print(rings)
    print(prize)
    '''

def getBicycleCalories(km):

    return km/10 * 300


def getStation(name):
    array = getStations()
    for rows in array:
        if rows.name.find(name):
            x = 0
        else:
            return rows
    return Station("", 49.13916696, 11.56524034, 1)


# allStations = getStations()
# print(getStation("Mar").name)
'''

allStations = getStations()
print(getStation("Mar").name)


stat1 = Station("Marien", 49.13916696, 11.56524034, 1)
stat2 = Station("Karlsplatz", 48.13643422, 11.57765115, 1)
dist = getStationsDistance(stat1, stat2)

print(getMonthlyPriceTransportation(stat1, stat2))
print(dist)
cars = getAllCars()
print(cars[0].getMonthlyLossofValue(dist))
print(getBicycleCalories(dist))




allStations = getStations()
for stationNames in allStations:
    print(stationNames.name)


a = getAllCars()

print(a[0].getMonthlyPriceGas(10))
print(a[0].getMonthlyLossofValue(10))


print (find_angle((12.92473, 77.6183), (12.92512, 77.61923), (12.92541, 77.61985)))

allStations = getStations()
for stationNames in allStations:
    print(stationNames.name)


allStations = getStations()
for stationNames in allStations:
    print(stationNames.name)


a = getStations()
print(a[0].name)


stat1 = Station("Marien", 48.13916696, 11.56524034, 1)
stat2 = Station("Karlsplatz", 48.13643422, 11.57765115, 4)
print(getMonthlyPriceTransportation(stat1, stat2))

stat1 = Station("Marien", 48.13916696, 11.56524034, 1)
stat2 = Station("Karlsplatz", 48.13643422, 11.57765115, 1)
compareStations(stat1, stat2)

#marien = Stations("marienplatz", 48.13, 11.57, 1)
#print ("The station " + marien.name)
'''

