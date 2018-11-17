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




class Station:
    def __init__(self, name, longitude, latitude, ring):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.ring = ring


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
    return distance
    return distance * 1.2

#get Monthly ticket price of 2 different stations
def getMonthlyPriceTransportation(station1, station2):
    array = [55.20, 66.60, 79.10, 90.40, 103.70, 116.50, 127.80, 140.50, 152.50, 163.40, 175.10, 188.00, 201.30, 212.50, 225.60]

    if (abs(station1.ring - station2.ring) == 0):
       return array[0]
    else:
        return array[abs(station1.ring - station2.ring)-1]


#adac.de for loss of value
def getAllCars():
    array = [Car("Small Cars", 0.052, 30, 0.338),Car("Family Car", 0.055, 30, 0.572), Car("SUV", 0.0661, 30, 0.868), Car("Family Bus", 0.0701, 30, 0.764), Car("Pickup", 0.0801, 30, 0.745)]

    return array







def find_angle( p0, p1, p2 ):
    a = (p1[0]-p0[0])**2 + (p1[1]-p0[1])**2
    b = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    c = (p2[0]-p0[0])**2 + (p2[1]-p0[1])**2
    return acos( (a+b-c) / sqrt(4*a*b) ) * 180/pi

'''

#prints all the starion names
allStations = getStations()
for stationNames in allStations:
    print(stationNames.name)

'''

